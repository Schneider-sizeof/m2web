from modeltranslation.translator import register, TranslationOptions
from .models import ResellerTier

@register(ResellerTier)
class ResellerTierTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'badge_text', 'volume_label', 'discount_text', 'features', 'cta_text')
