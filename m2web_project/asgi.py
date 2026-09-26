import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.dev')

application = get_asgi_application()
