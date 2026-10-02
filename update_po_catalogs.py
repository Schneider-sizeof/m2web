import polib
import sys

sys.stdout.reconfigure(encoding='utf-8')

new_translations = [
    {
        'msgid': '84 km/h • Transit Fès ➔ Casa • ⛽ 92%',
        'en': '84 km/h • Transit Fez ➔ Casa • ⛽ 92%',
        'ar': '84 كم/س • طريق فاس ➔ الدار البيضاء • ⛽ 92%',
        'fr': '84 km/h • Transit Fès ➔ Casa • ⛽ 92%'
    },
    {
        'msgid': 'Consommation 45L • Carburant 39%',
        'en': 'Consumption 45L • Fuel 39%',
        'ar': 'استهلاك 45 لتر • وقود 39%',
        'fr': 'Consommation 45L • Carburant 39%'
    },
    {
        'msgid': 'App iOS/Android',
        'en': 'iOS & Android App',
        'ar': 'تطبيق iOS وأندرويد',
        'fr': 'App iOS/Android'
    },
    {
        'msgid': 'Dacia Logan',
        'en': 'Dacia Logan',
        'ar': 'داسيا لوغان',
        'fr': 'Dacia Logan'
    },
    {
        'msgid': 'Fès → Casablanca • 84 km/h',
        'en': 'Fez → Casablanca • 84 km/h',
        'ar': 'فاس ← الدار البيضاء • 84 كم/س',
        'fr': 'Fès → Casablanca • 84 km/h'
    },
    {
        'msgid': 'Hay Riad, Rabat • 12 min',
        'en': 'Hay Riad, Rabat • 12 min',
        'ar': 'حي الرياض، الرباط • 12 دقيقة',
        'fr': 'Hay Riad, Rabat • 12 min'
    },
    {
        'msgid': 'M2web Fleet Telematics — Suivi en Direct',
        'en': 'M2web Fleet Telematics — Live Tracking',
        'ar': 'M2web تليماتيك الأساطيل — التتبع المباشر',
        'fr': 'M2web Fleet Telematics — Suivi en Direct'
    },
    {
        'msgid': 'Moto Livraison',
        'en': 'Delivery Motorbike',
        'ar': 'دراجة التوصيل',
        'fr': 'Moto Livraison'
    },
    {
        'msgid': 'Médina, Fès • 32 km/h',
        'en': 'Medina, Fez • 32 km/h',
        'ar': 'المدينة القديمة، فاس • 32 كم/س',
        'fr': 'Médina, Fès • 32 km/h'
    },
    {
        'msgid': 'NEW',
        'en': 'NEW',
        'ar': 'جديد',
        'fr': 'NOUVEAU'
    },
    {
        'msgid': 'PRO',
        'en': 'PRO',
        'ar': 'احترافي',
        'fr': 'PRO'
    },
    {
        'msgid': 'Volvo FH16',
        'en': 'Volvo FH16',
        'ar': 'فولفو FH16',
        'fr': 'Volvo FH16'
    },
    {
        'msgid': 'Volvo FH16 (Flotte Fès)',
        'en': 'Volvo FH16 (Fez Fleet)',
        'ar': 'فولفو FH16 (أسطول فاس)',
        'fr': 'Volvo FH16 (Flotte Fès)'
    },
    {
        'msgid': 'Traceur OBD-II',
        'en': 'OBD-II Tracker',
        'ar': 'جهاز تتبع OBD-II',
        'fr': 'Traceur OBD-II'
    },
    {
        'msgid': 'Traceur Filaire (Hardwired)',
        'en': 'Hardwired Tracker',
        'ar': 'جهاز تتبع سلكي',
        'fr': 'Traceur Filaire (Hardwired)'
    },
    {
        'msgid': 'Traceur Magnétique Autonome',
        'en': 'Standalone Magnetic Tracker',
        'ar': 'جهاز تتبع مغناطيسي مستقل',
        'fr': 'Traceur Magnétique Autonome'
    },
    {
        'msgid': 'Traceur Personnel / Portatif',
        'en': 'Personal / Portable Tracker',
        'ar': 'جهاز تتبع شخصي / محمول',
        'fr': 'Traceur Personnel / Portatif'
    },
    {
        'msgid': 'Capteur & Accessoire',
        'en': 'Sensor & Accessory',
        'ar': 'مستشعر وملحقات',
        'fr': 'Capteur & Accessoire'
    },
    {
        'msgid': 'Fermé',
        'en': 'Closed',
        'ar': 'مغلق',
        'fr': 'Fermé'
    },
    {
        'msgid': 'Suivant',
        'en': 'Next',
        'ar': 'التالي',
        'fr': 'Suivant'
    },
    {
        'msgid': 'Précédent',
        'en': 'Previous',
        'ar': 'السابق',
        'fr': 'Précédent'
    },
    {
        'msgid': 'Langue',
        'en': 'Language',
        'ar': 'اللغة',
        'fr': 'Langue'
    },
    {
        'msgid': 'Aperçu en Direct',
        'en': 'Live Preview',
        'ar': 'معاينة حية',
        'fr': 'Aperçu en Direct'
    },
    {
        'msgid': 'Compatible iOS 13+ & Android 8+ • Notifications Push en temps réel',
        'en': 'Compatible with iOS 13+ & Android 8+ • Real-time push notifications',
        'ar': 'متوافق مع iOS 13+ وأندرويد 8+ • إشعارات فورية في الوقت الفعلي',
        'fr': 'Compatible iOS 13+ & Android 8+ • Notifications Push en temps réel'
    },
    {
        'msgid': 'Jeton OTP :',
        'en': 'OTP Token:',
        'ar': 'رمز OTP :',
        'fr': 'Jeton OTP :'
    },
    {
        'msgid': "Laissez vide si la double authentification (2FA) n'a pas encore été configurée pour votre compte.",
        'en': 'Leave blank if two-factor authentication (2FA) is not yet configured for your account.',
        'ar': 'اتركه فارغاً إذا لم يتم إعداد المصادقة الثنائية (2FA) لحسابك بعد.',
        'fr': "Laissez vide si la double authentification (2FA) n'a pas encore été configurée pour votre compte."
    },
    {
        'msgid': 'Log in',
        'en': 'Log in',
        'ar': 'تسجيل الدخول',
        'fr': 'Se connecter'
    },
    {
        'msgid': 'OTP Device:',
        'en': 'OTP Device:',
        'ar': 'جهاز OTP :',
        'fr': 'Appareil OTP :'
    },
    {
        'msgid': 'Get OTP Challenge',
        'en': 'Get OTP Challenge',
        'ar': 'الحصول على تحدي OTP',
        'fr': 'Obtenir le défi OTP'
    },
    {
        'msgid': 'Please correct the error below.',
        'en': 'Please correct the error below.',
        'ar': 'يرجى تصحيح الخطأ أدناه.',
        'fr': 'Veuillez corriger l’erreur ci-dessous.'
    },
    {
        'msgid': 'Please correct the errors below.',
        'en': 'Please correct the errors below.',
        'ar': 'يرجى تصحيح الأخطاء أدناه.',
        'fr': 'Veuillez corriger les erreurs ci-dessous.'
    },
    {
        'msgid': 'Forgotten your password or username?',
        'en': 'Forgotten your password or username?',
        'ar': 'هل نسيت كلمة المرور أو اسم المستخدم؟',
        'fr': 'Mot de passe ou identifiant oublié ?'
    }
]

