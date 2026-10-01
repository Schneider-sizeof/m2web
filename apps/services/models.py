from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(help_text='Short description for cards')
    icon_class = models.CharField(max_length=100, default='bi bi-geo-alt', help_text='Bootstrap Icons class')
    detailed_content = CKEditor5Field('Contenu détaillé', config_name='extends', blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})

    @property
    def short_description(self):
        return self.description

    def __str__(self):
        return self.title

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('obd', _('Traceur OBD-II')),
        ('hardwired', _('Traceur Filaire (Hardwired)')),
        ('magnetic', _('Traceur Magnétique Autonome')),
        ('personal', _('Traceur Personnel / Portatif')),
        ('sensor', _('Capteur & Accessoire')),
    ]
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, allow_unicode=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    specifications = models.TextField(blank=True, help_text='Technical specs, one per line')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price_range = models.CharField(max_length=100, blank=True, help_text='e.g., 450 - 650 MAD')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    @property
    def price(self):
        return self.price_range

    def __str__(self):
        return self.name
