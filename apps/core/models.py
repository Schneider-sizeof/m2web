from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class CompanyInfo(models.Model):
    # Brand & Identity
    company_name = models.CharField(max_length=200, default='M2web Maroc')
    tagline = models.TextField(blank=True, default='Solutions Avancées de Géolocalisation & Gestion de Flotte')
    phone = models.CharField(max_length=30, default='+212 6 61 76 14 89', verbose_name='Téléphone Mobile')
    phone_display = models.CharField(max_length=30, default='06 61 76 14 89', blank=True, verbose_name='Mobile (Affichage)')
    phone_fix = models.CharField(max_length=30, default='+212 5 35 94 02 71', verbose_name='Téléphone Fixe')
    phone_fix_display = models.CharField(max_length=30, default='05 35 94 02 71', blank=True, verbose_name='Fixe (Affichage)')
    email = models.EmailField(default='m2web@m2web.com')
    whatsapp_number = models.CharField(max_length=30, default='+212661761489', help_text='Format international sans espaces, ex: +212661761489')
    address = models.TextField(default='CN, 2 Rue Ibn Al Kayem, Fès 30000, Maroc')
    city = models.CharField(max_length=100, default='Fès')
    country = models.CharField(max_length=100, default='Maroc')
    google_maps_url = models.URLField(blank=True, default='https://www.google.com/maps/place/M2web+Maroc/data=!4m2!3m1!1s0x0:0xe6a8036782c11407')
    google_maps_embed_url = models.TextField(blank=True, help_text='Google Maps iframe embed URL', default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3306.073998701988!2d-5.0069811!3d34.0419356!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd9f8b484d445777%3A0x10e6aaae728148b5!2s2%20Rue%20Ibn%20Al%20Kayem%2C%20Fes%2030000%2C%20Morocco!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s')
    
    # Header & Topbar
    topbar_badge = models.CharField(max_length=100, default='Fournisseur Agréé', help_text='Badge affiché dans la barre supérieure')
    topbar_warranty = models.CharField(max_length=150, default='Garantie & Support Direct', help_text='Texte de garantie dans la topbar')

    # Operating Hours
    operating_hours_weekday = models.CharField(max_length=100, default='08:30 – 18:30')
    operating_hours_saturday = models.CharField(max_length=100, default='08:30 – 13:30')
    operating_hours_sunday = models.CharField(max_length=100, default='Fermé')

    # Hero Section
    hero_badge = models.CharField(max_length=200, default='N°1 de la Géolocalisation & Télématique au Maroc')
    hero_title_line1 = models.CharField(max_length=100, default='Prenez le Contrôle')
    hero_title_highlight = models.CharField(max_length=100, default='Total de Votre Flotte')
    hero_title_line2 = models.CharField(max_length=100, default='en Temps Réel')
    hero_subtitle = models.TextField(default='Fournisseur direct de traceurs GPS 4G & solutions télématiques avancées à Fès et partout au Maroc. Réduisez vos coûts de carburant de 20%, protégez vos véhicules contre le vol et suivez vos actifs 24/7 sur smartphone & PC.')
    hero_trust_badge_1 = models.CharField(max_length=100, default='Traceurs 4G Certifiés')
    hero_trust_badge_2 = models.CharField(max_length=100, default='Installation sur Site')
    hero_trust_badge_3 = models.CharField(max_length=100, default='Support 24/7 à Fès')

    # Stats Section
    stat_trackers_count = models.PositiveIntegerField(default=5000, help_text='Nombre de traceurs installés')
    stat_trackers_label = models.CharField(max_length=100, default='Trackers Installés')
    stat_fleets_count = models.PositiveIntegerField(default=350, help_text='Nombre de flottes gérées')
    stat_fleets_label = models.CharField(max_length=100, default='Flottes Gérées')
    stat_uptime_count = models.CharField(max_length=50, default='99.8%', help_text='Pourcentage disponibilité')
    stat_uptime_label = models.CharField(max_length=100, default='Disponibilité Serveurs')
    stat_experience_count = models.PositiveIntegerField(default=10, help_text='Années expérience')
    stat_experience_label = models.CharField(max_length=100, default="Années d'Expertise à Fès")

    # B2B Banner
    b2b_banner_badge = models.CharField(max_length=100, default='ESPACE REVENDEURS & GROSSISTES')
    b2b_banner_title = models.CharField(max_length=200, default='Vous êtes installateur, intégrateur ou revendeur ?')
    b2b_banner_desc = models.TextField(default="Bénéficiez de tarifs grossiste préférentiels, d'un stock disponible immédiatement à Fès et d'un support technique d'experts pour développer votre activité au Maroc.")

    # About Page Texts
    about_story_title = models.CharField(max_length=200, default='Notre Histoire & Mission')
    about_lead = models.TextField(default='Basée à Fès, M2web Maroc est une entreprise technologique spécialisée dans les solutions de géolocalisation et la gestion de flotte.')
    about_text = models.TextField(default="Depuis notre création, nous nous sommes engagés à fournir à nos clients des outils fiables, précis et faciles à utiliser pour optimiser leurs opérations logistiques. Notre mission est d'accompagner les entreprises marocaines dans leur transformation numérique en leur offrant une visibilité totale sur leurs actifs mobiles.")

    # Brand Media & Images
    logo = models.ImageField(upload_to='company/', blank=True, null=True, verbose_name='Logo principal du site', help_text='Logo affiché dans la barre de navigation et le pied de page.')
    favicon = models.ImageField(upload_to='company/', blank=True, null=True, verbose_name='Favicon du site (.ico / .png)', help_text='Icône affichée dans l\'onglet du navigateur.')
    about_image = models.ImageField(upload_to='company/', blank=True, null=True, verbose_name='Photo page À Propos', help_text='Image représentant l\'équipe ou les locaux sur la page À Propos. Recommandé: 800x600px')
    platform_screenshot = models.ImageField(upload_to='platform/', blank=True, null=True, verbose_name='Capture d\'écran Plateforme GPS Web', help_text='Capture d\'écran de la plateforme web affichée sur la page Plateforme & Serveur GPS.')
    promo_video_url = models.URLField(blank=True, verbose_name='URL Vidéo Promotionnelle (YouTube/Vimeo)', help_text='Lien vidéo de présentation affiché sur le site web.')
    hero_slider_image_1 = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Slide Hero 1 (Plateforme & Dashboard)', help_text='Image affichée sur le 1er slide du hero d\'accueil.')
    hero_slider_image_2 = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Slide Hero 2 (Suivi de Flotte)', help_text='Image affichée sur le 2ème slide du hero d\'accueil.')
    hero_slider_image_3 = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Slide Hero 3 (App Mobile & Rapports)', help_text='Image affichée sur le 3ème slide du hero d\'accueil.')

    # Hero Background Media
    hero_bg_video = models.FileField(upload_to='hero/', blank=True, null=True, verbose_name='Vidéo de fond Hero (MP4)', help_text='Vidéo de fond pour le hero de la page d\'accueil. Format MP4, max 10MB recommandé.')
    hero_bg_image = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Image de fond Hero', help_text='Image de fond alternative si pas de vidéo. Taille recommandée: 1920x1080px')
    hero_bg_overlay_opacity = models.FloatField(default=0.7, verbose_name='Opacité overlay hero', help_text='0.0 = transparent, 1.0 = opaque. Recommandé: 0.6-0.8')
    page_header_bg = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Image fond en-tête sous-pages', help_text='Image de fond par défaut pour les en-têtes de toutes les sous-pages')

    # Social Media
    linkedin_url = models.URLField(blank=True, default='https://linkedin.com/company/m2web-maroc')
    facebook_url = models.URLField(blank=True, default='https://facebook.com/m2web.maroc')
    instagram_url = models.URLField(blank=True, default='https://instagram.com/m2web_maroc')
    youtube_url = models.URLField(blank=True, default='https://youtube.com/@m2webmaroc')
    
    analytics_id = models.CharField(max_length=50, blank=True)
    meta_description = models.TextField(blank=True)

    # Navbar Action Buttons (Customizable from Admin)
    login_button_url = models.URLField(
        default='https://trackmaroc.com', blank=True,
        verbose_name='Lien du bouton Connexion',
        help_text='URL de redirection du bouton "Connexion" dans la barre de navigation (ex: https://trackmaroc.com).'
    )
    login_button_text = models.CharField(
        max_length=50, default='Connexion', blank=True,
        verbose_name='Texte du bouton Connexion',
        help_text='Texte affiché sur le bouton (ex: Connexion, Sign In, Se connecter).'
    )
    login_button_title = models.CharField(
        max_length=150, default='Connexion Plateforme Trackmaroc', blank=True,
        verbose_name='Infobulle du bouton Connexion (alt/title)',
        help_text='Texte affiché au survol du bouton (tooltip/alt text).'
    )
    quote_button_text = models.CharField(
        max_length=50, default='Demander un Devis', blank=True,
        verbose_name='Texte du bouton Devis',
        help_text='Texte affiché sur le bouton devis (ex: Demander un Devis, Request a Quote).'
    )

    class Meta:
        verbose_name = 'Configuration Générale & Société'
        verbose_name_plural = 'Configuration Générale & Société'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(CompanyInfo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1, defaults={'company_name': 'M2web Maroc'})
        return obj

    @property
    def name(self):
        return self.company_name

    @property
    def get_login_button_text(self):
        from django.utils.translation import get_language, gettext as _
        lang = (get_language() or 'fr')[:2]
        if lang == 'ar':
            val = (getattr(self, 'login_button_text_ar', None) or '').strip()
            if val and val != 'Connexion':
                return val
            return _('Connexion')
        elif lang == 'en':
            val = (getattr(self, 'login_button_text_en', None) or '').strip()
            if val and val != 'Connexion':
                return val
            return _('Connexion')
        return getattr(self, 'login_button_text_fr', None) or getattr(self, 'login_button_text', None) or _('Connexion')

    @property
    def get_quote_button_text(self):
        from django.utils.translation import get_language, gettext as _
        lang = (get_language() or 'fr')[:2]
        if lang == 'ar':
            val = (getattr(self, 'quote_button_text_ar', None) or '').strip()
            if val and val != 'Demander un Devis':
                return val
            return _('Demander un Devis')
        elif lang == 'en':
            val = (getattr(self, 'quote_button_text_en', None) or '').strip()
            if val and val != 'Demander un Devis':
                return val
            return _('Demander un Devis')
        return getattr(self, 'quote_button_text_fr', None) or getattr(self, 'quote_button_text', None) or _('Demander un Devis')

    @property
    def get_login_button_title(self):
        from django.utils.translation import get_language, gettext as _
        lang = (get_language() or 'fr')[:2]
        if lang == 'ar':
            val = (getattr(self, 'login_button_title_ar', None) or '').strip()
            if val and val != 'Connexion Plateforme Trackmaroc':
                return val
            return _('Connexion Plateforme Trackmaroc')
        elif lang == 'en':
            val = (getattr(self, 'login_button_title_en', None) or '').strip()
            if val and val != 'Connexion Plateforme Trackmaroc':
                return val
            return _('Connexion Plateforme Trackmaroc')
        return getattr(self, 'login_button_title_fr', None) or getattr(self, 'login_button_title', None) or _('Connexion Plateforme Trackmaroc')

    def get_promo_video_embed_url(self):
        """Converts YouTube or other video URLs into an embeddable iframe URL."""
        url = (self.promo_video_url or '').strip()
        if not url:
            try:
                ma = MobileApp.objects.first()
                if ma and ma.promo_video_url:
                    return ma.get_promo_video_embed_url()
            except Exception:
                pass
            return ''
        video_id = None
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0].split('&')[0]
        elif 'youtube.com/watch' in url:
            import urllib.parse
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query)
            if 'v' in params and params['v']:
                video_id = params['v'][0]
        elif 'youtube.com/shorts/' in url:
            video_id = url.split('youtube.com/shorts/')[1].split('?')[0].split('&')[0]
        elif 'youtube.com/embed/' in url:
            video_id = url.split('youtube.com/embed/')[1].split('?')[0].split('&')[0]
        elif 'youtube-nocookie.com/embed/' in url:
            video_id = url.split('youtube-nocookie.com/embed/')[1].split('?')[0].split('&')[0]

        if video_id:
            return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&enablejsapi=1"

        if 'vimeo.com/' in url and 'player.vimeo.com' not in url:
            v_id = url.split('vimeo.com/')[1].split('?')[0].split('&')[0]
            return f"https://player.vimeo.com/video/{v_id}"
        return url

    def __str__(self):
        return self.company_name


