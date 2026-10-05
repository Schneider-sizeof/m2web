from django.contrib import admin
from .models import WholesaleInquiry, ResellerInquiry, PlatformInquiry

@admin.register(WholesaleInquiry)
class WholesaleInquiryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'city', 'monthly_volume', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'monthly_volume', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['company_name', 'contact_person', 'email']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

@admin.register(ResellerInquiry)
class ResellerInquiryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'city', 'activity_type', 'expected_volume', 'interested_in_whitelabel', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'activity_type', 'expected_volume', 'interested_in_whitelabel', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['company_name', 'contact_person', 'email', 'phone', 'city']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

@admin.register(PlatformInquiry)
class PlatformInquiryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_name', 'city', 'acquisition_mode', 'fleet_size', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'acquisition_mode', 'fleet_size', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['company_name', 'contact_name', 'email', 'phone', 'city']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
from modeltranslation.admin import TranslationAdmin
from .models import ResellerTier

@admin.register(ResellerTier)
class ResellerTierAdmin(TranslationAdmin):
    list_display = ['title', 'badge_text', 'volume_label', 'discount_text', 'is_featured', 'is_active', 'order']
    list_editable = ['is_active', 'is_featured', 'order']
    list_filter = ['is_active', 'is_featured']
    fieldsets = (
        ('General', {
            'fields': ('title', 'description')
        }),
        ('Display', {
            'fields': ('badge_text', 'icon_class', 'badge_style', 'is_featured', 'is_active', 'order')
        }),
        ('Volume & Pricing', {
            'fields': ('volume_min', 'volume_max', 'volume_label', 'discount_text')
        }),
        ('Features', {
            'fields': ('features', 'cta_text', 'cta_url')
        }),
    )
