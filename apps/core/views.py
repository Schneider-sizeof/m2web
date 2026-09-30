from django.shortcuts import render
from .models import CompanyInfo, WhyChooseUsPillar, Testimonial, Partner, Promotion, MobileApp, AppFeature, AppScreenshot, AppPlan
from apps.services.models import Service, Product

def home_view(request):
    services = Service.objects.filter(is_featured=True)[:6]
    if not services.exists():
        services = Service.objects.all()[:6]

    products = Product.objects.filter(is_featured=True, is_available=True)[:6]
    if not products.exists():
        products = Product.objects.filter(is_available=True)[:6]

    pillars = WhyChooseUsPillar.objects.filter(is_active=True).order_by('order')
    promotions = Promotion.objects.filter(is_active=True, is_featured=True)[:3]

    context = {
        'company': CompanyInfo.get_instance(),
        'services': services,
        'products': products,
        'pillars': pillars,
        'promotions': promotions,
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

def promotions_view(request):
    promotions = Promotion.objects.filter(is_active=True)
    context = {
        'promotions': promotions,
        'company': CompanyInfo.get_instance(),
        'page_title': 'Promotions & Offres',
    }
    return render(request, 'core/promotions.html', context)

def mobile_app_view(request):
    app_info = MobileApp.get_instance()
    features = AppFeature.objects.filter(is_active=True)
    screenshots = AppScreenshot.objects.filter(is_active=True)
    plans = AppPlan.objects.filter(is_active=True)
    company = CompanyInfo.get_instance()
    context = {
        'app': app_info,
        'features': features,
        'screenshots': screenshots,
        'plans': plans,
        'company': company,
        'page_title': 'Application Mobile GPS',
    }
    return render(request, 'core/mobile_app.html', context)
