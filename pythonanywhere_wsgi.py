"""
PythonAnywhere WSGI Configuration File for M2web Maroc
======================================================
Copy and paste this configuration into your PythonAnywhere WSGI file:
Path: /var/www/<your_username>_pythonanywhere_com_wsgi.py
"""

import os
import sys

# 1. Update this with your PythonAnywhere username
username = 'YOUR_PYTHONANYWHERE_USERNAME'
project_home = f'/home/{username}/m2web'

# 2. Add project directory to sys.path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 3. Specify PythonAnywhere production settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'm2web_project.settings.pythonanywhere'

# 4. Initialize Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
