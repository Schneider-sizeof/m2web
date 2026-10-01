from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import ContactForm
from apps.core.models import CompanyInfo

from apps.core.emails import send_inquiry_emails

def contact_view(request):
    company = CompanyInfo.get_instance()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            details = {
                'Entreprise': getattr(msg, 'company_name', '') or 'Particulier',
                'Sujet': msg.subject,
                'Message': msg.message,
            }
            send_inquiry_emails(
                inquiry_type=f"Message de Contact ({msg.subject})",
                details=details,
                user_email=msg.email,
                user_name=msg.name,
                user_phone=msg.phone
            )
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
