from modeltranslation.translator import translator, TranslationOptions
from .models import CompanyInfo, Testimonial, WhyChooseUsPillar

class CompanyInfoTranslationOptions(TranslationOptions):
    fields = (
        'tagline',
        'meta_description',
        'operating_hours_weekday',
        'operating_hours_saturday',
        'operating_hours_sunday',
        'topbar_badge',
        'topbar_warranty',
        'hero_badge',
        'hero_title_line1',
        'hero_title_highlight',
        'hero_title_line2',
        'hero_subtitle',
        'hero_trust_badge_1',
        'hero_trust_badge_2',
        'hero_trust_badge_3',
        'stat_trackers_label',
        'stat_fleets_label',
        'stat_uptime_label',
        'stat_experience_label',
        'b2b_banner_badge',
        'b2b_banner_title',
        'b2b_banner_desc',
        'about_story_title',
        'about_lead',
        'about_text',
    )

class WhyChooseUsPillarTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class TestimonialTranslationOptions(TranslationOptions):
    fields = ('content', 'role')

translator.register(CompanyInfo, CompanyInfoTranslationOptions)
translator.register(WhyChooseUsPillar, WhyChooseUsPillarTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
