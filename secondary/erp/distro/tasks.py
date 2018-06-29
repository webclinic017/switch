from __future__ import absolute_import
from celery import shared_task
# from celery.contrib.methods import task_method
from celery import task
from switch.celery import app
from celery.utils.log import get_task_logger

from django.shortcuts import render
from django.contrib.auth.models import User
# from upc.backend.wrappers import *
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
import time, os, random, string, json
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.gis.geos import Point
from django.conf import settings
from django.core.files import File
import base64, re
from decimal import Decimal, ROUND_UP, ROUND_DOWN
from django.db.models import Max
from .models import *

import logging

lgr = logging.getLogger('secondary.erp.distro')


class Wrappers:
    pass


class System(Wrappers):
    def register_agent(self, payload, node_info):
        try:
            gateway_profile = GatewayProfile.objects.get(id=payload['gateway_profile_id'])
            session_gateway_profile = GatewayProfile.objects.get(id=payload['session_gateway_profile_id'])

            status = AgentStatus.objects.get(name='CREATED')
            agent = Agent(profile=session_gateway_profile.user.profile, status=status,
                          registrar=gateway_profile.user.profile)
            agent.save()
            payload['response'] = 'Profile Registered'
            payload['response_status'] = '00'
        except Exception, e:
            payload['response_status'] = '96'
            lgr.info("Error on register agent: %s" % e)
        return payload

    def get_trading_institution_details(self, payload, node_info):
        try:
            institution = Institution.objects.get(id=payload['institution_id'])
            trading_institution_list = TradingInstitution.objects.filter(institution=institution)
            if trading_institution_list.exists():
                trading_institution = trading_institution_list[0]
                payload['suppliers'] = ','.join([str(x.institution.id) for x in trading_institution.supplier.all()])
                payload['trader_type'] = trading_institution.trader_type.name

            payload['response'] = 'Got Trading institution details'
            payload['response_status'] = '00'
        except Exception, e:
            payload['response_status'] = '96'
            lgr.info("Error Getting Trading institution details: %s" % e)
        return payload

    def get_trading_institution(self, payload, node_info):
        try:
            gateway_profile = GatewayProfile.objects.get(id=payload['gateway_profile_id'])
            institution = Institution.objects.get(id=payload['institution_id'])
            agent = Agent.objects.get(profile=gateway_profile.user.profile)
            trading_institution_list = TradingInstitution.objects.filter(institution=institution, agent=agent)
            if trading_institution_list.exists():
                trading_institution = trading_institution_list[0]
            else:
                trader_type = TraderType.objects.get(name=payload['trader_type'])
                status = TradingInstitutionStatus.objects.get(name='CREATED')
                trading_institution = TradingInstitution(trader_type=trader_type,
                                                         institution=institution, agent=agent, status=status)
                trading_institution.save()

            if 'supplier' in payload.keys():

                suppliers = [int(a) for a in payload['supplier'].split(',') if a]
                current_suppliers = trading_institution.supplier.values_list('pk', flat=True)

                remove_suppliers = list(set(current_suppliers).difference(suppliers))
                add_suppliers = list(set(suppliers).difference(current_suppliers))

                trading_institution.supplier.add(*TradingInstitution.objects.filter(institution__id__in=add_suppliers))
                trading_institution.supplier.remove(*TradingInstitution.objects.filter(
                    institution__id__in=remove_suppliers
                ))

            payload['trading_institution_id'] = trading_institution.id
            payload['trading_institution_name'] = trading_institution.institution.name

            payload['enrollment_type_id'] = trading_institution.trader_type.enrollment_type.id
            payload['response'] = 'Institution Captured'
            payload['response_status'] = '00'
        except Exception, e:
            payload['response_status'] = '96'
            lgr.info("Error on get trading institution: %s" % e)
        return payload


class Trade(System):
    pass


class Registrations(System):
    pass

