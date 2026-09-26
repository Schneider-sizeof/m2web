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
