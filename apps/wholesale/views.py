import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import WholesaleInquiryForm, ResellerInquiryForm, PlatformInquiryForm
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
                            f'+212 6 61 76 14 89',
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

def reseller_view(request):
    company = CompanyInfo.get_instance()
    if request.method == 'POST':
        form = ResellerInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            try:
                send_mail(
                    subject=f'[M2web Revendeur] Nouvelle candidature de {inquiry.company_name}',
                    message=f'Nouvelle candidature revendeur:\n\n'
                            f'Entreprise: {inquiry.company_name}\n'
                            f'Contact: {inquiry.contact_person}\n'
                            f'Email: {inquiry.email}\n'
                            f'Téléphone: {inquiry.phone}\n'
                            f'Ville: {inquiry.city}\n'
                            f'Secteur: {inquiry.get_activity_type_display()}\n'
                            f'Volume estimé: {inquiry.get_expected_volume_display()}\n'
                            f'Expérience installation: {"Oui" if inquiry.has_installed_before else "Non"}\n'
                            f'Intéressé marque blanche: {"Oui" if inquiry.interested_in_whitelabel else "Non"}\n'
                            f'Message: {inquiry.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[company.email if company and company.email else 'm2web@m2web.com'],
                    fail_silently=True,
                )
                send_mail(
                    subject='M2web Maroc — Candidature Revendeur bien reçue',
                    message=f'Bonjour {inquiry.contact_person},\n\n'
                            f'Nous avons bien reçu votre candidature pour devenir revendeur M2web.\n'
                            f'Notre équipe commerciale analysera votre profil et vous contactera sous 48h.\n\n'
                            f'Cordialement,\nL\'équipe M2web Maroc\n'
                            f'+212 6 61 76 14 89',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[inquiry.email],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, _('Votre candidature a été envoyée avec succès. Nous vous contacterons sous 48h.'))
            return redirect('wholesale:success')
    else:
        form = ResellerInquiryForm()
    context = {
        'form': form,
        'company': company,
        'page_title': 'Devenir Revendeur',
    }
    return render(request, 'wholesale/reseller.html', context)

def platform_view(request):
    company = CompanyInfo.get_instance()
    if request.method == 'POST':
        form = PlatformInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            try:
                send_mail(
                    subject=f'[M2web Plateforme] Demande de {inquiry.company_name}',
                    message=f'Nouvelle demande plateforme GPS:\n\n'
                            f'Entreprise: {inquiry.company_name}\n'
                            f'Contact: {inquiry.contact_name}\n'
                            f'Email: {inquiry.email}\n'
                            f'Téléphone: {inquiry.phone}\n'
                            f'Ville: {inquiry.city}\n'
                            f'Formule: {inquiry.get_acquisition_mode_display()}\n'
                            f'Taille flotte: {inquiry.get_fleet_size_display()}\n'
                            f'Rapports avancés: {"Oui" if inquiry.needs_reports else "Non"}\n'
                            f'Contrôle carburant: {"Oui" if inquiry.needs_fuel_sensor else "Non"}\n'
                            f'Message: {inquiry.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[company.email if company and company.email else 'm2web@m2web.com'],
                    fail_silently=True,
                )
                send_mail(
                    subject='M2web Maroc — Demande Plateforme GPS bien reçue',
                    message=f'Bonjour {inquiry.contact_name},\n\n'
                            f'Nous avons bien reçu votre demande concernant notre plateforme GPS.\n'
                            f'Un expert technique vous contactera pour une démonstration personnalisée.\n\n'
                            f'Cordialement,\nL\'équipe M2web Maroc\n'
                            f'+212 6 61 76 14 89',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[inquiry.email],
                    fail_silently=True,
                )
            except Exception:
                pass
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