class WhyChooseUsPillar(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    icon_class = models.CharField(max_length=100, default='bi bi-broadcast-pin', help_text='Classe Bootstrap Icons (ex: bi bi-broadcast-pin, bi bi-phone, bi bi-fuel-pump, bi bi-tools)')
    link_url = models.CharField(max_length=255, blank=True, verbose_name='Lien de redirection', help_text='URL interne (ex: /services/ ou /mobile-app/ ou /wholesale/) ou externe. Si vide, redirige automatiquement vers la solution correspondante.')
    order = models.PositiveIntegerField(default=0, verbose_name='Ordre d\'affichage')
    is_active = models.BooleanField(default=True, verbose_name='Actif')

    class Meta:
        ordering = ['order']
        verbose_name = 'Pourquoi Nous Choisir (Pilier)'
        verbose_name_plural = 'Pourquoi Nous Choisir (Piliers)'

    def get_link_url(self):
        from django.urls import reverse
        if self.link_url:
            clean = self.link_url.strip().strip('/')
            if clean in ('mobile-app', 'application-mobile', 'app'):
                try:
                    return reverse('core:mobile_app')
                except Exception:
                    pass
            elif clean == 'services':
                try:
                    return reverse('services:list')
                except Exception:
                    pass
            elif clean == 'contact':
                try:
                    return reverse('contact:contact')
                except Exception:
                    pass
            elif clean in ('a-propos', 'about'):
                try:
                    return reverse('core:about')
                except Exception:
                    pass
            return self.link_url

        titles = [
            getattr(self, 'title_fr', None) or '',
            getattr(self, 'title_en', None) or '',
            getattr(self, 'title_ar', None) or '',
            self.title or ''
        ]
        t = ' '.join(titles).lower()

        try:
            if any(k in t for k in ['carburant', 'fuel', 'sonde', 'وقود']):
                return reverse('services:detail', kwargs={'slug': 'controle-carburant-eco-conduite'})
            elif any(k in t for k in ['mobile', 'app', 'web', 'تطبيق', 'هاتف']):
                return reverse('core:mobile_app')
            elif any(k in t for k in ['4g', 'multi', 'réseau', 'network', 'شبكة']):
                return reverse('services:list')
            elif any(k in t for k in ['install', 'support', 'fès', 'fez', 'تركيب', 'دعم']):
                return reverse('contact:contact')
            return reverse('services:list')
        except Exception:
            return reverse('core:home')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    @property
    def name(self):
        return self.client_name

    @property
    def company_name(self):
        return self.company

    def __str__(self):
        return f"{self.client_name} - {self.company}"


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/')
    website_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre de l'offre")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    badge = models.CharField(max_length=100, default='OFFRE SPÉCIALE', verbose_name="Badge promo (ex: -20%, PROMO FLASH)")
    discount_label = models.CharField(max_length=50, blank=True, verbose_name="Remise affichée (ex: -20%, -300 DH)")
    summary = models.TextField(verbose_name="Résumé court")
    description = models.TextField(blank=True, verbose_name="Description détaillée")
    features = models.TextField(blank=True, help_text="Avantages inclus, un par ligne", verbose_name="Éléments inclus (1 par ligne)")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Prix d'origine (DH)")
    promo_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix promotionnel (DH)")
    price_unit = models.CharField(max_length=50, default='/ traceur', verbose_name="Unité de prix (ex: / traceur, / pack)")
    image = models.ImageField(upload_to='promotions/', blank=True, null=True, verbose_name="Image illustrative")
    valid_until = models.DateField(null=True, blank=True, verbose_name="Date limite de validité")
    cta_text = models.CharField(max_length=100, default="Profiter de l'offre", verbose_name="Texte du bouton CTA")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    is_featured = models.BooleanField(default=False, verbose_name="Mettre en avant sur l'accueil")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Promotion & Offre'
        verbose_name_plural = 'Promotions & Offres'

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title) or 'promo'
            slug = base_slug
            counter = 1
            while Promotion.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_features_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    def __str__(self):
        return f"{self.title} ({self.badge})"

