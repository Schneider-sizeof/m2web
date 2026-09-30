from django.db import models
from django.utils.translation import gettext_lazy as _

class WholesaleInquiry(models.Model):
    VOLUME_CHOICES = [
        ('10-50', '10 – 50 unités/mois'),
        ('50-200', '50 – 200 unités/mois'),
        ('200+', '200+ unités/mois')
    ]
    
    company_name = models.CharField(max_length=200, verbose_name=_('Nom de l\'entreprise'))
    contact_person = models.CharField(max_length=200, verbose_name=_('Personne de contact'))
    email = models.EmailField(verbose_name=_('Adresse email'))
    phone = models.CharField(max_length=30, verbose_name=_('Téléphone'))
    city = models.CharField(max_length=100, verbose_name=_('Ville'))
    monthly_volume = models.CharField(max_length=10, choices=VOLUME_CHOICES, verbose_name=_('Volume mensuel'))
    hardware_types_needed = models.TextField(help_text=_('Types of GPS trackers needed'), verbose_name=_('Types d\'équipements souhaités'))
    message = models.TextField(blank=True, verbose_name=_('Message'))
    is_processed = models.BooleanField(default=False, verbose_name=_('Traité'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de création'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Demande B2B'
        verbose_name_plural = 'Demandes B2B'

    def __str__(self):
        return f"{self.company_name} - {self.contact_person}"


class ResellerInquiry(models.Model):
    ACTIVITY_CHOICES = [
        ('auto_electrician', _('Électricien auto / Installateur')),
        ('it_telecom', _('Revendeur informatique & télécom')),
        ('security', _('Société de sécurité / Gardiennage')),
        ('car_rental', _('Loueur de véhicules / Agence de transport')),
        ('distributor', _('Grossiste / Distributeur commercial')),
        ('other', _('Autre professionnel')),
    ]
    VOLUME_CHOICES = [
        ('5-15', _('5 – 15 traceurs / mois (Pack Découverte)')),
        ('15-50', _('15 – 50 traceurs / mois (Pack Pro Installateur)')),
        ('50+', _('50+ traceurs / mois (Distributeur Régional)')),
        ('server', _('Projet Serveur Dédié / Marque Blanche')),
    ]

    company_name = models.CharField(max_length=200, verbose_name=_('Nom de l\'entreprise / Atelier'))
    contact_person = models.CharField(max_length=200, verbose_name=_('Nom & Prénom du responsable'))
    email = models.EmailField(verbose_name=_('Adresse email'))
    phone = models.CharField(max_length=30, verbose_name=_('Téléphone / WhatsApp'))
    city = models.CharField(max_length=100, verbose_name=_('Ville d\'activité'))
    activity_type = models.CharField(max_length=30, choices=ACTIVITY_CHOICES, default='auto_electrician', verbose_name=_('Secteur d\'activité'))
    expected_volume = models.CharField(max_length=20, choices=VOLUME_CHOICES, default='5-15', verbose_name=_('Volume mensuel estimé'))
    has_installed_before = models.BooleanField(default=False, verbose_name=_('Avez-vous déjà installé des traceurs GPS ?'))
    interested_in_whitelabel = models.BooleanField(default=False, verbose_name=_('Intéressé par une plateforme en Marque Blanche'))
    message = models.TextField(blank=True, verbose_name=_('Message / Besoins particuliers'))
    is_processed = models.BooleanField(default=False, verbose_name=_('Traité'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de candidature'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Candidature Revendeur'
        verbose_name_plural = 'Candidatures Revendeurs'

    def __str__(self):
        return f"[Revendeur] {self.company_name} ({self.city}) - {self.contact_person}"


class PlatformInquiry(models.Model):
    OPTION_CHOICES = [
        ('rent_saas', _('Location / Abonnement SaaS (Par véhicule / mois ou an)')),
        ('buy_server', _('Achat de Serveur / Licence Définitive On-Premise')),
        ('whitelabel', _('Plateforme Serveur en Marque Blanche Complète (Logo + Domaine + App)')),
        ('custom', _('Développement / Intégration sur-mesure (API / ERP / Télématique)')),
    ]
    FLEET_SIZE_CHOICES = [
        ('1-10', _('1 à 10 véhicules')),
        ('11-50', _('11 à 50 véhicules')),
        ('51-200', _('51 à 200 véhicules')),
        ('200+', _('Plus de 200 véhicules')),
    ]

    company_name = models.CharField(max_length=200, verbose_name=_('Nom de l\'entreprise / Organisation'))
    contact_name = models.CharField(max_length=200, verbose_name=_('Nom du responsable'))
    email = models.EmailField(verbose_name=_('Adresse email'))
    phone = models.CharField(max_length=30, verbose_name=_('Téléphone / WhatsApp'))
    city = models.CharField(max_length=100, verbose_name=_('Ville'))
    acquisition_mode = models.CharField(max_length=20, choices=OPTION_CHOICES, default='rent_saas', verbose_name=_('Formule souhaitée'))
    fleet_size = models.CharField(max_length=20, choices=FLEET_SIZE_CHOICES, default='11-50', verbose_name=_('Taille de la flotte'))
    needs_reports = models.BooleanField(default=True, verbose_name=_('Besoin de rapports avancés & statistiques'))
    needs_fuel_sensor = models.BooleanField(default=False, verbose_name=_('Besoin de contrôle carburant / sondes'))
    message = models.TextField(blank=True, verbose_name=_('Détails du projet / Questions'))
    is_processed = models.BooleanField(default=False, verbose_name=_('Traité'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de demande'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Demande Plateforme & Serveur'
        verbose_name_plural = 'Demandes Plateforme & Serveur'

    def __str__(self):
        return f"[Plateforme] {self.company_name} ({self.get_acquisition_mode_display()})"
