from django.contrib import admin
from .models import WholesaleInquiry

@admin.register(WholesaleInquiry)
class WholesaleInquiryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'city', 'monthly_volume', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'monthly_volume', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['company_name', 'contact_person', 'email']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
