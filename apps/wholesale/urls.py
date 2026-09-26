from django.urls import path
from . import views

app_name = 'wholesale'
urlpatterns = [
    path('', views.wholesale_view, name='inquiry'),
    path('succes/', views.wholesale_success, name='success'),
]
