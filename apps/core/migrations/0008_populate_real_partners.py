from django.db import migrations

def populate_real_partners(apps, schema_editor):
    Partner = apps.get_model('core', 'Partner')
    
    # Remove older placeholder partners
    Partner.objects.all().delete()
    
    partners_data = [
        {
            'name': 'Orange',
            'logo': 'partners/orange.svg',
            'website_url': 'https://www.orange.ma',
            'order': 1,
            'is_active': True,
        },
        {
            'name': 'Coca-Cola',
            'logo': 'partners/coca_cola.svg',
            'website_url': 'https://www.coca-cola.com/ma/fr',
            'order': 2,
            'is_active': True,
        },
        {
            'name': 'Société Belmeki',
            'logo': 'partners/belmeki.svg',
            'website_url': '',
            'order': 3,
            'is_active': True,
        },
        {
            'name': 'Star Soda',
            'logo': 'partners/star_soda.svg',
            'website_url': '',
            'order': 4,
            'is_active': True,
        },
    ]
    
    for item in partners_data:
        Partner.objects.create(**item)

def reverse_partners(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_companyinfo_favicon_companyinfo_platform_screenshot_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_real_partners, reverse_partners),
    ]
