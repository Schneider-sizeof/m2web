from django.shortcuts import render
from .models import CompanyInfo, WhyChooseUsPillar, Testimonial, Partner
from apps.services.models import Service, Product

def home_view(request):
    services = Service.objects.filter(is_featured=True)[:6]
    if not services.exists():
        services = Service.objects.all()[:6]

    products = Product.objects.filter(is_featured=True, is_available=True)[:6]
    if not products.exists():
        products = Product.objects.filter(is_available=True)[:6]

    pillars = WhyChooseUsPillar.objects.filter(is_active=True).order_by('order')

    context = {
        'company': CompanyInfo.get_instance(),
        'services': services,
        'products': products,
        'pillars': pillars,
        'testimonials': Testimonial.objects.filter(is_active=True),
        'partners': Partner.objects.filter(is_active=True),
        'page_title': 'Accueil',
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    context = {
        'company': CompanyInfo.get_instance(),
        'page_title': 'À Propos',
    }
    return render(request, 'core/about.html', context)
