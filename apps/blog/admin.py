from django.contrib import admin
from django.utils import timezone
from modeltranslation.admin import TranslationAdmin
from .models import Category, BlogPost

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'author', 'is_published', 'published_date']
    list_filter = ['is_published', 'category', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'excerpt']
    date_hierarchy = 'created_at'
    actions = ['publish_posts', 'unpublish_posts']
    autocomplete_fields = ['category', 'author']

    @admin.action(description='Publier les articles sélectionnés')
    def publish_posts(self, request, queryset):
        queryset.update(is_published=True, published_date=timezone.now())

    @admin.action(description='Dépublier les articles sélectionnés')
    def unpublish_posts(self, request, queryset):
        queryset.update(is_published=False, published_date=None)
