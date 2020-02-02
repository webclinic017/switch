from django.contrib import admin
from secondary.finance.paygate.models import *
from django.forms.widgets import TextInput, Textarea
from django import forms

class FloatTypeAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','product_type_list','institution_list','service_list','gateway_list',\
			'payment_method_list','float_product_type',)
	list_filter = ('institution',)
admin.site.register(FloatType, FloatTypeAdmin)

class FloatChargeAdmin(admin.ModelAdmin):
	list_display = ('float_type','credit','expiry','min_amount','max_amount','charge_value','is_percentage','description',\
				'payment_method_list','product_type_list','institution_list','gateway_list')
admin.site.register(FloatCharge, FloatChargeAdmin)

class PollerFrequencyAdmin(admin.ModelAdmin):
	list_display = ('name','description','run_every',)
admin.site.register(PollerFrequency, PollerFrequencyAdmin)

class FloatAlertStatusAdmin(admin.ModelAdmin):
		list_display = ('name','description',)
admin.site.register(FloatAlertStatus, FloatAlertStatusAdmin)

class FloatAlertAdmin(admin.ModelAdmin):
		list_display = ('name','description','status','request','frequency','next_run','alert_below_value',\
				'alert_above_value','is_percentage','service','float_type','credit',\
				'institution','gateway')
admin.site.register(FloatAlert, FloatAlertAdmin)
 
class FloatManagerAdmin(admin.ModelAdmin):
	list_display = ('id','date_modified','date_created','ext_outbound_id','credit','request','float_amount',\
			'charge','balance_bf','expiry','float_type','gateway','institution','updated','float_alert','processed')
	list_filter = ('float_type','gateway','institution','credit','updated')
	search_fields = ('ext_outbound_id','id',)
admin.site.register(FloatManager, FloatManagerAdmin)
        
class AgentFloatManagerAdmin(admin.ModelAdmin):
        list_display = ('id','date_modified','date_created','ext_outbound_id','credit','float_amount',\
                        'charge','balance_bf','expiry','float_type','agent','gateway','updated',)
        list_filter = ('float_type','gateway','agent','credit','updated',)
        search_fields = ('ext_outbound_id','id',)
admin.site.register(AgentFloatManager, AgentFloatManagerAdmin)
 
class EndpointAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','request','url','account_id','username','password',)
admin.site.register(Endpoint, EndpointAdmin)

class RemittanceStatusAdmin(admin.ModelAdmin):
	list_display = ('name','description',)
admin.site.register(RemittanceStatus, RemittanceStatusAdmin)

class RemittanceAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','status','ext_service_id','ext_service_username',\
			'ext_service_password','ext_service_details',\
			'service','gateway_list',)
admin.site.register(Remittance, RemittanceAdmin)

class RemittanceProductAdmin(admin.ModelAdmin):
	list_display = ('id','name','description','remittance','ext_product_id','endpoint',\
			'product_type_list','service_list','realtime','show_message','fail_continues',\
			'payment_method_list','currency_list','institution',)
	list_filter = ('remittance','service','payment_method',)
admin.site.register(RemittanceProduct, RemittanceProductAdmin)

class InstitutionNotificationAdmin(admin.ModelAdmin):
	list_display = ('id','institution','remittance_product','description','request','url','account_id','username','password',)
admin.site.register(InstitutionNotification, InstitutionNotificationAdmin)

class InstitutionIncomingServiceAdmin(admin.ModelAdmin):
		list_display = ('id','service','description','keyword','product_item','gateway','details','process_order',)
admin.site.register(InstitutionIncomingService, InstitutionIncomingServiceAdmin)

class IncomingStateAdmin(admin.ModelAdmin):
		list_display = ('name','description','date_modified','date_created',)
admin.site.register(IncomingState, IncomingStateAdmin)

class IncomingAdmin(admin.ModelAdmin):
	list_display = ('id','remittance_product','reference','request','amount','charge','currency',\
			'response_status','message','ext_inbound_id','ext_first_name','ext_middle_name',\
			'ext_last_name','inst_notified','inst_num_tries',\
			'state','processed','institution_incoming_service',\
			'channel','institution','institution_notification',)
	search_fields = ('request','reference','message',)
admin.site.register(Incoming, IncomingAdmin)

class IncomingPollerStatusAdmin(admin.ModelAdmin):
		list_display = ('name','description','date_modified','date_created',)
admin.site.register(IncomingPollerStatus, IncomingPollerStatusAdmin)

class IncomingPollerAdmin(admin.ModelAdmin):
	list_display = ('name','description','request','remittance_product','remittance','frequency','service','next_run','status','gateway',)
admin.site.register(IncomingPoller, IncomingPollerAdmin)
 
class OutgoingStateAdmin(admin.ModelAdmin):
		list_display = ('name','description','date_modified','date_created',)
admin.site.register(OutgoingState, OutgoingStateAdmin)

class OutgoingAdmin(admin.ModelAdmin):
	list_display = ('id','remittance_product','reference','request','amount','charge','currency',\
			'scheduled_send','response_status','message','sends','ext_outbound_id',\
			'inst_notified','inst_num_tries','state','institution_notification','institution',)

	list_filter = ('remittance_product','currency','response_status','state',)
	search_fields = ('reference','request','ext_outbound_id','message',)
admin.site.register(Outgoing, OutgoingAdmin)

