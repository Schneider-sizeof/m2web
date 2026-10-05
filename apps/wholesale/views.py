import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import WholesaleInquiryForm, ResellerInquiryForm, PlatformInquiryForm
from apps.core.models import CompanyInfo
from apps.services.models import Product
from apps.core.emails import send_inquiry_emails

def wholesale_view(request):
    products = Product.objects.filter(is_available=True)
    company = CompanyInfo.get_instance()
    
    if request.method == 'POST':
        form = WholesaleInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            details = {
                'Entreprise': inquiry.company_name,
                'Ville': inquiry.city,
                'Volume mensuel': inquiry.get_monthly_volume_display(),
                'Types demandés': inquiry.hardware_types_needed,
                'Message': inquiry.message or 'N/A',
            }
            send_inquiry_emails(
                inquiry_type="Demande de Devis Vente en Gros / B2B",
                details=details,
                user_email=inquiry.email,
                user_name=inquiry.contact_person,
                user_phone=inquiry.phone
            )
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

def reseller_view(request):
    company = CompanyInfo.get_instance()
    if request.method == 'POST':
        form = ResellerInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            details = {
                'Entreprise / Atelier': inquiry.company_name,
                'Ville d\'activité': inquiry.city,
                'Secteur': inquiry.get_activity_type_display(),
                'Volume estimé': inquiry.get_expected_volume_display(),
                'Expérience installation': "Oui" if inquiry.has_installed_before else "Non",
                'Intéressé marque blanche': "Oui" if inquiry.interested_in_whitelabel else "Non",
                'Message': inquiry.message or 'N/A',
            }
            send_inquiry_emails(
                inquiry_type="Candidature Programme Revendeur M2web",
                details=details,
                user_email=inquiry.email,
                user_name=inquiry.contact_person,
                user_phone=inquiry.phone
            )
            messages.success(request, _('Votre candidature a été envoyée avec succès. Nous vous contacterons sous 48h.'))
            return redirect('wholesale:success')
    else:
        form = ResellerInquiryForm()
        
    from .models import ResellerTier
    tiers = ResellerTier.objects.filter(is_active=True)
    
    context = {
        'form': form,
        'company': company,
        'page_title': 'Devenir Revendeur',
        'tiers': tiers,
    }
    return render(request, 'wholesale/reseller.html', context)

def platform_view(request):
    company = CompanyInfo.get_instance()
    if request.method == 'POST':
        form = PlatformInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            details = {
                'Entreprise / Organisation': inquiry.company_name,
                'Ville': inquiry.city,
                'Formule d\'acquisition': inquiry.get_acquisition_mode_display(),
                'Taille de la flotte': inquiry.get_fleet_size_display(),
                'Besoin rapports avancés': "Oui" if inquiry.needs_reports else "Non",
                'Besoin contrôle carburant': "Oui" if inquiry.needs_fuel_sensor else "Non",
                'Message / Détails': inquiry.message or 'N/A',
            }
            send_inquiry_emails(
                inquiry_type="Demande Plateforme & Serveur GPS M2web",
                details=details,
                user_email=inquiry.email,
                user_name=inquiry.contact_name,
                user_phone=inquiry.phone
            )
            messages.success(request, _('Votre demande a été envoyée avec succès. Un expert vous contactera prochainement.'))
            return redirect('wholesale:success')
    else:
        form = PlatformInquiryForm()
    context = {
        'form': form,
        'company': company,
        'page_title': 'Plateforme & Serveur GPS',
    }
    return render(request, 'wholesale/platform.html', context)
