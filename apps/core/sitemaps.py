from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.services.models import Service
from apps.blog.models import BlogPost, Category


class BaseM2webSitemap(Sitemap):
    protocol = 'https'
    i18n = True
    alternates = True
    x_default = True

    def get_domain(self, site=None):
        return 'm2webmaroc.com'


class StaticViewSitemap(BaseM2webSitemap):
    def items(self):
        return [
            ('core:home', 1.0, 'weekly'),
            ('core:about', 0.8, 'monthly'),
            ('core:mobile_app', 0.9, 'weekly'),
            ('core:promotions', 0.8, 'weekly'),
            ('services:list', 0.9, 'weekly'),
            ('wholesale:platform', 0.9, 'weekly'),
            ('wholesale:reseller', 0.8, 'monthly'),
            ('wholesale:inquiry', 0.8, 'monthly'),
            ('blog:list', 0.8, 'daily'),
            ('contact:contact', 0.8, 'monthly'),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]


class ServiceSitemap(BaseM2webSitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Service.objects.all().order_by('order')

    def location(self, obj):
        return obj.get_absolute_url()


class BlogPostSitemap(BaseM2webSitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return BlogPost.objects.filter(is_published=True).order_by('-published_date')

    def lastmod(self, obj):
        return obj.updated_at or obj.published_date

    def location(self, obj):
        return obj.get_absolute_url()


class BlogCategorySitemap(BaseM2webSitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Category.objects.all().order_by('name')

    def location(self, obj):
        return reverse('blog:category', kwargs={'category_slug': obj.slug})


# Consolidated dictionary of sitemaps
sitemaps = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
    'blog': BlogPostSitemap,
    'categories': BlogCategorySitemap,
}
