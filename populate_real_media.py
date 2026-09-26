#!/usr/bin/env python
"""Link downloaded images to Django models and create partner logos."""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.dev')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import django
django.setup()

import urllib.request
from apps.services.models import Service, Product
from apps.blog.models import BlogPost
from apps.core.models import Testimonial, Partner

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

def download_file_if_missing(url, target_path):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
        print(f"Already exists: {os.path.basename(target_path)}")
        return
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=15) as response, open(target_path, 'wb') as out_file:
        out_file.write(response.read())
    print(f"Downloaded: {os.path.basename(target_path)} ({os.path.getsize(target_path)} bytes)")

def create_partner_svg(name, subtitle, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 60" width="240" height="60">
  <rect width="100%" height="100%" fill="transparent"/>
  <g transform="translate(10, 8)">
    <rect width="44" height="44" rx="10" fill="#1E1028"/>
    <circle cx="22" cy="22" r="14" fill="#F5A623" opacity="0.25"/>
    <path d="M14 22h16M22 14v16" stroke="#F5A623" stroke-width="3" stroke-linecap="round"/>
  </g>
  <text x="64" y="27" font-family="'Outfit', 'Inter', sans-serif" font-size="14" font-weight="800" fill="#1E1028" letter-spacing="0.5">{name}</text>
  <text x="64" y="43" font-family="'Inter', sans-serif" font-size="9" font-weight="600" fill="#888888" letter-spacing="1">{subtitle}</text>
</svg>'''
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created SVG partner logo: {os.path.basename(target_path)}")

def main():
    print("--- 1. Checking Static Graphics ---")
    static_images = {
        os.path.join(STATIC_ROOT, 'images', 'hero-fleet.jpg'): 'https://images.unsplash.com/photo-1519003722824-194d4455a60c?auto=format&fit=crop&w=1200&q=80',
        os.path.join(STATIC_ROOT, 'images', 'hero-dashboard.png'): 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1000&q=80',
        os.path.join(STATIC_ROOT, 'images', 'about-team.jpg'): 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1000&q=80',
        os.path.join(STATIC_ROOT, 'images', 'fleet-telematics.jpg'): 'https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=1000&q=80',
    }
    for path, url in static_images.items():
        try:
            download_file_if_missing(url, path)
        except Exception as e:
            print(f"Failed {path}: {e}")

    print("\n--- 2. Updating Services ---")
    services_media = {
        'gestion-flotte-temps-reel': 'https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=800&q=80',
        'controle-carburant-eco-conduite': 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=800&q=80',
        'securite-coupure-moteur': 'https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=800&q=80',
        'telematique-chaine-froid': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80',
        'installation-support-technique': 'https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=800&q=80',
    }
    for slug, url in services_media.items():
        local_filename = f"{slug}.jpg"
        target_path = os.path.join(MEDIA_ROOT, 'services', local_filename)
        try:
            download_file_if_missing(url, target_path)
            svc = Service.objects.filter(slug=slug).first()
            if svc:
                svc.image = f'services/{local_filename}'
                svc.save()
                print(f"[OK] Linked Service: {svc.title}")
        except Exception as e:
            print(f"Error for service {slug}: {e}")

    print("\n--- 3. Updating Products ---")
    products_media = {
        'traceur-gps-4g-obd-ii': 'https://images.unsplash.com/photo-1580674684081-7617fbf3d745?auto=format&fit=crop&w=800&q=80',
        'traceur-gps-4g-filaire': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80',
        'traceur-gps-magnetique': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=800&q=80',
        'traceur-personnel-asset': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=800&q=80',
        'sonde-carburant-capacitive': 'https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&w=800&q=80',
        'capteur-temperature': 'https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?auto=format&fit=crop&w=800&q=80',
    }
    for slug, url in products_media.items():
        local_filename = f"{slug}.jpg"
        target_path = os.path.join(MEDIA_ROOT, 'products', local_filename)
        try:
            download_file_if_missing(url, target_path)
            prod = Product.objects.filter(slug=slug).first()
            if prod:
                prod.image = f'products/{local_filename}'
                prod.save()
                print(f"[OK] Linked Product: {prod.name}")
        except Exception as e:
            print(f"Error for product {slug}: {e}")

    print("\n--- 4. Updating Blog Posts ---")
    blog_media = {
        'choisir-meilleur-traceur-gps-maroc': 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=900&q=80',
        'optimiser-couts-carburant-flotte': 'https://images.unsplash.com/photo-1506015391300-4802dc74de2e?auto=format&fit=crop&w=900&q=80',
    }
    for slug, url in blog_media.items():
        local_filename = f"{slug}.jpg"
        target_path = os.path.join(MEDIA_ROOT, 'blog', local_filename)
        try:
            download_file_if_missing(url, target_path)
            post = BlogPost.objects.filter(slug=slug).first()
            if post:
                post.image = f'blog/{local_filename}'
                post.save()
                print(f"[OK] Linked Blog: {post.title}")
        except Exception as e:
            print(f"Error for blog {slug}: {e}")

    print("\n--- 5. Updating Testimonials ---")
    testimonials_photos = {
        'Ahmed Benali': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80',
        'Fatima Zahra El Amrani': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80',
        'Karim Tazi': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80',
        'Youssef Alaoui': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80',
    }
    for name, url in testimonials_photos.items():
        clean_name = name.lower().replace(' ', '_')
        local_filename = f"{clean_name}.jpg"
        target_path = os.path.join(MEDIA_ROOT, 'testimonials', local_filename)
        try:
            download_file_if_missing(url, target_path)
            t = Testimonial.objects.filter(client_name=name).first()
            if t:
                t.photo = f'testimonials/{local_filename}'
                t.save()
                print(f"[OK] Linked Testimonial: {t.client_name}")
        except Exception as e:
            print(f"Error for testimonial {name}: {e}")

    print("\n--- 6. Creating Partner Logos ---")
    partners_list = [
        ('Transport Atlas', 'LOGISTIQUE & TRANSPORT', 'partner_1.svg'),
        ('Livraison Express Maroc', 'MESSAGERIE NATIONALE', 'partner_2.svg'),
        ('Auto Location Fès', 'LOCATION DE VÉHICULES', 'partner_3.svg'),
        ('Frigorifique du Nord', 'CHAÎNE DU FROID', 'partner_4.svg'),
    ]
    for name, sub, filename in partners_list:
        target_path = os.path.join(MEDIA_ROOT, 'partners', filename)
        create_partner_svg(name, sub, target_path)
        p = Partner.objects.filter(name=name).first()
        if p:
            p.logo = f'partners/{filename}'
            p.save()
            print(f"[OK] Linked Partner Logo: {p.name}")

    print("\nAll media populated successfully!")

if __name__ == '__main__':
    main()
