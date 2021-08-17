import sys
import os

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/transport')

os.environ['DJANGO_SETTINGS_MODULE'] = 'transport.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
