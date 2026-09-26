from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.i18n import set_language
from django.views.generic import RedirectView

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
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
