from modeltranslation.translator import register, TranslationOptions
from .models import Category, BlogPost

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'meta_description')
