import polib

for lang in ['en', 'ar', 'fr']:
    po_path = f'locale/{lang}/LC_MESSAGES/django.po'
    mo_path = f'locale/{lang}/LC_MESSAGES/django.mo'
    po = polib.pofile(po_path)
    po.save_as_mofile(mo_path)
    print(f"Compiled {po_path} -> {mo_path} ({len(po)} entries)")
