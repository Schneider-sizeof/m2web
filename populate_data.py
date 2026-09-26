#!/usr/bin/env python
"""Populate M2web Maroc with initial seed data."""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.dev')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import django
django.setup()

from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.core.models import CompanyInfo, Testimonial, Partner
from apps.services.models import Service, Product
from apps.blog.models import Category, BlogPost
from django.core.files.base import ContentFile


def main():
    print("Starting data population...")

    User = get_user_model()

    # 0. Create admin superuser
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'm2web@m2web.com',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    if created:
        admin_user.set_password('M2web@Admin2024!')
        admin_user.save()
        print("Created admin user (password: M2web@Admin2024!)")
    else:
        print("Admin user already exists.")

    # 1. CompanyInfo singleton
    company = CompanyInfo.get_instance()
    company.company_name = 'M2web Maroc'
    company.tagline = 'Solutions Avancées de Géolocalisation & Gestion de Flotte par GPS à Fès et partout au Maroc'
    company.phone = '+212 6 62 24 49 39'
    company.email = 'm2web@m2web.com'
    company.whatsapp_number = '+212662244939'
    company.address = 'CN, 2 Rue Ibn Al Kayem'
    company.city = 'Fès'
    company.country = 'Maroc'
    company.google_maps_url = 'https://www.google.com/maps/place/M2web+Maroc/data=!4m2!3m1!1s0x0:0xe6a8036782c11407'
    company.google_maps_embed_url = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3306.0!2d-5.0!3d34.03!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xe6a8036782c11407!2sM2web%20Maroc!5e0!3m2!1sfr!2sma!4v1'
    company.operating_hours_weekday = '08:30 – 18:30'
    company.operating_hours_saturday = '08:30 – 13:30'
    company.operating_hours_sunday = 'Fermé'
    company.linkedin_url = 'https://linkedin.com/company/m2web-maroc'
    company.facebook_url = 'https://facebook.com/m2web.maroc'
    company.instagram_url = 'https://instagram.com/m2web_maroc'
    company.youtube_url = 'https://youtube.com/@m2webmaroc'
    company.meta_description = 'M2web Maroc — Fournisseur N°1 de solutions GPS et gestion de flotte à Fès. Traceurs GPS en gros et au détail, installation et support technique.'
    company.save()
    print("✓ Populated CompanyInfo.")

    # 2. Services
    services_data = [
        {
            'title': 'Gestion de Flotte en Temps Réel',
            'slug': 'gestion-flotte-temps-reel',
            'icon_class': 'bi bi-geo-alt-fill',
            'description': 'Suivi en temps réel de votre flotte avec historique des trajets, alertes de vitesse, géo-clôtures et accès via application mobile.',
            'order': 1,
        },
        {
            'title': 'Contrôle Carburant & Éco-Conduite',
            'slug': 'controle-carburant-eco-conduite',
            'icon_class': 'bi bi-fuel-pump',
            'description': 'Intégration de sondes de carburant pour auditer la consommation, détecter les vols de carburant et analyser le comportement de conduite.',
            'order': 2,
        },
        {
            'title': 'Sécurité & Coupure Moteur à Distance',
            'slug': 'securite-coupure-moteur',
            'icon_class': 'bi bi-shield-lock',
            'description': 'Protection antivol complète avec coupure du moteur à distance via SMS ou application mobile et alertes d\'immobilisation.',
            'order': 3,
        },
        {
            'title': 'Télématique & Chaîne du Froid',
            'slug': 'telematique-chaine-froid',
            'icon_class': 'bi bi-thermometer-snow',
            'description': 'Capteurs de température pour le transport frigorifique garantissant le respect de la chaîne du froid avec alertes en temps réel.',
            'order': 4,
        },
        {
            'title': 'Installation & Support Technique',
            'slug': 'installation-support-technique',
            'icon_class': 'bi bi-tools',
            'description': 'Notre atelier à Fès et nos techniciens itinérants assurent une installation professionnelle et un support technique rapide partout au Maroc.',
            'order': 5,
        },
    ]

    for data in services_data:
        slug = data.pop('slug')
        obj, created = Service.objects.update_or_create(slug=slug, defaults={**data, 'is_featured': True})
        status = "created" if created else "updated"
        print(f"  Service '{obj.title}' {status}.")
    print("✓ Populated Services.")

    # 3. Products
    products_data = [
        {
            'name': 'Traceur GPS 4G OBD-II',
            'slug': 'traceur-gps-4g-obd-ii',
            'category': 'obd',
            'description': 'Traceur GPS OBD-II plug & play avec connectivité 4G LTE, suivi en temps réel et lecture des données de diagnostic du véhicule.',
            'specifications': '4G LTE\nOBD-II Port\nGPS + GLONASS + BeiDou\nAccéléromètre intégré\nApplication mobile\nGéo-clôture',
            'price_range': '450 - 600 MAD',
            'order': 1,
        },
        {
            'name': 'Traceur GPS 4G Filaire (Hardwired)',
            'slug': 'traceur-gps-4g-filaire',
            'category': 'hardwired',
            'description': 'Traceur GPS professionnel à installation filaire avec relais de coupure moteur et batterie de secours intégrée.',
            'specifications': '4G LTE\nInstallation filaire\nRelais coupure moteur\nBatterie de secours\nAntenne GPS externe\nMicro SIM',
            'price_range': '350 - 550 MAD',
            'order': 2,
        },
        {
            'name': 'Traceur GPS Magnétique Autonome',
            'slug': 'traceur-gps-magnetique',
            'category': 'magnetic',
            'description': 'Traceur GPS autonome avec aimant puissant et batterie longue durée, idéal pour la surveillance discrète et le suivi d\'actifs.',
            'specifications': '4G LTE\nAimant puissant\nBatterie 5000mAh\nÉtanche IP67\nJusqu\'à 90 jours d\'autonomie\nAlerte de mouvement',
            'price_range': '600 - 900 MAD',
            'order': 3,
        },
        {
            'name': 'Traceur Personnel / Asset Tracker',
            'slug': 'traceur-personnel-asset',
            'category': 'personal',
            'description': 'Traceur GPS personnel compact et léger avec bouton SOS, idéal pour les personnes âgées, enfants et petits actifs.',
            'specifications': '4G LTE\nCompact et léger\nBouton SOS\nGéo-clôture\nHistorique de trajet\nApplication mobile',
            'price_range': '250 - 400 MAD',
            'order': 4,
        },
        {
            'name': 'Sonde Carburant Capacitive',
            'slug': 'sonde-carburant-capacitive',
            'category': 'sensor',
            'description': 'Sonde de niveau carburant capacitive haute précision pour la surveillance de la consommation et la détection de vol de carburant.',
            'specifications': 'Précision ±1%\nLongueur ajustable\nCompatible tous réservoirs\nSortie analogique\nRésistant aux carburants\nInstallation professionnelle',
            'price_range': '800 - 1200 MAD',
            'order': 5,
        },
        {
            'name': 'Capteur de Température',
            'slug': 'capteur-temperature',
            'category': 'sensor',
            'description': 'Capteur de température pour le monitoring de la chaîne du froid avec alertes en temps réel et plage de mesure étendue.',
            'specifications': 'Plage -40°C à +80°C\nPrécision ±0.5°C\nÉtanche IP68\nCâble 3m\nIdéal chaîne du froid\nAlertes en temps réel',
            'price_range': '350 - 500 MAD',
            'order': 6,
        },
    ]

    for data in products_data:
        slug = data.pop('slug')
        obj, created = Product.objects.update_or_create(
            slug=slug,
            defaults={**data, 'is_featured': True, 'is_available': True}
        )
        status = "created" if created else "updated"
        print(f"  Product '{obj.name}' {status}.")
    print("✓ Populated Products.")

    # 4. Testimonials
    testimonials_data = [
        {
            'client_name': 'Ahmed Benali',
            'company': 'Transport Atlas Fès',
            'role': 'Directeur Général',
            'content': 'M2web a transformé la gestion de notre flotte de 45 camions. Le suivi en temps réel et les alertes de consommation nous ont permis de réduire nos coûts carburant de 20%.',
            'rating': 5,
            'order': 1,
        },
        {
            'client_name': 'Fatima Zahra El Amrani',
            'company': 'Livraison Express Maroc',
            'role': 'Responsable Logistique',
            'content': 'Service impeccable et support technique réactif. Les traceurs GPS 4G sont fiables et l\'application mobile est très intuitive. Je recommande vivement M2web.',
            'rating': 5,
            'order': 2,
        },
        {
            'client_name': 'Karim Tazi',
            'company': 'Location Auto Fès',
            'role': 'Gérant',
            'content': 'Grâce à M2web, nous avons sécurisé notre parc de 80 véhicules de location. La coupure moteur à distance nous a sauvé plusieurs fois du vol.',
            'rating': 5,
            'order': 3,
        },
        {
            'client_name': 'Youssef Alaoui',
            'company': 'Frigorifique du Nord',
            'role': 'Directeur Technique',
            'content': 'Les capteurs de température et le suivi de la chaîne du froid nous permettent de garantir la qualité de nos livraisons. M2web comprend les besoins du transport frigorifique.',
            'rating': 4,
            'order': 4,
        },
    ]

    for data in testimonials_data:
        client_name = data.pop('client_name')
        obj, created = Testimonial.objects.update_or_create(
            client_name=client_name, defaults=data
        )
        status = "created" if created else "updated"
        print(f"  Testimonial '{obj.client_name}' {status}.")
    print("✓ Populated Testimonials.")

    # 5. Partners (logo field is required — create a minimal 1x1 PNG placeholder)
    import struct
    import zlib

    def create_minimal_png():
        """Create a minimal valid 1x1 white PNG image."""
        header = b'\x89PNG\r\n\x1a\n'
        ihdr_data = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
        ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data) & 0xffffffff
        ihdr = struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
        raw = b'\x00\xff\xff\xff'
        compressed = zlib.compress(raw)
        idat_crc = zlib.crc32(b'IDAT' + compressed) & 0xffffffff
        idat = struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', idat_crc)
        iend_crc = zlib.crc32(b'IEND') & 0xffffffff
        iend = struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc)
        return header + ihdr + idat + iend

    png_data = create_minimal_png()

    partners_data = [
        'Transport Atlas',
        'Livraison Express Maroc',
        'Auto Location Fès',
        'Frigorifique du Nord',
    ]

    for i, name in enumerate(partners_data, 1):
        partner, created = Partner.objects.get_or_create(
            name=name,
            defaults={'is_active': True, 'order': i}
        )
        if created:
            partner.logo.save(f'partner_{i}_placeholder.png', ContentFile(png_data), save=True)
            print(f"  Partner '{name}' created.")
        else:
            print(f"  Partner '{name}' already exists.")
    print("✓ Populated Partners.")

    # 6. Blog Categories
    categories_data = [
        {'name': 'Guides GPS', 'slug': 'guides-gps', 'description': 'Guides et tutoriels sur les traceurs GPS'},
        {'name': 'Actualités', 'slug': 'actualites', 'description': 'Actualités du secteur GPS et télématique au Maroc'},
        {'name': 'Gestion de Flotte', 'slug': 'gestion-flotte', 'description': 'Conseils pour la gestion de flotte automobile'},
    ]

    cats = {}
    for data in categories_data:
        slug = data.pop('slug')
        obj, created = Category.objects.update_or_create(slug=slug, defaults=data)
        cats[slug] = obj
        status = "created" if created else "updated"
        print(f"  Category '{obj.name}' {status}.")
    print("✓ Populated Blog Categories.")

    # 7. Blog Posts
    posts_data = [
        {
            'title': 'Comment choisir le meilleur traceur GPS pour votre véhicule au Maroc',
            'slug': 'choisir-meilleur-traceur-gps-maroc',
            'category': cats['guides-gps'],
            'excerpt': 'Guide complet pour sélectionner le traceur GPS adapté à vos besoins : OBD-II, filaire ou magnétique ? Comparatif des technologies 4G disponibles au Maroc.',
            'content': '''<h2>Les différents types de traceurs GPS</h2>
<p>Le choix d'un traceur GPS dépend de vos besoins spécifiques. Au Maroc, trois grandes catégories de traceurs dominent le marché :</p>
<h3>1. Traceurs OBD-II (Plug & Play)</h3>
<p>Les traceurs OBD-II se branchent directement sur le port diagnostic de votre véhicule. Installation instantanée sans câblage. Idéal pour les véhicules personnels et les petites flottes.</p>
<h3>2. Traceurs Filaires (Hardwired)</h3>
<p>Les traceurs filaires nécessitent une installation professionnelle mais offrent une sécurité accrue avec la possibilité de coupure moteur à distance. Recommandé pour les flottes professionnelles.</p>
<h3>3. Traceurs Magnétiques Autonomes</h3>
<p>Avec leur batterie longue durée et leur aimant puissant, ces traceurs sont parfaits pour la surveillance temporaire ou les actifs non motorisés.</p>
<h2>Pourquoi choisir le 4G ?</h2>
<p>Avec l'extinction progressive du réseau 2G au Maroc, il est essentiel d'investir dans un traceur GPS 4G LTE pour garantir la pérennité de votre solution de suivi.</p>''',
        },
        {
            'title': 'Migration 2G vers 4G : Pourquoi mettre à jour votre traceur GPS',
            'slug': 'migration-2g-4g-traceur-gps',
            'category': cats['actualites'],
            'excerpt': 'Le réseau 2G est en fin de vie au Maroc. Découvrez pourquoi la migration vers le 4G est essentielle pour votre flotte et comment M2web vous accompagne.',
            'content': '''<h2>La fin du réseau 2G au Maroc</h2>
<p>Les opérateurs télécoms marocains retirent progressivement le réseau 2G pour réallouer les fréquences au 4G et 5G. Si votre traceur GPS fonctionne encore en 2G, il risque de perdre sa connectivité dans les prochains mois.</p>
<h2>Les avantages du 4G pour le suivi GPS</h2>
<ul>
<li><strong>Couverture élargie :</strong> Le réseau 4G couvre désormais plus de 95% du territoire marocain.</li>
<li><strong>Latence réduite :</strong> Les positions GPS remontent en quelques secondes, contre parfois 30 secondes en 2G.</li>
<li><strong>Fiabilité accrue :</strong> Moins de pertes de signal dans les zones denses ou rurales.</li>
<li><strong>Pérennité :</strong> Le 4G sera maintenu pendant au moins 10 ans supplémentaires.</li>
</ul>
<h2>M2web vous accompagne</h2>
<p>Notre équipe technique à Fès propose un service de migration clé en main : diagnostic de votre installation existante, remplacement des traceurs 2G par des modèles 4G, et reconfiguration de votre plateforme de suivi.</p>''',
        },
    ]

    for data in posts_data:
        slug = data.pop('slug')
        obj, created = BlogPost.objects.update_or_create(
            slug=slug,
            defaults={
                **data,
                'author': admin_user,
                'is_published': True,
                'published_date': timezone.now(),
            }
        )
        status = "created" if created else "updated"
        print(f"  Blog post '{obj.title}' {status}.")
    print("✓ Populated Blog Posts.")

    print("\n✅ Data population complete!")


if __name__ == '__main__':
    main()