import os, re

for lang in ['en', 'ar', 'fr']:
    po_path = f'locale/{lang}/LC_MESSAGES/django.po'
    po = polib.pofile(po_path)
    existing_ids = {e.msgid: e for e in po}
    
    added_count = 0
    updated_count = 0
    for item in new_translations:
        msgid = item['msgid']
        translation = item[lang]
        if msgid in existing_ids:
            entry = existing_ids[msgid]
            if not entry.msgstr or entry.msgstr == msgid and lang != 'fr':
                entry.msgstr = translation
                updated_count += 1
        else:
            entry = polib.POEntry(
                msgid=msgid,
                msgstr=translation,
            )
            po.append(entry)
            existing_ids[msgid] = entry
            added_count += 1
            
    if lang == 'fr':
        for root, dirs, files in os.walk('templates'):
            for f in files:
                if f.endswith('.html'):
                    with open(os.path.join(root, f), 'r', encoding='utf-8') as fh:
                        matches = re.findall(r'{%\s*trans\s+[\'"](.*?)[\'"]\s*%}', fh.read())
                        for m in matches:
                            if m not in existing_ids:
                                po.append(polib.POEntry(msgid=m, msgstr=m))
                                existing_ids[m] = m
                                added_count += 1
    
    po.save()
    mo_path = f'locale/{lang}/LC_MESSAGES/django.mo'
    po.save_as_mofile(mo_path)
    print(f"[{lang}] Added: {added_count}, Updated: {updated_count}, Total: {len(po)} -> saved MO")
