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
    company = CompanyInfo.get_instance()
    if company and company.email and '@' in company.email:
        return company.email
    return ADMIN_EMAIL

def send_inquiry_emails(inquiry_type, details, user_email, user_name, user_phone=None):
    """
    Sends two emails:
    1. Admin Notification -> sent to m2webmaroc23@gmail.com with all submitted details and Reply-To = user_email
    2. User Confirmation  -> sent to user_email confirming receipt with company contact info
    """
    company = CompanyInfo.get_instance()
    admin_recipient = get_admin_recipient()
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None) or f"M2web Maroc <{admin_recipient}>"

    phone_display = user_phone or details.get('Téléphone') or details.get('Phone') or ''

    # ==========================================
    # 1. ADMIN NOTIFICATION EMAIL
    # ==========================================
    admin_subject = f"[M2WEB NOUVEAU CONTACT] {inquiry_type} - {user_name}"
    
    # Plain text version
    admin_text = f"""==================================================
M2WEB MAROC — NOUVELLE DEMANDE DE CONTACT
==================================================

Type de demande : {inquiry_type}
Date            : Notification instantanée site web

--- INFORMATIONS DU CONTACT ---
Nom / Responsable : {user_name}
Email             : {user_email}
Téléphone         : {phone_display}

--- DÉTAILS DE LA DEMANDE ---
"""
    for key, val in details.items():
        admin_text += f"{key:<20} : {val}\n"

    admin_text += f"""
==================================================
Pour répondre directement à ce prospect, répondez à cet email.
==================================================
"""

    # Clean text-based HTML version (no external images/trackers to prevent spam filters)
    details_html_rows = "".join(
        f'<tr><td style="padding: 8px 12px; font-weight: bold; color: #1E1028; border-bottom: 1px solid #f0f0f0; width: 35%;">{k}</td>'
        f'<td style="padding: 8px 12px; color: #444; border-bottom: 1px solid #f0f0f0;">{v}</td></tr>'
        for k, v in details.items()
    )

    admin_html = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: Arial, sans-serif; background-color: #f8f9fa; margin: 0; padding: 20px; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 8px; border: 1px solid #e5e5e5; overflow: hidden;">
        <div style="background: #1E1028; padding: 20px; text-align: center; border-bottom: 3px solid #F5A623;">
            <h2 style="color: #ffffff; margin: 0; font-size: 20px; letter-spacing: 1px;">M2WEB MAROC</h2>
            <p style="color: #F5A623; margin: 4px 0 0; font-size: 13px; font-weight: bold; text-transform: uppercase;">Nouvelle Demande : {inquiry_type}</p>
        </div>
        <div style="padding: 24px;">
            <p style="font-size: 15px; margin-top: 0;">Une nouvelle demande a été soumise sur votre site web <strong>m2web.ma</strong> :</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 20px; background: #fafafa; border-radius: 6px;">
                <tr>
                    <td style="padding: 8px 12px; font-weight: bold; color: #1E1028; border-bottom: 1px solid #f0f0f0;">Nom / Contact</td>
                    <td style="padding: 8px 12px; color: #444; border-bottom: 1px solid #f0f0f0;"><strong>{user_name}</strong></td>
                </tr>
                <tr>
                    <td style="padding: 8px 12px; font-weight: bold; color: #1E1028; border-bottom: 1px solid #f0f0f0;">Email</td>
                    <td style="padding: 8px 12px; color: #444; border-bottom: 1px solid #f0f0f0;"><a href="mailto:{user_email}" style="color: #1E1028;">{user_email}</a></td>
                </tr>
                <tr>
                    <td style="padding: 8px 12px; font-weight: bold; color: #1E1028; border-bottom: 1px solid #f0f0f0;">Téléphone</td>
                    <td style="padding: 8px 12px; color: #444; border-bottom: 1px solid #f0f0f0;"><a href="tel:{phone_display}" style="color: #1E1028; font-weight: bold;">{phone_display}</a></td>
                </tr>
                {details_html_rows}
            </table>
            <div style="text-align: center; margin-top: 25px;">
                <a href="mailto:{user_email}" style="display: inline-block; background: #F5A623; color: #1E1028; font-weight: bold; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-size: 14px;">
                    Répondre à {user_name}
                </a>
            </div>
        </div>
        <div style="background: #f4f4f4; padding: 14px; text-align: center; font-size: 12px; color: #777; border-top: 1px solid #eaeaea;">
            M2web Maroc — Siège : CN, 2 Rue Ibn Al Kayem, Fès — Tél : +212 6 61 76 14 89 / +212 5 35 94 02 71
        </div>
    </div>
