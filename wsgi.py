import os, prctl

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
prctl.set_name("govtrack-" + os.environ["NAME"])

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
