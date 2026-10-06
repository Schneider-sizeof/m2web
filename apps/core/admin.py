from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from .models import CompanyInfo, WhyChooseUsPillar, Testimonial, Partner, Promotion, MobileApp, AppFeature, AppScreenshot, AppPlan, AppInquiry

admin.site.site_header = 'M2web Maroc — Administration'
admin.site.site_title = 'M2web Admin'
admin.site.index_title = 'Tableau de Bord & Gestion de Contenu'

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identité & Coordonnées Principales', {
            'fields': (
                'company_name', 'tagline', 'phone', 'phone_display', 'phone_fix', 'phone_fix_display',
                'whatsapp_number', 'email', 'address', 'city', 'country', 'google_maps_url', 'google_maps_embed_url'
            )
        }),
        ('Logos, Vidéo & Médias Principaux (Tableau de Bord)', {
            'description': 'Logo officiel, favicon, capture plateforme GPS, vidéo de présentation, photo À Propos et diapositives d\'accueil',
            'fields': (
                ('logo', 'logo_preview'),
                ('favicon', 'favicon_preview'),
                ('platform_screenshot', 'platform_screenshot_preview'),
                'promo_video_url',
                ('about_image', 'about_image_preview'),
                'hero_slider_image_1', 'hero_slider_image_2', 'hero_slider_image_3'
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
        ('Médias de Fond (Hero & En-têtes)', {
            'description': 'Vidéo/image de fond pour le hero de la page d\'accueil et les en-têtes des sous-pages',
            'fields': ('hero_bg_video', 'hero_bg_image', 'hero_bg_overlay_opacity', 'page_header_bg')
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
        ('Boutons de la Barre de Navigation', {
            'description': 'Personnalisez le bouton Connexion et le bouton Devis dans la barre de navigation',
            'fields': ('login_button_url', 'login_button_text', 'login_button_title', 'quote_button_text')
        }),
        ('Réseaux Sociaux', {
            'fields': ('linkedin_url', 'facebook_url', 'instagram_url', 'youtube_url')
        }),
        ('Référencement & Balises SEO', {
            'fields': ('meta_description', 'analytics_id')
        }),
    )

    readonly_fields = ['logo_preview', 'favicon_preview', 'about_image_preview', 'platform_screenshot_preview']

    def logo_preview(self, obj):
        try:
            if obj and obj.logo:
                return format_html('<img src="{}" style="max-height: 48px; max-width: 180px; background: #1E1028; padding: 4px; border-radius: 4px;" />', obj.logo.url)
        except Exception:
            pass
        return "Aucun logo téléversé (logo par défaut actif)"
    logo_preview.short_description = "Aperçu Logo"

    def favicon_preview(self, obj):
        try:
            if obj and obj.favicon:
                return format_html('<img src="{}" style="max-height: 32px; max-width: 32px;" />', obj.favicon.url)
        except Exception:
            pass
        return "Favicon par défaut actif"
    favicon_preview.short_description = "Aperçu Favicon"

    def about_image_preview(self, obj):
        try:
            if obj and obj.about_image:
                return format_html('<img src="{}" style="max-height: 120px; max-width: 200px; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);" />', obj.about_image.url)
        except Exception:
            pass
        return "Aucune image personnalisée (image par défaut active)"
    about_image_preview.short_description = "Aperçu Photo À Propos"

    def platform_screenshot_preview(self, obj):
        try:
            if obj and obj.platform_screenshot:
                return format_html('<img src="{}" style="max-height: 120px; max-width: 200px; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);" />', obj.platform_screenshot.url)
        except Exception:
            pass
        return "Aucune capture personnalisée (tableau de bord par défaut actif)"
    platform_screenshot_preview.short_description = "Aperçu Capture Plateforme"

    def has_add_permission(self, request):
        if CompanyInfo.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(WhyChooseUsPillar)
class WhyChooseUsPillarAdmin(TranslationAdmin):
    list_display = ['order', 'title', 'icon_class', 'link_url', 'is_active']
    list_editable = ['title', 'icon_class', 'link_url', 'is_active']
    list_display_links = ['order']
    search_fields = ['title', 'description', 'link_url']
    ordering = ['order']

@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    list_display = ['client_name', 'company', 'role', 'rating', 'is_active', 'order']
    list_filter = ['is_active', 'rating']
    list_editable = ['is_active', 'order']
    search_fields = ['client_name', 'company', 'content']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['logo_preview', 'name', 'website_url', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'website_url']
    readonly_fields = ['logo_preview']

    def logo_preview(self, obj):
        try:
            if obj and obj.logo:
                return format_html('<img src="{}" style="max-height: 38px; max-width: 120px; object-fit: contain; background: #f8fafc; padding: 3px 8px; border: 1px solid #e2e8f0; border-radius: 6px;" />', obj.logo.url)
        except Exception:
            pass
        return "-"
    logo_preview.short_description = "Aperçu Logo"

@admin.register(Promotion)
class PromotionAdmin(TranslationAdmin):
    list_display = ['title', 'badge', 'discount_label', 'promo_price', 'original_price', 'valid_until', 'is_active', 'is_featured', 'order']
    list_filter = ['is_active', 'is_featured', 'badge']
    list_editable = ['is_active', 'is_featured', 'order']
    search_fields = ['title', 'summary', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order', '-created_at']

class AppFeatureInline(admin.TabularInline):
    model = AppFeature
    extra = 1
    fields = ['title', 'description', 'icon_class', 'order', 'is_active']

class AppScreenshotInline(admin.TabularInline):
    model = AppScreenshot
    extra = 1
    fields = ['image', 'caption', 'order', 'is_active']

@admin.register(MobileApp)
class MobileAppAdmin(TranslationAdmin):
    fieldsets = (
        ('Identité de l\'Application', {
            'fields': ('app_name', 'tagline', 'hero_title', 'hero_subtitle', 'description', 'is_active')
        }),
        ('Téléchargement & Disponibilité', {
            'fields': ('android_url', 'android_available')
        }),
        ('Médias', {
            'fields': ('hero_image', 'promo_video_url')
        }),
        ('Section Fonctionnalités', {
            'fields': ('features_title', 'features_subtitle')
        }),
        ('Section Appel à l\'Action', {
            'fields': ('cta_title', 'cta_subtitle')
        }),
    )
    
    def has_add_permission(self, request):
        if MobileApp.objects.exists():
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AppFeature)
class AppFeatureAdmin(TranslationAdmin):
    list_display = ['title', 'icon_class', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description']

@admin.register(AppScreenshot)
class AppScreenshotAdmin(TranslationAdmin):
    list_display = ['caption', 'order', 'is_active']
    list_editable = ['order', 'is_active']

@admin.register(AppPlan)
class AppPlanAdmin(TranslationAdmin):
    list_display = ['name', 'price', 'period', 'max_vehicles', 'is_featured', 'is_active', 'order']
    list_editable = ['price', 'is_featured', 'is_active', 'order']
    list_filter = ['is_active', 'is_featured', 'period']

@admin.register(AppInquiry)
class AppInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'company', 'plan_interest', 'fleet_size', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'plan_interest', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['name', 'email', 'phone', 'company']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
