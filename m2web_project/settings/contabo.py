"""
Production settings for Contabo VPS deployment.
All secrets are read from environment variables — never hardcoded.
"""
from .base import *
import os

# ─── Core ────────────────────────────────────────────────────
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']  # will crash if missing (intentional)

ALLOWED_HOSTS = [
    'M2webmaroc.com',
    'www.M2webmaroc.com',
    'm2webmaroc.com',
    'www.m2webmaroc.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://M2webmaroc.com',
    'https://www.M2webmaroc.com',
    'https://m2webmaroc.com',
    'https://www.m2webmaroc.com',
]

# ─── Database (PostgreSQL) ───────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'm2web_db'),
        'USER': os.getenv('DB_USER', 'm2web_user'),
        'PASSWORD': os.environ['DB_PASSWORD'],  # required
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# ─── Email (Gmail SMTP) ─────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# ─── Static & Media (WhiteNoise + Nginx) ─────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

CONTENT_SECURITY_POLICY = None

# ─── Security hardening ─────────────────────────────────────
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000       # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ─── Axes (behind Nginx reverse proxy) ──────────────────────
AXES_IP_GETTER = 'axes.helpers.get_client_ip'

# ─── Logging ─────────────────────────────────────────────────
LOGGING['handlers']['file']['filename'] = '/var/log/m2web/django.log'
