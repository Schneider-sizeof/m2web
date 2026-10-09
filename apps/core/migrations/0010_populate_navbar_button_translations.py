from django.db import migrations

def populate_translations(apps, schema_editor):
    CompanyInfo = apps.get_model('core', 'CompanyInfo')
    for company in CompanyInfo.objects.all():
        company.login_button_text_fr = 'Connexion'
        company.quote_button_text_fr = 'Demander un Devis'
        company.login_button_title_fr = 'Connexion Plateforme Trackmaroc'

        company.login_button_text_en = 'Sign In'
        company.quote_button_text_en = 'Request a Quote'
        company.login_button_title_en = 'Login to Trackmaroc Platform'

        company.login_button_text_ar = 'تسجيل الدخول'
        company.quote_button_text_ar = 'طلب عرض سعر'
        company.login_button_title_ar = 'تسجيل الدخول إلى منصة تراك ماروك'

        company.save()

def backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_add_navbar_button_fields'),
    ]

    operations = [
        migrations.RunPython(populate_translations, backwards),
    ]
