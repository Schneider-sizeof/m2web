from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nom'))
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(blank=True, verbose_name=_('Description'))

    class Meta:
        ordering = ['name']
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('Titre'))
    slug = models.SlugField(unique=True, allow_unicode=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts', verbose_name=_('Catégorie'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts', verbose_name=_('Auteur'))
    excerpt = models.TextField(help_text=_('Short summary for listing pages'), max_length=500, verbose_name=_('Extrait'))
    content = CKEditor5Field('Contenu', config_name='extends')
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name=_('Image mise en avant'))
    meta_description = models.CharField(max_length=160, blank=True, verbose_name=_('Méta description'))
    is_published = models.BooleanField(default=False, verbose_name=_('Publié'))
    published_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Date de publication'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de création'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Dernière modification'))

    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    @property
    def image(self):
        return self.featured_image

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)
