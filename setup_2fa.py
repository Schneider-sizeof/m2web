"""
M2web Maroc - 2FA TOTP Device Setup Tool
Run this script to configure Google Authenticator / Authy for Django Admin 2FA.

Usage:
    python setup_2fa.py [username]
    python setup_2fa.py admin
    python setup_2fa.py --verify admin 123456
    python setup_2fa.py --disable admin
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.dev')
django.setup()

from django.contrib.auth import get_user_model
from django_otp.plugins.otp_totp.models import TOTPDevice
from urllib.parse import parse_qs, urlparse
import qrcode

User = get_user_model()

def print_banner():
    print("=" * 60)
    print("      M2WEB MAROC — 2FA (TOTP) CONFIGURATION TOOL      ")
    print("=" * 60)

def setup_user_2fa(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"[ERROR] User '{username}' does not exist.")
        users = list(User.objects.values_list('username', flat=True))
        print(f"Available users: {', '.join(users)}")
        return

    # Delete existing devices to start fresh
    TOTPDevice.objects.filter(user=user).delete()

    # Create new confirmed device
    device = TOTPDevice.objects.create(
        user=user,
        name='default',
        confirmed=True,
        step=30,
        digits=6
    )

    config_url = device.config_url
    parsed = urlparse(config_url)
    params = parse_qs(parsed.query)
    secret = params.get('secret', [''])[0]

    # Format secret in readable 4-char chunks
    formatted_secret = ' '.join(secret[i:i+4] for i in range(0, len(secret), 4))

    print(f"\n[OK] 2FA TOTP Device created for user: '{username}'")
    print(f"\nSecret Key (Manual Entry):")
    print(f"  >>> {formatted_secret} <<<\n")
    print("How to configure in Google Authenticator / Microsoft Authenticator:")
    print("  1. Open Google Authenticator or Authy on your smartphone.")
    print("  2. Tap '+' -> 'Enter a setup key' (or scan QR code below).")
    print(f"  3. Account Name: M2web Admin ({username})")
    print(f"  4. Key: {secret}")
    print("  5. Type of key: Time-based\n")

    # Generate ASCII QR Code in terminal if supported
    try:
        qr = qrcode.QRCode(border=1)
        qr.add_data(config_url)
        qr.make(fit=True)
        print("Scan this QR Code in your Authenticator app:")
        print("-" * 50)
        qr.print_ascii(invert=True)
        print("-" * 50)
    except Exception:
        print("(ASCII QR rendering skipped on Windows console)")

    # Save PNG QR Code
    os.makedirs('media', exist_ok=True)
    qr_img = qrcode.make(config_url)
    qr_path = f"media/2fa_qr_{username}.png"
    qr_img.save(qr_path)
    print(f"\n[SUCCESS] QR Code image saved to: {qr_path}")
    print(f"Direct QR Image link: http://127.0.0.1:8000/media/2fa_qr_{username}.png")
    print(f"otpauth URI: {config_url}\n")
    print("Next step: Try logging into http://127.0.0.1:8000/fr/admin/ with your password and the 6-digit code.")

def verify_code(username, token):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"[ERROR] User '{username}' does not exist.")
        return

    device = TOTPDevice.objects.filter(user=user, confirmed=True).first()
    if not device:
        print(f"[ERROR] No active 2FA device found for user '{username}'.")
        return

    if device.verify_token(token):
        print(f"[SUCCESS] OTP token '{token}' is VALID for user '{username}'! 2FA is working properly.")
    else:
        print(f"[FAILED] OTP token '{token}' is INVALID. Check your phone's clock or regenerate the secret.")

def disable_2fa(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"[ERROR] User '{username}' does not exist.")
        return

    count, _ = TOTPDevice.objects.filter(user=user).delete()
    print(f"[OK] Disabled 2FA for user '{username}' (removed {count} device(s)).")

if __name__ == '__main__':
    print_banner()
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
        if arg1 == '--verify' and len(sys.argv) >= 4:
            verify_code(sys.argv[2], sys.argv[3])
        elif arg1 == '--disable' and len(sys.argv) >= 3:
            disable_2fa(sys.argv[2])
        else:
            setup_user_2fa(arg1)
    else:
        # Default to first superuser or 'admin'
        superusers = User.objects.filter(is_superuser=True)
        if superusers.exists():
            for su in superusers:
                setup_user_2fa(su.username)
        else:
            print("No superusers found in database.")
