from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nom'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=30, blank=True, verbose_name=_('Téléphone'))
    subject = models.CharField(max_length=300, verbose_name=_('Sujet'))
    message = models.TextField(verbose_name=_('Message'))
    is_read = models.BooleanField(default=False, verbose_name=_('Lu'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date d\'envoi'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"{self.name} - {self.subject}"
