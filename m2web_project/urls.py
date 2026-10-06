from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.i18n import set_language
from django.views.generic import RedirectView
from django.contrib.admin import AdminSite
from django_otp import user_has_device
from django_otp.admin import OTPAdminSite, OTPAdminAuthenticationForm


class FlexibleOTPAdminAuthenticationForm(OTPAdminAuthenticationForm):
    """
    Authentication form that enforces OTP if and only if the user has
    at least one registered OTP device. Users without devices (e.g. freshly created superusers)
    can authenticate with their password to access the admin panel and configure 2FA.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'otp_token' in self.fields:
            self.fields['otp_token'].widget.attrs.update({
                'placeholder': 'Jeton OTP (laisser vide si 2FA non configuré)',
                'autocomplete': 'off',
            })

    def clean(self):
        self.cleaned_data = super(OTPAdminAuthenticationForm, self).clean()
        user = self.get_user()
        if user and user_has_device(user):
            self.clean_otp(user)
        return self.cleaned_data


class FlexibleOTPAdminSite(OTPAdminSite):
    """
    OTPAdminSite that allows access to staff/superusers who do not yet have an OTP device configured.
    Once a device is added, 2FA is strictly enforced.
    """
    login_form = FlexibleOTPAdminAuthenticationForm

    def has_permission(self, request):
        if not AdminSite.has_permission(self, request):
            return False
        try:
            if user_has_device(request.user):
                return getattr(request.user, 'is_verified', lambda: True)()
        except Exception:
            pass
        return True


# Replace default admin with Flexible OTP-verified admin
admin.site.__class__ = FlexibleOTPAdminSite
admin.site.login_form = FlexibleOTPAdminAuthenticationForm

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('mobile-app/', RedirectView.as_view(pattern_name='core:mobile_app', permanent=False)),
    path('application-mobile/', RedirectView.as_view(pattern_name='core:mobile_app', permanent=False)),
    path('app/', RedirectView.as_view(pattern_name='core:mobile_app', permanent=False)),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('services/', include('apps.services.urls')),
    path('vente-en-gros/', include('apps.wholesale.urls')),
    path('wholesale/', RedirectView.as_view(pattern_name='wholesale:inquiry', permanent=False)),
    path('blog/', include('apps.blog.urls')),
    path('contact/', include('apps.contact.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
