import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import WholesaleInquiryForm
from apps.core.models import CompanyInfo
from apps.services.models import Product

def wholesale_view(request):
    products = Product.objects.filter(is_available=True)
    company = CompanyInfo.get_instance()
    
    if request.method == 'POST':
        form = WholesaleInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            try:
                send_mail(
                    subject=f'[M2web B2B] Nouvelle demande de {inquiry.company_name}',
                    message=f'Nouvelle demande B2B reçue:\n\n'
                            f'Entreprise: {inquiry.company_name}\n'
                            f'Contact: {inquiry.contact_person}\n'
                            f'Email: {inquiry.email}\n'
                            f'Téléphone: {inquiry.phone}\n'
                            f'Ville: {inquiry.city}\n'
                            f'Volume mensuel: {inquiry.get_monthly_volume_display()}\n'
                            f'Types demandés: {inquiry.hardware_types_needed}\n'
                            f'Message: {inquiry.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[company.email if company and company.email else 'm2web@m2web.com'],
                    fail_silently=True,
                )
                send_mail(
                    subject='M2web Maroc — Demande B2B bien reçue',
                    message=f'Bonjour {inquiry.contact_person},\n\n'
                            f'Nous avons bien reçu votre demande de devis en gros.\n'
                            f'Notre équipe commerciale vous contactera sous 24h.\n\n'
                            f'Cordialement,\nL\'équipe M2web Maroc\n'
                            f'+212 6 62 24 49 39',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[inquiry.email],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, _('Votre demande a été envoyée avec succès. Nous vous contacterons sous 24h.'))
            return redirect('wholesale:success')
    else:
        form = WholesaleInquiryForm()
    
    context = {
        'form': form,
        'products': products,
        'company': company,
        'page_title': 'Vente en Gros / B2B',
    }
    return render(request, 'wholesale/wholesale.html', context)

def wholesale_success(request):
    return render(request, 'wholesale/inquiry_success.html', {
        'company': CompanyInfo.get_instance(),
        'page_title': 'Demande Envoyée',
    })
