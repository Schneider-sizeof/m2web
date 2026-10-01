"""
M2web Maroc - Centralized Email Dispatcher
Handles spam-safe admin notifications and customer confirmation emails for all inquiry types.
"""
import logging
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from apps.core.models import CompanyInfo

logger = logging.getLogger(__name__)

ADMIN_EMAIL = 'm2webmaroc23@gmail.com'

def get_admin_recipient():
    try:
        company = CompanyInfo.objects.first()
        if company and company.email and '@' in company.email:
            return company.email
    except Exception:
        pass
    return ADMIN_EMAIL

def send_inquiry_emails(inquiry_type, details, user_email, user_name, user_phone=None):
    """
    Sends two emails:
    1. Admin Notification -> sent to m2webmaroc23@gmail.com with all submitted details and Reply-To = user_email
    2. User Confirmation  -> sent to user_email confirming receipt with company contact info
    """
    admin_recipient = get_admin_recipient()
    from_email = f"M2web Maroc <{admin_recipient}>"

    phone_display = user_phone or details.get('Téléphone') or details.get('Phone') or ''

    # ==========================================
    # 1. ADMIN NOTIFICATION EMAIL
    # ==========================================
    admin_subject = f"Nouveau contact : {inquiry_type} - {user_name}"
    
    # Plain text version
    admin_text = f"""M2WEB MAROC - NOUVELLE DEMANDE DE CONTACT
==================================================

Type de demande : {inquiry_type}
Nom / Contact   : {user_name}
Email           : {user_email}
Téléphone       : {phone_display}

DETAILS TRANSFERRED :
"""
    for key, val in details.items():
        admin_text += f"- {key} : {val}\n"

    admin_text += f"""
==================================================
Pour repondre directement a ce prospect, repondez a cet email.
"""

    details_html_rows = "".join(
        f'<tr><td style="padding: 7px 12px; font-weight: bold; color: #2D1B3D; border-bottom: 1px solid #eee; width: 35%;">{k}</td>'
        f'<td style="padding: 7px 12px; color: #333; border-bottom: 1px solid #eee;">{v}</td></tr>'
        for k, v in details.items()
    )

    admin_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: Arial, Helvetica, sans-serif; background-color: #f6f7f9; margin: 0; padding: 20px; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; background: #ffffff; border: 1px solid #dddddd; border-radius: 6px; padding: 24px;">
        <div style="border-bottom: 2px solid #2D1B3D; padding-bottom: 12px; margin-bottom: 20px;">
            <h2 style="color: #2D1B3D; margin: 0; font-size: 20px;">M2WEB MAROC</h2>
            <p style="color: #666; margin: 4px 0 0; font-size: 13px;">Notification de contact web : <strong>{inquiry_type}</strong></p>
        </div>
        
        <p style="font-size: 14px; margin-top: 0;">Une nouvelle demande a été soumise depuis le site web :</p>
        
        <table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 20px; background: #fafafa; border: 1px solid #eee;">
            <tr>
                <td style="padding: 7px 12px; font-weight: bold; color: #2D1B3D; border-bottom: 1px solid #eee; width: 35%;">Nom / Contact</td>
                <td style="padding: 7px 12px; color: #333; border-bottom: 1px solid #eee;"><strong>{user_name}</strong></td>
            </tr>
            <tr>
                <td style="padding: 7px 12px; font-weight: bold; color: #2D1B3D; border-bottom: 1px solid #eee;">Email</td>
                <td style="padding: 7px 12px; color: #333; border-bottom: 1px solid #eee;"><a href="mailto:{user_email}" style="color: #2D1B3D;">{user_email}</a></td>
            </tr>
            <tr>
                <td style="padding: 7px 12px; font-weight: bold; color: #2D1B3D; border-bottom: 1px solid #eee;">Téléphone</td>
                <td style="padding: 7px 12px; color: #333; border-bottom: 1px solid #eee;"><strong>{phone_display}</strong></td>
            </tr>
            {details_html_rows}
        </table>
        
        <p style="font-size: 13px; color: #555; margin-top: 20px;">
            Pour répondre directement à ce client, cliquez sur "Répondre" dans votre messagerie ou écrivez à <a href="mailto:{user_email}">{user_email}</a>.
        </p>
    </div>