</body>
</html>
"""

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
    # 2. CUSTOMER CONFIRMATION EMAIL
    # ==========================================
    if user_email and '@' in user_email:
        user_subject = "Confirmation : Votre demande a bien été reçue — M2web Maroc"
        
        user_text = f"""Bonjour {user_name},

Nous avons bien reçu votre demande concernant nos solutions de géolocalisation et télématique M2web Maroc.

Notre équipe commerciale et technique examine votre demande et vous contactera dans les plus brefs délais (sous 24h ouvrées).

--- Récapitulatif de votre demande ---
Type    : {inquiry_type}
Contact : {user_name}
Email   : {user_email}

Si vous avez une question urgente ou souhaitez échanger immédiatement avec un conseiller technique :
- Téléphone direct / WhatsApp : +212 6 61 76 14 89
- Téléphone fixe : +212 5 35 94 02 71
- Adresse Siège : CN, 2 Rue Ibn Al Kayem, Fès, Maroc

Merci de votre confiance,
L'équipe M2web Maroc
https://m2web.ma
"""

        user_html = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: Arial, sans-serif; background-color: #f8f9fa; margin: 0; padding: 20px; color: #333;">
    <div style="max-width: 580px; margin: 0 auto; background: #ffffff; border-radius: 8px; border: 1px solid #e5e5e5; overflow: hidden;">
        <div style="background: #1E1028; padding: 20px; text-align: center; border-bottom: 3px solid #F5A623;">
            <h2 style="color: #ffffff; margin: 0; font-size: 20px; letter-spacing: 1px;">M2WEB MAROC</h2>
            <p style="color: #F5A623; margin: 4px 0 0; font-size: 13px; font-weight: bold;">TÉLÉMATIQUE & GÉOLOCALISATION GPS</p>
        </div>
        <div style="padding: 24px;">
            <h3 style="color: #1E1028; margin-top: 0; font-size: 18px;">Bonjour {user_name},</h3>
            <p style="font-size: 14px; line-height: 1.6; color: #444;">
                Nous vous confirmons la bonne réception de votre demande concernant : <strong>{inquiry_type}</strong>.
            </p>
            <p style="font-size: 14px; line-height: 1.6; color: #444;">
                Notre équipe commerciale et technique étudie votre projet et reviendra vers vous avec une réponse personnalisée sous <strong>24 heures ouvrées</strong>.
            </p>
            
            <div style="background: #fbfbfb; border-left: 4px solid #F5A623; padding: 14px; margin: 20px 0; border-radius: 4px; font-size: 13px;">
                <p style="margin: 0 0 6px; font-weight: bold; color: #1E1028;">Besoin d'une réponse immédiate ?</p>
                <p style="margin: 0; color: #555; line-height: 1.5;">
                    Direct & WhatsApp : <strong>+212 6 61 76 14 89</strong><br>
                    Téléphone fixe : <strong>+212 5 35 94 02 71</strong><br>
                    Siège & Showroom : <strong>CN, 2 Rue Ibn Al Kayem, Fès</strong>
                </p>
            </div>
            
            <div style="text-align: center; margin-top: 25px;">
                <a href="https://wa.me/212661761489" style="display: inline-block; background: #25D366; color: #ffffff; font-weight: bold; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-size: 13px;">
                    Contacter un expert sur WhatsApp
                </a>
            </div>
        </div>
        <div style="background: #f4f4f4; padding: 14px; text-align: center; font-size: 12px; color: #777; border-top: 1px solid #eaeaea;">
            © M2web Maroc — Tous droits réservés.
        </div>
    </div>
</body>
</html>
"""

        try:
            user_msg = EmailMultiAlternatives(
                subject=user_subject,
                body=user_text,
                from_email=from_email,
                to=[user_email],
                reply_to=[admin_recipient]
            )
            user_msg.attach_alternative(user_html, "text/html")
            user_msg.send(fail_silently=False)
            logger.info(f"Confirmation email sent to customer {user_email}")
        except Exception as e:
            logger.error(f"Failed to send confirmation email to customer: {e}")
