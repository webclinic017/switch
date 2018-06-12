import os
import datetime
import psycopg2

# Django settings for switch project.
#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import ConfigParser
from keyczar import keyczar

location = '/opt/kz'
crypter = keyczar.Crypter.Read(location)

cf = ConfigParser.ConfigParser()
cf.read('switch/conf/switch.properties')

#print cf._sections


conf_products = cf.get('INSTALLED_APPS','products')
products=conf_products.split(",")

conf_thirdparty = cf.get('INSTALLED_APPS','thirdparty')
thirdparty=conf_thirdparty.split(",")


dbengine = cf.get('DATABASES','default_dbengine')
dbname = cf.get('DATABASES','default_dbname')
dbuser = cf.get('DATABASES','default_dbuser')
dbuser = crypter.Decrypt(dbuser)
dbpassword = cf.get('DATABASES','default_dbpassword')
dbpassword = crypter.Decrypt(dbpassword)
dbhost = cf.get('DATABASES','default_dbhost')
dbport = cf.get('DATABASES','default_dbport')

smtphost = cf.get('SMTP','default_host')
smtpport = cf.get('SMTP','default_port')
smtptls_default = cf.get('SMTP','tls')
tls_default = {'True': True, 'False': False}
smtptls = tls_default[smtptls_default]

conf_hosts = cf.get('ALLOWED_HOSTS','hosts')
hosts = conf_hosts.split(",")

installed_apps = products+thirdparty
installed_apps = filter(None, installed_apps)

primary = (
    'primary.core.administration',
    'primary.core.api',
    'primary.core.upc',
    'primary.core.bridge',
	)

secondary = (
    'secondary.channels.vcs',
    'secondary.channels.iic',
    'secondary.channels.dsc',
    'secondary.channels.notify',
    'secondary.erp.distro',
    'secondary.erp.pos',
    'secondary.erp.ads',
    'secondary.erp.crm',
    'secondary.erp.survey',
    'secondary.erp.loyalty',
    'secondary.finance.vbs',
    'secondary.finance.crc',
    'secondary.finance.paygate',
	)

installed_apps = primary + secondary + tuple(installed_apps)


#import djcelery
#djcelery.setup_loader()

CELERY_TASK_PROTOCOL = 1
delivery_mode = 1
result_backend = 'django-db'
#result_backend = "amqp"
CELERY_AMQP_TASK_RESULT_EXPIRES = 1000 
#beat_scheduler = 'djcelery.schedulers.DatabaseScheduler'
beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
task_serializer = 'json'
result_serializer = 'json'
#accept_content = ['pickle']
accept_content = ['pickle', 'json', 'msgpack', 'yaml','application/x-python-serialize']
timezone='Africa/Nairobi'
CELERY_enable_utc=True
result_expires=3600
task_soft_time_limit = 60
#task_acks_late = True
task_acks_late = False
worker_prefetch_multiplier = 128
worker_disable_rate_limits = True
broker_pool_limit = 100
broker_heartbeat = 10 
broker_heartbeat_checkrate = 2.0
#broker_transport_options = {'confirm_publish': True}
#broker_pool_limit = None
#broker_url = "amqp://Super%40User:%40wys1WYG@localhost:5672//"
#broker_url = "librabbitmq://Super%40User:%40wys1WYG@localhost:5672//"

#broker_url = "librabbitmq://guest:guest@localhost:5672//"
#broker_url = "librabbitmq://guest:guest@zabbix:56720//"
#broker_url = "pyamqp://guest:guest@localhost:5672//"
#broker_url = ["librabbitmq://guest:guest@localhost:5672//","librabbitmq://guest:guest@zabbix:56720//"]
broker_url = "librabbitmq://guest:guest@localhost:5672//"

#TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DEBUG = True
#TEMPLATE_DEBUG = DEBUG #Deprecated 1.8

GEOIP_PATH = '/usr/share/GeoIP'

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'interintel.helpdesk@gmail.com'
#EMAIL_HOST_PASSWORD = 'User@InterIntel1234'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = smtphost
#EMAIL_PORT = 25
EMAIL_PORT = smtpport
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = smtptls
#EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'InterIntel <noreply@interintel.co.ke>'

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

ADMINS = (
     ('InterIntel Support', 'support@interintel.co.ke'),
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Switch Administrator',


}

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': dbengine, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': dbname,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': dbuser,
        'PASSWORD': dbpassword,
        'HOST': dbhost,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': dbport,                      # Set to empty string for default.
	#'CONN_MAX_AGE': '600',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = hosts

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Nairobi'
#TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media').replace('\\','/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
#STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hj-99b$$ap_z4zmd=0z$ol5691_xe+$xn!n5horl*jfymibrrc'

ROOT_URLCONF = 'switch.urls'

WSGI_APPLICATION = 'switch.wsgi.application'

'''
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_extensions',
    'django_celery_results',
    'django_celery_beat',
    'primary.core.administration',
    'primary.core.api',
    'primary.core.upc',
    'primary.core.bridge',
)
'''
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_extensions',
    'django_celery_results',
    'django_celery_beat',
) +  installed_apps

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


'''
#REQUEST CONTEXT PROCESSOR
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#VENV_ROOT = os.path.join(os.path.dirname(__file__), 'logs').replace('\\','/')
VENV_ROOT = '/opt/logs/switch/'

print VENV_ROOT

LOGFILE='info.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s-%(name)s %(module)s %(process)d %(thread)d-(%(threadName)-2s) %(levelname)s-%(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'special': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        },
        'file_actions': {                # define and name a handler
            'level': 'DEBUG',
            'class': 'logging.FileHandler', # set the logging class to log to a file
            'formatter': 'verbose',         # define the formatter to associate
            'filename': os.path.join(VENV_ROOT, '', LOGFILE) # log file
        },     
        
    },

    'loggers': {
        'logview.usersaves': {               # define another logger
            'handlers': ['file_actions'],  # associate a different handler
            'level': 'INFO',                 # specify the logging level
            'propagate': True,
        }, 
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },

    }
}
#for app in installed_apps:
#	print app



for app in installed_apps:
	LOGGING['handlers'][app] = {
            'level' : 'INFO',
            'formatter' : 'verbose', # from the django doc example
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : os.path.join(VENV_ROOT, '', app+'.log'), # full path works
            'when' : 'midnight',
            'interval' : 1,
            'backupCount' : 7,
        }

	LOGGING['loggers'][app] = {
            'handlers': [app],
            'level': 'INFO',
        }

'''
print 'HANDLERS' 
for handle in LOGGING['handlers']:
	print handle, LOGGING['handlers'][handle]
print 'LOGGERS' 
for log in LOGGING['loggers']:
	print log, LOGGING['loggers'][log]
'''
