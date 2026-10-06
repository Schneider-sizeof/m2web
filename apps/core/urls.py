from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('a-propos/', views.about_view, name='about'),
    path('about/', RedirectView.as_view(pattern_name='core:about', permanent=False)),
    path('promotions/', views.promotions_view, name='promotions'),
    path('application-mobile/', views.mobile_app_view, name='mobile_app'),
    path('mobile-app/', RedirectView.as_view(pattern_name='core:mobile_app', permanent=False)),
    path('app/', RedirectView.as_view(pattern_name='core:mobile_app', permanent=False)),
]
