import os
import sys
import site


paths = [ '/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi/asservizi/',
          '/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi',
          '/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi/lib/python2.7/site-packages/',
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi')
sys.path.append('/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi/asservizi')

os.environ['DJANGO_SETTINGS_MODULE'] = 'asservizi.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