</body>
</html>"""

    try:
        msg = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_text,
            from_email=from_email,
            to=[admin_recipient],
            reply_to=[user_email] if user_email else None
        )
        msg.attach_alternative(admin_html, "text/html")
        msg.send(fail_silently=False)
        logger.info(f"Admin notification email sent for {inquiry_type} to {admin_recipient}")
    except Exception as e:
        logger.error(f"Failed to send admin notification email: {e}")

    # ==========================================
    # 2. CUSTOMER CONFIRMATION EMAIL (Anti-Spam Optimized)
    # ==========================================
    if user_email and '@' in user_email:
        # Clean subject without special symbols or em-dashes
        user_subject = f"M2web Maroc - Réception de votre message ({inquiry_type})"

        user_text = f"""Bonjour {user_name},

Nous vous confirmons la bonne reception de votre message concernant : {inquiry_type}.

Notre equipe commerciale et technique a Fes etudie votre demande et reviendra vers vous rapidement.

Coordonnees transmises :
- Nom : {user_name}
- Email : {user_email}
- Telephone : {phone_display or 'Non renseigne'}

Pour toute question urgente :
- Telephone & WhatsApp : +212 6 61 76 14 89
- Telephone fixe : +212 5 35 94 02 71
- Email : {admin_recipient}
- Adresse : CN, 2 Rue Ibn Al Kayem, Fes 30000, Maroc

Merci de votre confiance,
L'equipe M2web Maroc
"""

        # Clean corporate HTML: No heavy dark backgrounds, no wa.me redirect links, no bright CTA buttons
        user_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: Arial, Helvetica, sans-serif; background-color: #f7f7f7; margin: 0; padding: 24px; color: #222222; line-height: 1.5;">
    <div style="max-width: 580px; margin: 0 auto; background: #ffffff; border: 1px solid #e0e0e0; border-radius: 6px; padding: 28px;">
        <div style="border-bottom: 2px solid #2D1B3D; padding-bottom: 12px; margin-bottom: 20px;">
            <div style="font-size: 20px; font-weight: bold; color: #2D1B3D; letter-spacing: 0.5px;">M2WEB MAROC</div>
            <div style="font-size: 12px; color: #666666; margin-top: 2px;">Solutions de Géolocalisation & Gestion de Flotte</div>
        </div>

        <p style="font-size: 15px; margin: 0 0 16px 0; color: #222222;">Bonjour <strong>{user_name}</strong>,</p>

        <p style="font-size: 14px; margin: 0 0 16px 0; color: #333333;">
            Nous vous confirmons la bonne réception de votre message concernant : <strong>{inquiry_type}</strong>.
        </p>

        <p style="font-size: 14px; margin: 0 0 20px 0; color: #333333;">
            Notre équipe commerciale et technique étudie votre projet et prendra contact avec vous dans les meilleurs délais pour vous apporter toutes les informations nécessaires.
        </p>

        <div style="background: #fbfbfb; border: 1px solid #ebebeb; border-radius: 4px; padding: 14px 16px; margin-bottom: 22px; font-size: 13px; color: #444444;">
            <div style="font-weight: bold; color: #2D1B3D; margin-bottom: 6px;">Besoin d'une réponse rapide ?</div>
            <div style="line-height: 1.6;">
                Téléphone & WhatsApp : <strong>+212 6 61 76 14 89</strong><br>
                Téléphone fixe : <strong>+212 5 35 94 02 71</strong><br>
                Email : <a href="mailto:{admin_recipient}" style="color: #2D1B3D;">{admin_recipient}</a><br>
                Bureau & Atelier : CN, 2 Rue Ibn Al Kayem, Fès 30000, Maroc
            </div>
        </div>

        <p style="font-size: 14px; margin: 0 0 4px 0; color: #333333;">Merci de votre confiance,</p>
        <p style="font-size: 14px; margin: 0; font-weight: bold; color: #2D1B3D;">L'équipe M2web Maroc</p>

        <div style="border-top: 1px solid #eeeeee; margin-top: 24px; padding-top: 14px; font-size: 11px; color: #888888; text-align: center;">
            Cet email est une confirmation automatique suite à votre demande sur notre site. Vous pouvez y répondre directement.
        </div>
    </div>
</body>
</html>"""

        try:
            # Transactional email headers to avoid spam classification
            headers = {
                'Auto-Submitted': 'auto-generated',
                'X-Auto-Response-Suppress': 'All',
            }
            user_msg = EmailMultiAlternatives(
                subject=user_subject,
                body=user_text,
                from_email=from_email,
                to=[user_email],
                reply_to=[admin_recipient],
                headers=headers
            )
            user_msg.attach_alternative(user_html, "text/html")
            user_msg.send(fail_silently=False)
            logger.info(f"Confirmation email sent to customer {user_email}")
        except Exception as e:
            logger.error(f"Failed to send confirmation email to customer: {e}")