class MobileApp(models.Model):
    """Singleton model for the GPS Tracking mobile app promotion page."""
    app_name = models.CharField(max_length=200, default='M2web GPS Tracker')
    tagline = models.CharField(max_length=300, default='Suivez votre flotte en temps réel depuis votre smartphone')
    hero_title = models.CharField(max_length=200, default='Application Mobile GPS')
    hero_subtitle = models.TextField(default="Téléchargez notre application de suivi GPS et gardez un œil sur vos véhicules 24/7, où que vous soyez.")
    description = models.TextField(default="Notre application mobile M2web GPS Tracker vous offre un contrôle total sur votre flotte depuis votre smartphone Android. Interface intuitive, notifications en temps réel, et rapports détaillés à portée de main.")
    
    # Download links
    android_url = models.URLField(blank=True, default='https://play.google.com/store/apps/details?id=com.m2web.gps', verbose_name='Lien Google Play Store')
    android_available = models.BooleanField(default=True, verbose_name='Disponible sur Android')
    ios_url = models.URLField(blank=True, verbose_name='Lien App Store (iOS)')
    ios_available = models.BooleanField(default=False, verbose_name='Disponible sur iOS')
    ios_coming_soon = models.BooleanField(default=False, verbose_name='iOS bientôt disponible')
    
    # Media
    hero_image = models.ImageField(upload_to='app/', blank=True, null=True, verbose_name='Image principale (mockup téléphone)', help_text='Image de mockup du téléphone avec l\'app. Taille recommandée: 600x800px')
    promo_video_url = models.URLField(blank=True, verbose_name='URL vidéo promotionnelle (YouTube)')
    
    # Features section title
    features_title = models.CharField(max_length=200, default='Fonctionnalités Clés', verbose_name='Titre section fonctionnalités')
    features_subtitle = models.TextField(default='Tout ce dont vous avez besoin pour gérer votre flotte depuis votre poche.', verbose_name='Sous-titre fonctionnalités')
    
    # CTA section
    cta_title = models.CharField(max_length=200, default='Prêt à Prendre le Contrôle ?', verbose_name='Titre CTA')
    cta_subtitle = models.TextField(default="Téléchargez l'application gratuitement et commencez à suivre vos véhicules en quelques minutes.", verbose_name='Sous-titre CTA')
    
    is_active = models.BooleanField(default=True, verbose_name='Page active')
    
    class Meta:
        verbose_name = 'Application Mobile'
        verbose_name_plural = 'Application Mobile'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass
    
    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1, defaults={'app_name': 'M2web GPS Tracker'})
        return obj
    
    def get_promo_video_embed_url(self):
        """Converts YouTube or other video URLs into an embeddable iframe URL."""
        if not self.promo_video_url:
            return ''
        url = self.promo_video_url.strip()
        video_id = None
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0].split('&')[0]
        elif 'youtube.com/watch' in url:
            import urllib.parse
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query)
            if 'v' in params and params['v']:
                video_id = params['v'][0]
        elif 'youtube.com/shorts/' in url:
            video_id = url.split('youtube.com/shorts/')[1].split('?')[0].split('&')[0]
        elif 'youtube.com/embed/' in url:
            video_id = url.split('youtube.com/embed/')[1].split('?')[0].split('&')[0]
        elif 'youtube-nocookie.com/embed/' in url:
            video_id = url.split('youtube-nocookie.com/embed/')[1].split('?')[0].split('&')[0]

        if video_id:
            return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&enablejsapi=1"

        if 'vimeo.com/' in url and 'player.vimeo.com' not in url:
            v_id = url.split('vimeo.com/')[1].split('?')[0].split('&')[0]
            return f"https://player.vimeo.com/video/{v_id}"
        return url


    def __str__(self):
        return self.app_name



