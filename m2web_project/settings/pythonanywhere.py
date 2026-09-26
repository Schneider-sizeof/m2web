from .base import *
import os

# Set DEBUG to False by default for production, or True if specified in environment
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-m2web-maroc-pa-prod-key-2026-safe-9f7b1e8')

# Allow all PythonAnywhere domains, custom domains, and local test servers
ALLOWED_HOSTS = [
    '.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
    '*',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static and Media configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email backend (console by default for free tier accounts without outbound SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CSRF Trusted Origins for PythonAnywhere HTTPS
CSRF_TRUSTED_ORIGINS = [
    'https://*.pythonanywhere.com',
    'http://*.pythonanywhere.com',
]

# Axes reverse-proxy configuration (using standard Axes 8+ defaults)
AXES_IP_GETTER = 'axes.helpers.get_client_ip'

# CSP settings: allow standard Google Fonts, CDNs, Leaflet, Maps iframe
CONTENT_SECURITY_POLICY_REPORT_ONLY = CONTENT_SECURITY_POLICY
CONTENT_SECURITY_POLICY = None
