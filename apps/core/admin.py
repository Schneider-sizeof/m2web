from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CompanyInfo, WhyChooseUsPillar, Testimonial, Partner

admin.site.site_header = 'M2web Maroc — Administration'
admin.site.site_title = 'M2web Admin'
admin.site.index_title = 'Tableau de Bord & Gestion de Contenu'

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identité & Coordonnées Principales', {
            'fields': (
                'company_name', 'tagline', 'phone', 'phone_display', 'whatsapp_number', 
                'email', 'address', 'city', 'country', 'google_maps_url', 'google_maps_embed_url'
            )
        }),
        ('Barre Supérieure & En-tête (Topbar)', {
            'description': 'Textes et badges affichés tout en haut du site web',
            'fields': ('topbar_badge', 'topbar_warranty')
        }),
        ('Section Hero (Bannière Accueil)', {
            'description': 'Titres, sous-titres et arguments clés affichés sur la page d\'accueil',
            'fields': (
                'hero_badge', 'hero_title_line1', 'hero_title_highlight', 'hero_title_line2', 
                'hero_subtitle', 'hero_trust_badge_1', 'hero_trust_badge_2', 'hero_trust_badge_3'
            )
        }),
        ('Statistiques Chiffrées Clés', {
            'description': 'Chiffres animés présentés sous la bannière d\'accueil',
            'fields': (
                ('stat_trackers_count', 'stat_trackers_label'),
                ('stat_fleets_count', 'stat_fleets_label'),
                ('stat_uptime_count', 'stat_uptime_label'),
                ('stat_experience_count', 'stat_experience_label'),
            )
        }),
        ('Bannière Espace B2B & Grossistes', {
            'description': 'Encadré d\'appel à l\'action pour les installateurs et revendeurs',
            'fields': ('b2b_banner_badge', 'b2b_banner_title', 'b2b_banner_desc')
        }),
        ('Page À Propos', {
            'description': 'Textes de présentation de l\'entreprise sur la page À Propos',
            'fields': ('about_story_title', 'about_lead', 'about_text')
        }),
        ('Horaires d\'Ouverture Showroom & Support', {
            'fields': ('operating_hours_weekday', 'operating_hours_saturday', 'operating_hours_sunday')
        }),
        ('Réseaux Sociaux', {
            'fields': ('linkedin_url', 'facebook_url', 'instagram_url', 'youtube_url')
        }),
        ('Référencement & Balises SEO', {
            'fields': ('meta_description', 'analytics_id')
        }),
    )

    def has_add_permission(self, request):
        if CompanyInfo.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(WhyChooseUsPillar)
class WhyChooseUsPillarAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'icon_class', 'is_active']
    list_editable = ['title', 'icon_class', 'is_active']
    list_display_links = ['order']
    search_fields = ['title', 'description']
    ordering = ['order']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'company', 'role', 'rating', 'is_active', 'order']
    list_filter = ['is_active', 'rating']
    list_editable = ['is_active', 'order']
    search_fields = ['client_name', 'company', 'content']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website_url', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['name']
