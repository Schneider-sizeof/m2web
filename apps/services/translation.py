from modeltranslation.translator import translator, TranslationOptions
from .models import Service, Product

class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'detailed_content')

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'specifications', 'price_range')

translator.register(Service, ServiceTranslationOptions)
translator.register(Product, ProductTranslationOptions)