class AppFeature(models.Model):
    """Individual feature of the mobile app."""
    title = models.CharField(max_length=200, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    icon_class = models.CharField(max_length=100, default='bi bi-geo-alt-fill', help_text='Classe Bootstrap Icons', verbose_name='Icône')
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Fonctionnalité App'
        verbose_name_plural = 'Fonctionnalités App'
    
    def __str__(self):
        return self.title


class AppScreenshot(models.Model):
    """Screenshot/mockup of the mobile app."""
    image = models.ImageField(upload_to='app/screenshots/', verbose_name='Capture d\'écran')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Légende')
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Capture d\'écran App'
        verbose_name_plural = 'Captures d\'écran App'
    
    def __str__(self):
        return self.caption or f'Screenshot {self.pk}'


class AppPlan(models.Model):
    """Pricing/membership plan for the mobile app."""
    PERIOD_CHOICES = [
        ('month', _('Par mois')),
        ('year', _('Par an')),
        ('once', _('Paiement unique')),
        ('free', _('Gratuit')),
    ]
    name = models.CharField(max_length=200, verbose_name='Nom du forfait')
    badge = models.CharField(max_length=100, blank=True, verbose_name='Badge (ex: POPULAIRE, RECOMMANDÉ)')
    description = models.TextField(blank=True, verbose_name='Description courte')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Prix (DH)')
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='month', verbose_name='Période')
    features = models.TextField(help_text='Un avantage par ligne', verbose_name='Avantages inclus')
    max_vehicles = models.CharField(max_length=100, default='1 véhicule', verbose_name='Nombre de véhicules')
    cta_text = models.CharField(max_length=100, default='Choisir ce forfait', verbose_name='Texte du bouton')
    is_featured = models.BooleanField(default=False, verbose_name='Mis en avant')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Forfait App'
        verbose_name_plural = 'Forfaits App'
    
    def get_features_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.split('\n') if f.strip()]
    
    def __str__(self):
        return f"{self.name} - {self.price} DH/{self.get_period_display()}"


class AppInquiry(models.Model):
    """Inquiry/request from users interested in the mobile app."""
    INTEREST_CHOICES = [
        ('free', 'Essai gratuit'),
        ('basic', 'Forfait Essentiel'),
        ('pro', 'Forfait Pro'),
        ('enterprise', 'Forfait Entreprise'),
        ('info', 'Demande d\'information'),
    ]
    name = models.CharField(max_length=200, verbose_name='Nom & Prénom')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=30, verbose_name='Téléphone')
    company = models.CharField(max_length=200, blank=True, verbose_name='Entreprise')
    plan_interest = models.CharField(max_length=20, choices=INTEREST_CHOICES, default='info', verbose_name='Forfait souhaité')
    fleet_size = models.CharField(max_length=100, blank=True, verbose_name='Nombre de véhicules')
    message = models.TextField(blank=True, verbose_name='Message')
    is_processed = models.BooleanField(default=False, verbose_name='Traité')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de demande')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Demande App Mobile'
        verbose_name_plural = 'Demandes App Mobile'
    
    def __str__(self):
        return f"{self.name} - {self.get_plan_interest_display()}"
