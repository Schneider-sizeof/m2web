from django.shortcuts import render, get_object_or_404
from .models import Service, Product

def services_list(request):
    services = Service.objects.all()
    products = Product.objects.filter(is_available=True)
    
    context = {
        'services': services,
        'products': products,
        'page_title': 'Nos Services & Produits',
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    
    context = {
        'service': service,
        'page_title': service.title,
    }
    return render(request, 'services/service_detail.html', context)
