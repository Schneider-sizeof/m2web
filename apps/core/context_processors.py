from django.conf import settings
from .models import CompanyInfo
from apps.services.models import Service

def company_context(request):
    """
    Globally injects company details, primary services, and security config into all template contexts.
    Allows header, footer, topbar, and widgets to dynamically update from the admin.
    """
    try:
        company = CompanyInfo.get_instance()
    except Exception:
        company = None

    try:
        nav_services = Service.objects.all().order_by('order')[:6]
    except Exception:
        nav_services = []

    return {
        'company': company,
        'nav_services': nav_services,
        'license_gist_url': getattr(settings, 'LICENSE_GIST_URL', ''),
    }
