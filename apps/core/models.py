from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CompanyInfo(models.Model):
    # Brand & Identity
    company_name = models.CharField(max_length=200, default='M2web Maroc')
    tagline = models.TextField(blank=True, default='Solutions Avancées de Géolocalisation & Gestion de Flotte')
    phone = models.CharField(max_length=30, default='+212 6 62 24 49 39')
    phone_display = models.CharField(max_length=30, default='06 62 24 49 39', blank=True)
    email = models.EmailField(default='m2web@m2web.com')
    whatsapp_number = models.CharField(max_length=30, default='+212662244939', help_text='Format international sans espaces, ex: +212662244939')
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

    # Social Media
    linkedin_url = models.URLField(blank=True, default='https://linkedin.com/company/m2web-maroc')
    facebook_url = models.URLField(blank=True, default='https://facebook.com/m2web.maroc')
    instagram_url = models.URLField(blank=True, default='https://instagram.com/m2web_maroc')
    youtube_url = models.URLField(blank=True, default='https://youtube.com/@m2webmaroc')
    
    analytics_id = models.CharField(max_length=50, blank=True)
    meta_description = models.TextField(blank=True)

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

    def __str__(self):
        return self.company_name


class WhyChooseUsPillar(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    icon_class = models.CharField(max_length=100, default='bi bi-broadcast-pin', help_text='Classe Bootstrap Icons (ex: bi bi-broadcast-pin, bi bi-phone, bi bi-fuel-pump, bi bi-tools)')
    order = models.PositiveIntegerField(default=0, verbose_name='Ordre d\'affichage')
    is_active = models.BooleanField(default=True, verbose_name='Actif')

    class Meta:
        ordering = ['order']
        verbose_name = 'Pourquoi Nous Choisir (Pilier)'
        verbose_name_plural = 'Pourquoi Nous Choisir (Piliers)'

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
