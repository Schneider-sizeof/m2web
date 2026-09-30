from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('a-propos/', views.about_view, name='about'),
    path('promotions/', views.promotions_view, name='promotions'),
    path('application-mobile/', views.mobile_app_view, name='mobile_app'),
]
