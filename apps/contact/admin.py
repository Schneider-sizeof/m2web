from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'email', 'phone', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'company_name', 'email', 'phone', 'subject', 'message']
    readonly_fields = ['name', 'email', 'phone', 'company_name', 'subject', 'message', 'created_at']
    date_hierarchy = 'created_at'
    actions = ['mark_as_read', 'mark_as_unread']

    @admin.action(description='Marquer comme lu')
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description='Marquer comme non lu')
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
