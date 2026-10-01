from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if not EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CSP in report-only mode for dev
CONTENT_SECURITY_POLICY_REPORT_ONLY = CONTENT_SECURITY_POLICY
CONTENT_SECURITY_POLICY = None

