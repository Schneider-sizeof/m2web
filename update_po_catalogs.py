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
    },
    {
        'msgid': 'GPS EN DIRECT',
        'en': 'LIVE GPS',
        'ar': 'تتبع مباشر GPS',
        'fr': 'GPS EN DIRECT'
    },
    {
        'msgid': 'Carte & Flotte Temps Réel',
        'en': 'Real-Time Map & Fleet',
        'ar': 'خريطة وتتبع الأسطول المباشر',
        'fr': 'Carte & Flotte Temps Réel'
    },
    {
        'msgid': 'Fès • Casablanca • Tanger',
        'en': 'Fez • Casablanca • Tangier',
        'ar': 'فاس • الدار البيضاء • طنجة',
        'fr': 'Fès • Casablanca • Tanger'
    },
    {
        'msgid': 'Autoroute A2 • Vers Rabat',
        'en': 'Highway A2 • Towards Rabat',
        'ar': 'الطريق السيار A2 • باتجاه الرباط',
        'fr': 'Autoroute A2 • Vers Rabat'
    },
    {
        'msgid': 'Réservoir: 78%',
        'en': 'Tank: 78%',
        'ar': 'الخزان: 78%',
        'fr': 'Réservoir: 78%'
    },
    {
        'msgid': 'Conso: 31L/100',
        'en': 'Consumption: 31L/100',
        'ar': 'الاستهلاك: 31 لتر/100',
        'fr': 'Conso: 31L/100'
    },
    {
        'msgid': 'Dacia Duster',
        'en': 'Dacia Duster',
        'ar': 'داسيا داستر',
        'fr': 'Dacia Duster'
    },
    {
        'msgid': 'Contact ON',
        'en': 'Ignition ON',
        'ar': 'المحرك مشتغل',
        'fr': 'Contact ON'
    },
    {
        'msgid': 'Zone Industrielle Dokkarat, Fès',
        'en': 'Dokkarat Industrial Zone, Fez',
        'ar': 'الحي الصناعي الدكارات، فاس',
        'fr': 'Zone Industrielle Dokkarat, Fès'
    },
    {
        'msgid': 'Antivol & Coupure Moteur Prêts',
        'en': 'Anti-theft & Engine Cut-off Ready',
        'ar': 'نظام مضاد للسرقة وقطع المحرك جاهز',
        'fr': 'Antivol & Coupure Moteur Prêts'
    },
    {
        'msgid': 'Suivi cartographique haute précision en temps réel',
        'en': 'High-precision real-time map tracking',
        'ar': 'تتبع خرائطي عالي الدقة في الوقت الفعلي',
        'fr': 'Suivi cartographique haute précision en temps réel'
    },
    {
        'msgid': 'SONDE CARBURANT',
        'en': 'FUEL SENSOR',
        'ar': 'مستشعر الوقود',
        'fr': 'SONDE CARBURANT'
    },
    {
        'msgid': 'Contrôle Carburant Précis',
        'en': 'Precise Fuel Monitoring',
        'ar': 'مراقبة دقيقة للوقود',
        'fr': 'Contrôle Carburant Précis'
    },
    {
        'msgid': 'Précision capacitive à 99%',
        'en': '99% capacitive accuracy',
        'ar': 'دقة سعوية تصل إلى 99%',
        'fr': 'Précision capacitive à 99%'
    },
    {
        'msgid': 'Niveau actuel du réservoir',
        'en': 'Current fuel tank level',
        'ar': 'المستوى الحالي للخزان',
        'fr': 'Niveau actuel du réservoir'
    },
    {
        'msgid': 'Plein validé : +180L',
        'en': 'Refuel validated: +180L',
        'ar': 'تعبئة مؤكدة: +180 لتر',
        'fr': 'Plein validé : +180L'
    },
    {
        'msgid': 'Station Afriquia Fès Sud • 10:14',
        'en': 'Afriquia Station Fez South • 10:14',
        'ar': 'محطة أفريقيا فاس الجنوب • 10:14',
        'fr': 'Station Afriquia Fès Sud • 10:14'
    },
    {
        'msgid': 'Alerte vol & siphonage activée',
        'en': 'Fuel theft & siphoning alert active',
        'ar': 'تنبيه سرقة وشفط الوقود مفعّل',
        'fr': 'Alerte vol & siphonage activée'
    },
    {
        'msgid': 'Mise à jour toutes les 10 secondes',
        'en': 'Updated every 10 seconds',
        'ar': 'تحديث كل 10 ثوانٍ',
        'fr': 'Mise à jour toutes les 10 secondes'
    },
    {
        'msgid': 'Détection immédiate des pleins et siphonnages',
        'en': 'Immediate detection of refuels and theft',
        'ar': 'كشف فوري لتعبئة وشفط الوقود',
        'fr': 'Détection immédiate des pleins et siphonnages'
    },
    {
        'msgid': 'RAPPORTS & ÉCO-CONDUITE',
        'en': 'REPORTS & ECO-DRIVING',
        'ar': 'تقارير والقيادة الاقتصادية',
        'fr': 'RAPPORTS & ÉCO-CONDUITE'
    },
    {
        'msgid': 'Score Chauffeurs & Trajets',
        'en': 'Driver Score & Trips',
        'ar': 'تقييم السائقين والرحلات',
        'fr': 'Score Chauffeurs & Trajets'
    },
    {
        'msgid': 'Historique 12 mois complet',
        'en': 'Full 12-month history',
        'ar': 'سجل كامل لمدة 12 شهراً',
        'fr': 'Historique 12 mois complet'
    },
    {
        'msgid': "Kilométrage Aujourd'hui",
        'en': 'Mileage Today',
        'ar': 'المسافة المقطوعة اليوم',
        'fr': "Kilométrage Aujourd'hui"
    },
    {
        'msgid': 'Vitesse Maximale',
        'en': 'Top Speed',
        'ar': 'السرعة القصوى',
        'fr': 'Vitesse Maximale'
    },
    {
        'msgid': 'Temps de Conduite',
        'en': 'Driving Time',
        'ar': 'وقت السياقة',
        'fr': 'Temps de Conduite'
    },
    {
        'msgid': 'Arrêts & Pauses',
        'en': 'Stops & Breaks',
        'ar': 'التوقفات والاستراحات',
        'fr': 'Arrêts & Pauses'
    },
    {
        'msgid': '3 arrêts (45min)',
        'en': '3 stops (45min)',
        'ar': '3 توقفات (45 دقيقة)',
        'fr': '3 arrêts (45min)'
    },
    {
        'msgid': 'Rapports PDF & Excel exportables',
        'en': 'Exportable PDF & Excel reports',
        'ar': 'تقارير قابلة للتصدير بصيغة PDF و Excel',
        'fr': 'Rapports PDF & Excel exportables'
    },
    {
        'msgid': 'Analyses complètes et export de rapports détaillés',
        'en': 'Comprehensive analysis and detailed report export',
        'ar': 'تحليلات شاملة وتصدير تقارير مفصلة',
        'fr': 'Analyses complètes et export de rapports détaillés'
    },
    {
        'msgid': 'DH',
        'en': 'DH',
        'ar': 'درهم',
        'fr': 'DH'
    },
    {
        'msgid': 'DH / mois',
        'en': 'DH / month',
        'ar': 'درهم / شهر',
        'fr': 'DH / mois'
    },
    {
        'msgid': 'DH / an',
        'en': 'DH / year',
        'ar': 'درهم / سنة',
        'fr': 'DH / an'
    },
    {
        'msgid': 'DH (paiement unique)',
        'en': 'DH (one-time payment)',
        'ar': 'درهم (دفعة واحدة)',
        'fr': 'DH (paiement unique)'
    },
    {
        'msgid': 'Par mois',
        'en': 'Per month',
        'ar': 'شهرياً',
        'fr': 'Par mois'
    },
    {
        'msgid': 'Par an',
        'en': 'Per year',
        'ar': 'سنوياً',
        'fr': 'Par an'
    },
    {
        'msgid': 'Paiement unique',
        'en': 'One-time payment',
        'ar': 'دفعة واحدة',
        'fr': 'Paiement unique'
    },
    {
        'msgid': 'Vidéo Démo',
        'en': 'Demo Video',
        'ar': 'فيديو توضيحي',
        'fr': 'Vidéo Démo'
    },
    {
        'msgid': 'Voir la vidéo',
        'en': 'Watch Video',
        'ar': 'مشاهدة الفيديو',
        'fr': 'Voir la vidéo'
    },
    {
        'msgid': 'Démonstration Vidéo',
        'en': 'Video Demonstration',
        'ar': 'عرض توضيحي بالفيديو',
        'fr': 'Démonstration Vidéo'
    },
    {
        'msgid': "Découvrez l'Application en Action",
        'en': 'Discover the App in Action',
        'ar': 'اكتشف التطبيق أثناء العمل',
        'fr': "Découvrez l'Application en Action"
    },
    {
        'msgid': 'Regardez notre vidéo de présentation pour voir le suivi en temps réel et les fonctionnalités clés.',
        'en': 'Watch our presentation video to see real-time tracking and key features.',
        'ar': 'شاهد فيديو العرض التقديمي للاطلاع على التتبع في الوقت الفعلي والميزات الأساسية.',
        'fr': 'Regardez notre vidéo de présentation pour voir le suivi en temps réel et les fonctionnalités clés.'
    },
    {
        'msgid': 'Vidéo de présentation M2web GPS',
        'en': 'M2web GPS presentation video',
        'ar': 'فيديو تقديمي لتطبيق M2web GPS',
        'fr': 'Vidéo de présentation M2web GPS'
    },
    {
        'msgid': 'Voir la Démo Vidéo',
        'en': 'Watch Demo Video',
        'ar': 'مشاهدة العرض التوضيحي',
        'fr': 'Voir la Démo Vidéo'
    },
    {
        'msgid': 'Ouvrir la vidéo sur YouTube',
        'en': 'Open video on YouTube',
        'ar': 'فتح الفيديو على يوتيوب',
        'fr': 'Ouvrir la vidéo sur YouTube'
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
