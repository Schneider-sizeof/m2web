from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import ContactForm
from apps.core.models import CompanyInfo

def contact_view(request):
    company = CompanyInfo.get_instance()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            try:
                # Notification to company
                send_mail(
                    subject=f'[M2web Contact] {msg.subject}',
                    message=f'Nouveau message de contact:\n\n'
                            f'Nom: {msg.name}\n'
                            f'Email: {msg.email}\n'
                            f'Téléphone: {msg.phone}\n'
                            f'Sujet: {msg.subject}\n\n'
                            f'Message:\n{msg.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[company.email if company and company.email else 'm2web@m2web.com'],
                    fail_silently=True,
                )
                # Confirmation to sender
                send_mail(
                    subject='M2web Maroc — Message bien reçu',
                    message=f'Bonjour {msg.name},\n\n'
                            f'Nous avons bien reçu votre message et nous vous répondrons dans les plus brefs délais.\n\n'
                            f'Cordialement,\nL\'équipe M2web Maroc\n'
                            f'+212 6 62 24 49 39',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[msg.email],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, _('Votre message a été envoyé avec succès. Nous vous répondrons rapidement.'))
            return redirect('contact:success')
    else:
        form = ContactForm()
    context = {
        'form': form,
        'company': company,
        'page_title': 'Contact',
    }
    return render(request, 'contact/contact.html', context)

def contact_success(request):
    return render(request, 'contact/contact_success.html', {
        'company': CompanyInfo.get_instance(),
        'page_title': 'Message Envoyé',
    })
