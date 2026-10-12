#!/usr/bin/env python3
"""
Complete translation seeder for M2web Maroc — Contabo VPS.
Fills ALL untranslated AR/EN fields for every model in the database.
Run on the VPS: python fill_all_translations.py
"""
import os, sys

# Auto-detect environment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.contabo')

import django
django.setup()

from apps.core.models import CompanyInfo, WhyChooseUsPillar, Testimonial, Promotion, MobileApp, AppFeature, AppScreenshot, AppPlan
from apps.services.models import Service, Product
from apps.blog.models import Category, BlogPost
from apps.wholesale.models import ResellerTier


def fill_company():
    c = CompanyInfo.objects.first()
    if not c:
        print("No CompanyInfo found")
        return

    translations = {
        # Tagline
        'tagline_fr': 'Solutions Avancées de Géolocalisation & Gestion de Flotte',
        'tagline_en': 'Advanced Geolocation & Fleet Management Solutions',
        'tagline_ar': 'حلول متقدمة لتتبع المواقع وإدارة الأساطيل',

        # Topbar
        'topbar_badge_fr': 'Fournisseur Agréé',
        'topbar_badge_en': 'Certified Supplier',
        'topbar_badge_ar': 'مزود معتمد',
        'topbar_warranty_fr': 'Garantie & Support Direct',
        'topbar_warranty_en': 'Warranty & Direct Support',
        'topbar_warranty_ar': 'ضمان ودعم مباشر',

        # Operating Hours
        'operating_hours_weekday_fr': '08:30 – 18:30',
        'operating_hours_weekday_en': '08:30 AM – 06:30 PM',
        'operating_hours_weekday_ar': '08:30 – 18:30',
        'operating_hours_saturday_fr': '08:30 – 13:30',
        'operating_hours_saturday_en': '08:30 AM – 01:30 PM',
        'operating_hours_saturday_ar': '08:30 – 13:30',
        'operating_hours_sunday_fr': 'Fermé',
        'operating_hours_sunday_en': 'Closed',
        'operating_hours_sunday_ar': 'مغلق',

        # Hero Section
        'hero_badge_fr': 'N°1 de la Géolocalisation & Télématique au Maroc',
        'hero_badge_en': '#1 in Geolocation & Telematics in Morocco',
        'hero_badge_ar': 'الرائد في تتبع المواقع والتليماتيك بالمغرب',
        'hero_title_line1_fr': 'Prenez le Contrôle',
        'hero_title_line1_en': 'Take Full Control',
        'hero_title_line1_ar': 'تحكم الكامل',
        'hero_title_highlight_fr': 'Total de Votre Flotte',
        'hero_title_highlight_en': 'Of Your Fleet',
        'hero_title_highlight_ar': 'في أسطولك',
        'hero_title_line2_fr': 'en Temps Réel',
        'hero_title_line2_en': 'in Real Time',
        'hero_title_line2_ar': 'في الوقت الفعلي',
        'hero_subtitle_fr': 'Fournisseur direct de traceurs GPS 4G & solutions télématiques avancées à Fès et partout au Maroc. Réduisez vos coûts de carburant de 20%, protégez vos véhicules contre le vol et suivez vos actifs 24/7 sur smartphone & PC.',
        'hero_subtitle_en': 'Direct supplier of 4G GPS trackers & advanced telematics solutions in Fez and across Morocco. Reduce fuel costs by 20%, protect your vehicles from theft, and track your assets 24/7 on smartphone & PC.',
        'hero_subtitle_ar': 'مزود مباشر لأجهزة تتبع GPS 4G وحلول التليماتيك المتقدمة في فاس وعبر المغرب. خفض تكاليف الوقود بنسبة 20%، حماية مركباتك من السرقة، وتتبع أصولك على مدار الساعة عبر الهاتف والحاسوب.',
        'hero_trust_badge_1_fr': 'Traceurs 4G Certifiés',
        'hero_trust_badge_1_en': 'Certified 4G Trackers',
        'hero_trust_badge_1_ar': 'أجهزة تتبع 4G معتمدة',
        'hero_trust_badge_2_fr': 'Installation sur Site',
        'hero_trust_badge_2_en': 'On-Site Installation',
        'hero_trust_badge_2_ar': 'تركيب في الموقع',
        'hero_trust_badge_3_fr': 'Support 24/7 à Fès',
        'hero_trust_badge_3_en': '24/7 Support in Fez',
        'hero_trust_badge_3_ar': 'دعم على مدار الساعة في فاس',

        # Stats
        'stat_trackers_label_fr': 'Trackers Installés',
        'stat_trackers_label_en': 'Trackers Installed',
        'stat_trackers_label_ar': 'أجهزة تتبع مثبتة',
        'stat_fleets_label_fr': 'Flottes Gérées',
        'stat_fleets_label_en': 'Managed Fleets',
        'stat_fleets_label_ar': 'أساطيل مدارة',
        'stat_uptime_label_fr': 'Disponibilité Serveurs',
        'stat_uptime_label_en': 'Server Uptime',
        'stat_uptime_label_ar': 'جاهزية الخوادم',
        'stat_experience_label_fr': "Années d'Expertise à Fès",
        'stat_experience_label_en': 'Years of Expertise in Fez',
        'stat_experience_label_ar': 'سنوات خبرة في فاس',

        # B2B Banner
        'b2b_banner_badge_fr': 'ESPACE REVENDEURS & GROSSISTES',
        'b2b_banner_badge_en': 'RESELLERS & WHOLESALERS AREA',
        'b2b_banner_badge_ar': 'فضاء الموزعين وتجار الجملة',
        'b2b_banner_title_fr': 'Vous êtes installateur, intégrateur ou revendeur ?',
        'b2b_banner_title_en': 'Are you an installer, integrator, or reseller?',
        'b2b_banner_title_ar': 'هل أنت مركّب أو موزع أو بائع؟',
        'b2b_banner_desc_fr': "Bénéficiez de tarifs grossiste préférentiels, d'un stock disponible immédiatement à Fès et d'un support technique d'experts pour développer votre activité au Maroc.",
        'b2b_banner_desc_en': 'Benefit from preferential wholesale pricing, immediately available stock in Fez, and expert technical support to grow your business across Morocco.',
        'b2b_banner_desc_ar': 'استفد من أسعار الجملة التفضيلية ومخزون متوفر فوراً في فاس ودعم تقني متخصص لتطوير نشاطك التجاري في جميع أنحاء المغرب.',

        # About Page
        'about_story_title_fr': 'Notre Histoire & Mission',
        'about_story_title_en': 'Our Story & Mission',
        'about_story_title_ar': 'قصتنا ومهمتنا',
        'about_lead_fr': 'Basée à Fès, M2web Maroc est une entreprise technologique spécialisée dans les solutions de géolocalisation et la gestion de flotte.',
        'about_lead_en': 'Based in Fez, M2web Morocco is a technology company specializing in geolocation solutions and fleet management.',
        'about_lead_ar': 'مقرها في فاس، M2web المغرب شركة تكنولوجية متخصصة في حلول تتبع المواقع وإدارة الأساطيل.',
        'about_text_fr': "Depuis notre création, nous nous sommes engagés à fournir à nos clients des outils fiables, précis et faciles à utiliser pour optimiser leurs opérations logistiques. Notre mission est d'accompagner les entreprises marocaines dans leur transformation numérique en leur offrant une visibilité totale sur leurs actifs mobiles.",
        'about_text_en': "Since our founding, we have been committed to providing our clients with reliable, accurate, and easy-to-use tools to optimize their logistics operations. Our mission is to support Moroccan businesses in their digital transformation by offering complete visibility over their mobile assets.",
        'about_text_ar': 'منذ تأسيسنا، التزمنا بتوفير أدوات موثوقة ودقيقة وسهلة الاستخدام لعملائنا لتحسين عملياتهم اللوجستية. مهمتنا هي مرافقة الشركات المغربية في تحولها الرقمي من خلال منحها رؤية شاملة على أصولها المتنقلة.',

        # Meta SEO
        'meta_description_fr': 'M2web Maroc — Fournisseur N°1 de solutions GPS et gestion de flotte à Fès. Traceurs GPS en gros et au détail, installation et support technique.',
        'meta_description_en': 'M2web Morocco — Leading provider of GPS tracking & fleet management solutions in Fez and across Morocco. Wholesale & retail trackers, installation & tech support.',
        'meta_description_ar': 'M2web المغرب — المزود الرائد لحلول تتبع المركبات GPS وإدارة الأساطيل في فاس وجميع أنحاء المغرب. بيع بالجملة والتقسيط مع التركيب والدعم الفني.',

        # Nav Buttons
        'login_button_text_fr': 'Connexion',
        'login_button_text_en': 'Login',
        'login_button_text_ar': 'تسجيل الدخول',
        'login_button_title_fr': 'Connexion Plateforme Trackmaroc',
        'login_button_title_en': 'Login to Trackmaroc Platform',
        'login_button_title_ar': 'تسجيل الدخول إلى منصة Trackmaroc',
        'quote_button_text_fr': 'Demander un Devis',
        'quote_button_text_en': 'Request a Quote',
        'quote_button_text_ar': 'طلب عرض سعر',
    }

    for field, value in translations.items():
        setattr(c, field, value)
    c.save()
    print("✅ CompanyInfo — ALL fields translated (FR/EN/AR)")


def fill_mobile_app():
    app = MobileApp.objects.first()
    if not app:
        print("No MobileApp found")
        return

    translations = {
        'tagline_fr': 'Suivez votre flotte en temps réel depuis votre smartphone',
        'tagline_en': 'Track your fleet in real time from your smartphone',
        'tagline_ar': 'تتبع أسطولك في الوقت الفعلي من هاتفك الذكي',
        'hero_title_fr': 'Application Mobile GPS',
        'hero_title_en': 'GPS Mobile Application',
        'hero_title_ar': 'تطبيق الهاتف للتتبع GPS',
        'hero_subtitle_fr': "Téléchargez notre application de suivi GPS et gardez un œil sur vos véhicules 24/7, où que vous soyez.",
        'hero_subtitle_en': "Download our GPS tracking app and keep an eye on your vehicles 24/7, wherever you are.",
        'hero_subtitle_ar': 'حمّل تطبيقنا لتتبع GPS وراقب مركباتك على مدار الساعة أينما كنت.',
        'description_fr': "Notre application mobile M2web GPS Tracker vous offre un contrôle total sur votre flotte depuis votre smartphone Android. Interface intuitive, notifications en temps réel, et rapports détaillés à portée de main.",
        'description_en': "Our M2web GPS Tracker mobile app gives you complete control over your fleet from your Android smartphone. Intuitive interface, real-time notifications, and detailed reports at your fingertips.",
        'description_ar': 'يمنحك تطبيق M2web GPS Tracker تحكماً كاملاً في أسطولك من هاتفك الذكي أندرويد. واجهة بديهية وإشعارات فورية وتقارير مفصلة في متناول يدك.',
        'features_title_fr': 'Fonctionnalités Clés',
        'features_title_en': 'Key Features',
        'features_title_ar': 'الميزات الرئيسية',
        'features_subtitle_fr': 'Tout ce dont vous avez besoin pour gérer votre flotte depuis votre poche.',
        'features_subtitle_en': 'Everything you need to manage your fleet from your pocket.',
        'features_subtitle_ar': 'كل ما تحتاجه لإدارة أسطولك من جيبك.',
        'cta_title_fr': 'Prêt à Prendre le Contrôle ?',
        'cta_title_en': 'Ready to Take Control?',
        'cta_title_ar': 'مستعد للتحكم الكامل؟',
        'cta_subtitle_fr': "Téléchargez l'application gratuitement et commencez à suivre vos véhicules en quelques minutes.",
        'cta_subtitle_en': "Download the app for free and start tracking your vehicles in minutes.",
        'cta_subtitle_ar': 'حمّل التطبيق مجاناً وابدأ بتتبع مركباتك خلال دقائق.',
    }

    for field, value in translations.items():
        setattr(app, field, value)
    app.save()
    print("✅ MobileApp — ALL fields translated")


def fill_app_features():
    features_data = [
        {
            'title_fr': 'Suivi en Temps Réel', 'title_en': 'Real-Time Tracking', 'title_ar': 'تتبع في الوقت الفعلي',
            'desc_fr': 'Localisez vos véhicules instantanément sur la carte avec mise à jour toutes les 10 secondes.',
            'desc_en': 'Locate your vehicles instantly on the map with updates every 10 seconds.',
            'desc_ar': 'حدد مواقع مركباتك فوراً على الخريطة مع تحديثات كل 10 ثوانٍ.',
        },
        {
            'title_fr': 'Historique des Trajets', 'title_en': 'Trip History', 'title_ar': 'سجل الرحلات',
            'desc_fr': 'Consultez les parcours passés avec tous les arrêts, distances et durées de conduite.',
            'desc_en': 'View past trips with all stops, distances, and driving durations.',
            'desc_ar': 'استعرض الرحلات السابقة مع جميع نقاط التوقف والمسافات ومدد القيادة.',
        },
        {
            'title_fr': 'Alertes & Notifications', 'title_en': 'Alerts & Notifications', 'title_ar': 'التنبيهات والإشعارات',
            'desc_fr': 'Recevez des alertes de vitesse, géo-clôture, démarrage moteur et anti-sabotage.',
            'desc_en': 'Receive alerts for speeding, geofence crossings, engine start, and anti-tampering.',
            'desc_ar': 'تلقَّ تنبيهات السرعة والسياج الجغرافي وتشغيل المحرك ومحاولات العبث.',
        },
        {
            'title_fr': 'Rapports Détaillés', 'title_en': 'Detailed Reports', 'title_ar': 'تقارير مفصلة',
            'desc_fr': 'Rapports de conduite, consommation et activité exportables en PDF.',
            'desc_en': 'Driving, consumption, and activity reports exportable in PDF.',
            'desc_ar': 'تقارير القيادة والاستهلاك والنشاط قابلة للتصدير بصيغة PDF.',
        },
        {
            'title_fr': 'Coupure Moteur à Distance', 'title_en': 'Remote Engine Cutoff', 'title_ar': 'قطع المحرك عن بعد',
            'desc_fr': "Immobilisez votre véhicule à distance en cas de vol ou d'urgence directement depuis l'app.",
            'desc_en': "Immobilize your vehicle remotely in case of theft or emergency directly from the app.",
            'desc_ar': 'أوقف محرك مركبتك عن بعد في حالة السرقة أو الطوارئ مباشرة من التطبيق.',
        },
        {
            'title_fr': 'Multi-Véhicules', 'title_en': 'Multi-Vehicle', 'title_ar': 'إدارة عدة مركبات',
            'desc_fr': 'Gérez l\'ensemble de votre flotte depuis une seule interface mobile.',
            'desc_en': 'Manage your entire fleet from a single mobile interface.',
            'desc_ar': 'أدر أسطولك بالكامل من واجهة هاتف واحدة.',
        },
    ]

    for i, data in enumerate(features_data):
        try:
            feat = AppFeature.objects.all().order_by('order', 'pk')[i]
            feat.title_fr = data['title_fr']
            feat.title_en = data['title_en']
            feat.title_ar = data['title_ar']
            feat.description_fr = data['desc_fr']
            feat.description_en = data['desc_en']
            feat.description_ar = data['desc_ar']
            feat.save()
            print(f"  ✅ AppFeature {feat.pk}: {data['title_fr']}")
        except IndexError:
            break
    print("✅ AppFeatures translated")


def fill_app_plans():
    plans_data = [
        {
            'name_fr': 'Essai Gratuit', 'name_en': 'Free Trial', 'name_ar': 'تجربة مجانية',
            'badge_fr': '', 'badge_en': '', 'badge_ar': '',
            'desc_fr': 'Testez gratuitement pendant 7 jours', 'desc_en': 'Try free for 7 days', 'desc_ar': 'جرّب مجاناً لمدة 7 أيام',
            'features_fr': "Suivi temps réel\nHistorique 24h\n1 véhicule",
            'features_en': "Real-time tracking\n24h history\n1 vehicle",
            'features_ar': "تتبع في الوقت الفعلي\nسجل 24 ساعة\nمركبة واحدة",
            'max_vehicles_fr': '1 véhicule', 'max_vehicles_en': '1 vehicle', 'max_vehicles_ar': 'مركبة واحدة',
            'cta_text_fr': 'Essai Gratuit', 'cta_text_en': 'Free Trial', 'cta_text_ar': 'تجربة مجانية',
        },
        {
            'name_fr': 'Essentiel', 'name_en': 'Essential', 'name_ar': 'الأساسي',
            'badge_fr': '', 'badge_en': '', 'badge_ar': '',
            'desc_fr': 'Pour les particuliers et petites flottes', 'desc_en': 'For individuals and small fleets', 'desc_ar': 'للأفراد والأساطيل الصغيرة',
            'features_fr': "Suivi temps réel\nHistorique 30 jours\nAlertes SMS\nRapports mensuels",
            'features_en': "Real-time tracking\n30-day history\nSMS alerts\nMonthly reports",
            'features_ar': "تتبع فوري\nسجل 30 يوم\nتنبيهات SMS\nتقارير شهرية",
            'max_vehicles_fr': '1-5 véhicules', 'max_vehicles_en': '1-5 vehicles', 'max_vehicles_ar': '1-5 مركبات',
            'cta_text_fr': 'Choisir ce forfait', 'cta_text_en': 'Choose this plan', 'cta_text_ar': 'اختر هذا الاشتراك',
        },
        {
            'name_fr': 'Professionnel', 'name_en': 'Professional', 'name_ar': 'احترافي',
            'badge_fr': 'POPULAIRE', 'badge_en': 'POPULAR', 'badge_ar': 'الأكثر طلباً',
            'desc_fr': 'Pour les flottes professionnelles', 'desc_en': 'For professional fleets', 'desc_ar': 'للأساطيل المهنية',
            'features_fr': "Tout du forfait Essentiel\nHistorique 90 jours\nCoupure moteur\nRapports avancés\nSupport prioritaire",
            'features_en': "Everything in Essential\n90-day history\nEngine cutoff\nAdvanced reports\nPriority support",
            'features_ar': "كل ما في الأساسي\nسجل 90 يوم\nقطع المحرك\nتقارير متقدمة\nدعم أولوي",
            'max_vehicles_fr': '5-50 véhicules', 'max_vehicles_en': '5-50 vehicles', 'max_vehicles_ar': '5-50 مركبة',
            'cta_text_fr': 'Choisir ce forfait', 'cta_text_en': 'Choose this plan', 'cta_text_ar': 'اختر هذا الاشتراك',
        },
    ]

    for i, data in enumerate(plans_data):
        try:
            plan = AppPlan.objects.all().order_by('order', 'pk')[i]
            for key, val in data.items():
                setattr(plan, key, val)
            plan.save()
            print(f"  ✅ AppPlan {plan.pk}: {data['name_fr']}")
        except IndexError:
            break
    print("✅ AppPlans translated")


def fill_app_screenshots():
    captions = [
        {'fr': 'Tableau de bord principal', 'en': 'Main Dashboard', 'ar': 'لوحة القيادة الرئيسية'},
        {'fr': 'Suivi en direct', 'en': 'Live Tracking', 'ar': 'التتبع المباشر'},
        {'fr': 'Historique des trajets', 'en': 'Trip History', 'ar': 'سجل الرحلات'},
        {'fr': 'Alertes et notifications', 'en': 'Alerts & Notifications', 'ar': 'التنبيهات والإشعارات'},
    ]
    for i, cap in enumerate(captions):
        try:
            ss = AppScreenshot.objects.all().order_by('order', 'pk')[i]
            ss.caption_fr = cap['fr']
            ss.caption_en = cap['en']
            ss.caption_ar = cap['ar']
            ss.save()
            print(f"  ✅ AppScreenshot {ss.pk}")
        except IndexError:
            break
    print("✅ AppScreenshots translated")


def fill_pillars():
    pillars_data = [
        {
            'title_fr': 'Réseau 4G Multi-Opérateur', 'title_en': 'Multi-Operator 4G Network', 'title_ar': 'شبكة 4G متعددة المشغلين',
            'desc_fr': "Connectivité maximale garantie grâce à nos cartes SIM M2M multi-opérateurs couvrant l'ensemble du territoire marocain sans coupure.",
            'desc_en': 'Guaranteed maximum connectivity with multi-operator M2M SIM cards covering all of Morocco without interruption.',
            'desc_ar': 'اتصال مستمر ومضمون بفضل شرائح SIM M2M متعددة المشغلين تغطي كافة التراب المغربي بدون انقطاع.',
        },
        {
            'title_fr': 'Application Mobile & Web', 'title_en': 'Mobile & Web Application', 'title_ar': 'تطبيق الهاتف والويب',
            'desc_fr': "Accédez à votre flotte 24h/24 et 7j/7 depuis votre smartphone ou navigateur avec une interface moderne et fluide.",
            'desc_en': 'Access your fleet 24/7 from your smartphone or web browser with a modern and fluid interface.',
            'desc_ar': 'تحكم في أسطولك على مدار الساعة 24/7 عبر هاتفك الذكي أو متصفح الويب بواجهة عصرية وسلسة.',
        },
        {
            'title_fr': 'Contrôle Carburant Anti-Vol', 'title_en': 'Anti-Theft Fuel Monitoring', 'title_ar': 'مراقبة الوقود ومكافحة السرقة',
            'desc_fr': 'Sondes de niveau haute précision pour détecter instantanément les chutes anormales, les vols et surveiller la consommation réelle.',
            'desc_en': 'High-precision level probes to instantly detect abnormal drops, fuel theft, and monitor actual consumption.',
            'desc_ar': 'مستشعرات دقيقة لمستوى الوقود لكشف أي انخفاض غير طبيعي وسرقة الوقود ومراقبة الاستهلاك الفعلي فورياً.',
        },
        {
            'title_fr': 'Installation & Support à Fès', 'title_en': 'Installation & Support in Fez', 'title_ar': 'التركيب والدعم في فاس',
            'desc_fr': 'Atelier dédié à Fès et équipe technique itinérante pour une installation soignée, rapide et un service après-vente de proximité.',
            'desc_en': 'Dedicated workshop in Fez and mobile technical team for fast, professional installation and responsive local support.',
            'desc_ar': 'ورشة متخصصة في فاس وفريق تقني متنقل لتركيب احترافي وسريع مع خدمة ما بعد البيع.',
        },
    ]
    for i, data in enumerate(pillars_data):
        try:
            p = WhyChooseUsPillar.objects.all().order_by('order', 'pk')[i]
            p.title_fr = data['title_fr']; p.title_en = data['title_en']; p.title_ar = data['title_ar']
            p.description_fr = data['desc_fr']; p.description_en = data['desc_en']; p.description_ar = data['desc_ar']
            p.save()
            print(f"  ✅ Pillar {p.pk}: {data['title_fr']}")
        except IndexError:
            break
    print("✅ Pillars translated")


def fill_testimonials():
    data = [
        {'role_fr': 'Directeur Général', 'role_en': 'General Manager', 'role_ar': 'المدير العام',
         'content_fr': 'M2web a transformé la gestion de notre flotte de 45 camions. Le suivi en temps réel et les alertes de consommation nous ont permis de réduire nos coûts carburant de 20%.',
         'content_en': 'M2web transformed the management of our 45-truck fleet. Real-time tracking and consumption alerts allowed us to reduce our fuel costs by 20%.',
         'content_ar': 'غيرت M2web إدارة أسطولنا المكون من 45 شاحنة بالكامل. مكننا التتبع في الوقت الفعلي وتنبيهات الاستهلاك من خفض تكاليف الوقود بنسبة 20%.'},
        {'role_fr': 'Responsable Logistique', 'role_en': 'Logistics Manager', 'role_ar': 'مسؤولة اللوجستيك',
         'content_fr': "Service impeccable et support technique réactif. Les traceurs GPS 4G sont fiables et l'application mobile est très intuitive.",
         'content_en': 'Impeccable service and responsive technical support. The 4G GPS trackers are reliable and the mobile app is very intuitive.',
         'content_ar': 'خدمة لا تشوبها شائبة ودعم فني متجاوب للغاية. أجهزة التتبع 4G موثوقة جداً وتطبيق الهاتف سهل الاستخدام.'},
        {'role_fr': 'Gérant', 'role_en': 'Managing Director', 'role_ar': 'مسير شركة',
         'content_fr': 'Grâce à M2web, nous avons sécurisé notre parc de 80 véhicules de location. La coupure moteur à distance nous a sauvé plusieurs fois du vol.',
         'content_en': 'Thanks to M2web, we secured our fleet of 80 rental vehicles. The remote engine cutoff saved us from vehicle theft multiple times.',
         'content_ar': 'بفضل M2web أمّنا أسطولنا المكون من 80 سيارة كراء. ميزة قطع المحرك عن بعد أنقذتنا من السرقة في عدة مناسبات.'},
        {'role_fr': 'Directeur Technique', 'role_en': 'Technical Director', 'role_ar': 'المدير التقني',
         'content_fr': 'Les capteurs de température et le suivi de la chaîne du froid nous permettent de garantir la qualité de nos livraisons.',
         'content_en': 'Temperature sensors and cold chain monitoring allow us to guarantee delivery quality.',
         'content_ar': 'تتيح لنا مستشعرات الحرارة ومراقبة سلسلة التبريد ضمان جودة شحناتنا بدقة.'},
    ]
    for i, d in enumerate(data):
        try:
            t = Testimonial.objects.all().order_by('order', 'pk')[i]
            for k, v in d.items():
                setattr(t, k, v)
            t.save()
            print(f"  ✅ Testimonial {t.pk}: {t.client_name}")
        except IndexError:
            break
    print("✅ Testimonials translated")


def fill_services():
    data = [
        {'title_fr': 'Gestion de Flotte en Temps Réel', 'title_en': 'Real-Time Fleet Management', 'title_ar': 'إدارة الأساطيل في الوقت الفعلي',
         'desc_fr': 'Suivi en temps réel de votre flotte avec historique des trajets, alertes de vitesse, géo-clôtures et rapports détaillés.',
         'desc_en': 'Real-time fleet tracking with complete trip history, speed alerts, geofencing, and comprehensive reports.',
         'desc_ar': 'تتبع مباشر ولحظي لأسطولك مع سجل كامل للرحلات، تنبيهات السرعة، السياج الجغرافي وتقارير شاملة.'},
        {'title_fr': 'Contrôle Carburant & Éco-Conduite', 'title_en': 'Fuel Monitoring & Eco-Driving', 'title_ar': 'مراقبة الوقود والقيادة الاقتصادية',
         'desc_fr': 'Intégration de sondes de carburant pour auditer la consommation, détecter les vols de carburant et adopter une conduite économique.',
         'desc_en': 'Integration of high-precision fuel probes to audit consumption, detect fuel theft, and foster economical driving.',
         'desc_ar': 'دمج مستشعرات الوقود الدقيقة لتدقيق الاستهلاك، كشف السرقات، والتشجيع على القيادة الاقتصادية.'},
        {'title_fr': 'Sécurité & Coupure Moteur à Distance', 'title_en': 'Security & Remote Engine Cutoff', 'title_ar': 'الأمان وقطع المحرك عن بعد',
         'desc_fr': 'Protection antivol complète avec coupure du moteur à distance via SMS ou application mobile et alertes de remorquage.',
         'desc_en': 'Comprehensive anti-theft protection with remote engine shutdown via SMS or mobile app, and towing alerts.',
         'desc_ar': 'حماية شاملة ضد السرقة مع إمكانية إيقاف المحرك عن بعد عبر الرسائل القصيرة أو التطبيق وتنبيهات القطر.'},
        {'title_fr': 'Télématique & Chaîne du Froid', 'title_en': 'Telematics & Cold Chain Monitoring', 'title_ar': 'التتبع الذكي وسلسلة التبريد',
         'desc_fr': 'Capteurs de température pour le transport frigorifique garantissant le respect de la chaîne du froid avec alertes en temps réel.',
         'desc_en': 'Temperature sensors for refrigerated transport ensuring cold chain integrity with real-time temperature alerts.',
         'desc_ar': 'مستشعرات حرارة للنقل المبرد لضمان سلامة سلسلة التبريد مع تنبيهات فورية عند أي تغير في درجة الحرارة.'},
        {'title_fr': 'Installation & Support Technique', 'title_en': 'Professional Installation & Support', 'title_ar': 'التركيب والدعم التقني المتخصص',
         'desc_fr': 'Notre atelier à Fès et nos techniciens itinérants assurent une installation professionnelle et un support technique sur tout le Maroc.',
         'desc_en': 'Our dedicated workshop in Fez and mobile technicians provide professional installation and technical support across Morocco.',
         'desc_ar': 'تضمن ورشتنا في فاس وفرقنا المتنقلة تركيباً احترافياً ودعماً تقنياً متميزاً في جميع أنحاء المغرب.'},
    ]
    for i, d in enumerate(data):
        try:
            s = Service.objects.all().order_by('order', 'pk')[i]
            s.title_fr = d['title_fr']; s.title_en = d['title_en']; s.title_ar = d['title_ar']
            s.description_fr = d['desc_fr']; s.description_en = d['desc_en']; s.description_ar = d['desc_ar']
            s.save()
            print(f"  ✅ Service {s.pk}: {d['title_fr']}")
        except IndexError:
            break
    print("✅ Services translated")


def fill_products():
    data = [
        {'name_fr': 'Traceur GPS 4G OBD-II', 'name_en': '4G OBD-II GPS Tracker', 'name_ar': 'جهاز تتبع GPS 4G لمنفذ OBD-II',
         'desc_fr': 'Traceur GPS OBD-II plug & play avec connectivité 4G LTE, suivi en temps réel et lecture des données véhicule.',
         'desc_en': 'Plug & play OBD-II GPS tracker with 4G LTE connectivity, real-time tracking, and vehicle diagnostics.',
         'desc_ar': 'جهاز تتبع OBD-II سهل التركيب والتوصيل المباشر مع اتصال 4G LTE، تتبع فوري وتشخيص ذكي.',
         'specs_fr': "4G LTE\nOBD-II Port\nGPS + GLONASS + BeiDou\nAccéléromètre intégré\nApplication mobile iOS & Android",
         'specs_en': "4G LTE\nOBD-II Port\nGPS + GLONASS + BeiDou\nBuilt-in Accelerometer\niOS & Android Mobile App",
         'specs_ar': "4G LTE\nمنفذ OBD-II مباشر\nنظام GPS + GLONASS + BeiDou\nمستشعر تسارع مدمج\nتطبيق iOS وأندرويد",
         'price_fr': '450 - 600 MAD', 'price_en': '450 - 600 MAD', 'price_ar': '450 - 600 درهم'},
        {'name_fr': 'Traceur GPS 4G Filaire', 'name_en': '4G Hardwired GPS Tracker', 'name_ar': 'جهاز تتبع GPS 4G سلكي احترافي',
         'desc_fr': 'Traceur GPS professionnel à installation filaire avec relais de coupure moteur et batterie de secours.',
         'desc_en': 'Professional hardwired GPS tracker with remote engine cutoff relay and integrated backup battery.',
         'desc_ar': 'جهاز تتبع احترافي بتركيب سلكي مخفي مع مرحل لقطع المحرك عن بعد وبطارية طوارئ مدمجة.',
         'specs_fr': "4G LTE\nInstallation filaire\nRelais coupure moteur\nBatterie de secours\nAntenne GPS haute sensibilité",
         'specs_en': "4G LTE\nHardwired installation\nEngine cutoff relay\nBackup battery\nHigh-sensitivity GPS antenna",
         'specs_ar': "4G LTE\nتركيب سلكي احترافي\nمرحل قطع المحرك\nبطارية طوارئ احتياطية\nهوائي GPS عالي الحساسية",
         'price_fr': '350 - 550 MAD', 'price_en': '350 - 550 MAD', 'price_ar': '350 - 550 درهم'},
        {'name_fr': 'Traceur GPS Magnétique Autonome', 'name_en': 'Standalone Magnetic GPS Tracker', 'name_ar': 'جهاز تتبع GPS مغناطيسي مستقل',
         'desc_fr': 'Traceur GPS autonome avec aimant puissant et batterie longue durée, idéal pour les conteneurs et remorques.',
         'desc_en': 'Standalone GPS tracker with powerful magnet and long-life battery, ideal for assets and trailers.',
         'desc_ar': 'جهاز تتبع مستقل بمغناطيس صناعي قوي وبطارية تدوم طويلاً، مثالي للمقطورات والحاويات.',
         'specs_fr': "4G LTE\nAimant puissant\nBatterie 5000mAh\nÉtanche IP67\nJusqu'à 90 jours d'autonomie",
         'specs_en': "4G LTE\nPowerful magnet\n5000mAh battery\nWaterproof IP67\nUp to 90 days battery life",
         'specs_ar': "4G LTE\nمغناطيس تثبيت قوي\nبطارية 5000 مللي أمبير\nمقاوم للماء IP67\nاستقلالية تدوم حتى 90 يوماً",
         'price_fr': '600 - 900 MAD', 'price_en': '600 - 900 MAD', 'price_ar': '600 - 900 درهم'},
        {'name_fr': 'Traceur Personnel / Asset Tracker', 'name_en': 'Personal & Asset Tracker', 'name_ar': 'جهاز تتبع شخصي وللأصول الثمينة',
         'desc_fr': 'Traceur GPS personnel compact avec bouton SOS, idéal pour les personnes et objets de valeur.',
         'desc_en': 'Compact personal GPS tracker with emergency SOS button, ideal for workers and valuable assets.',
         'desc_ar': 'جهاز تتبع شخصي مدمج وخفيف مزود بزر استغاثة SOS، مثالي للأشخاص والمقتنيات الثمينة.',
         'specs_fr': "4G LTE\nCompact et léger\nBouton SOS\nGéo-clôture\nHistorique de trajet",
         'specs_en': "4G LTE\nCompact & Lightweight\nSOS emergency button\nGeofencing\nTrip history",
         'specs_ar': "4G LTE\nتصميم مدمج وخفيف\nزر استغاثة SOS\nسياج جغرافي\nسجل مسارات الرحلات",
         'price_fr': '250 - 400 MAD', 'price_en': '250 - 400 MAD', 'price_ar': '250 - 400 درهم'},
        {'name_fr': 'Sonde Carburant Capacitive', 'name_en': 'Capacitive Fuel Level Sensor', 'name_ar': 'مستشعر وقود سعوي عالي الدقة',
         'desc_fr': 'Sonde de niveau carburant capacitive haute précision pour la surveillance de la consommation et la détection de vol.',
         'desc_en': 'High-precision capacitive fuel level sensor for real-time consumption monitoring and theft prevention.',
         'desc_ar': 'مستشعر سعوي فائق الدقة لقياس مستوى الوقود في الوقت الفعلي ورصد الاستهلاك ومكافحة السرقة.',
         'specs_fr': "Précision ±1%\nLongueur ajustable\nCompatible tous réservoirs\nSortie analogique\nRésistant aux hydrocarbures",
         'specs_en': "Accuracy ±1%\nAdjustable length\nCompatible with all tanks\nAnalog/Digital output\nHydrocarbon-resistant",
         'specs_ar': "دقة قياس ±1%\nطول قابل للتعديل\nمتوافق مع جميع الخزانات\nمخرج تناظري ورقمي\nمقاوم للهيدروكربونات",
         'price_fr': '800 - 1200 MAD', 'price_en': '800 - 1200 MAD', 'price_ar': '800 - 1200 درهم'},
        {'name_fr': 'Capteur de Température', 'name_en': 'Temperature Sensor', 'name_ar': 'مستشعر درجة الحرارة',
         'desc_fr': 'Capteur de température pour le monitoring de la chaîne du froid avec alertes en temps réel.',
         'desc_en': 'Temperature monitoring sensor for cold chain logistics with real-time temperature deviation alerts.',
         'desc_ar': 'مستشعر مراقبة درجة الحرارة لنقل وتخزين المواد المبردة مع تنبيهات فورية عند أي تغير في الحرارة.',
         'specs_fr': "Plage -40°C à +80°C\nPrécision ±0.5°C\nÉtanche IP68\nCâble 3m\nIdéal chaîne du froid",
         'specs_en': "Range -40°C to +80°C\nAccuracy ±0.5°C\nWaterproof IP68\n3m cable\nIdeal for cold chain",
         'specs_ar': "نطاق من -40°C إلى +80°C\nدقة قياس ±0.5°C\nمقاوم للماء IP68\nكابل بطول 3 أمتار\nمثالي لسلسلة التبريد",
         'price_fr': '350 - 500 MAD', 'price_en': '350 - 500 MAD', 'price_ar': '350 - 500 درهم'},
    ]
    for i, d in enumerate(data):
        try:
            p = Product.objects.all().order_by('order', 'pk')[i]
            p.name_fr = d['name_fr']; p.name_en = d['name_en']; p.name_ar = d['name_ar']
            p.description_fr = d['desc_fr']; p.description_en = d['desc_en']; p.description_ar = d['desc_ar']
            p.specifications_fr = d['specs_fr']; p.specifications_en = d['specs_en']; p.specifications_ar = d['specs_ar']
            p.price_range_fr = d['price_fr']; p.price_range_en = d['price_en']; p.price_range_ar = d['price_ar']
            p.save()
            print(f"  ✅ Product {p.pk}: {d['name_fr']}")
        except IndexError:
            break
    print("✅ Products translated")


def fill_categories():
    data = [
        {'name_fr': 'Guides GPS', 'name_en': 'GPS Guides', 'name_ar': 'دليل أجهزة GPS',
         'desc_fr': 'Guides et tutoriels sur les traceurs GPS', 'desc_en': 'Guides and tutorials on GPS trackers', 'desc_ar': 'شروحات وإرشادات حول أجهزة التتبع'},
        {'name_fr': 'Actualités', 'name_en': 'News', 'name_ar': 'الأخبار والمستجدات',
         'desc_fr': 'Actualités du secteur GPS et télématique', 'desc_en': 'GPS tracking and telematics news', 'desc_ar': 'آخر أخبار ومستجدات قطاع التتبع الجغرافي'},
        {'name_fr': 'Gestion de Flotte', 'name_en': 'Fleet Management', 'name_ar': 'إدارة الأساطيل',
         'desc_fr': 'Conseils pour la gestion de flotte', 'desc_en': 'Fleet management tips and advice', 'desc_ar': 'نصائح وإرشادات لإدارة أساطيل المركبات'},
    ]
    for i, d in enumerate(data):
        try:
            c = Category.objects.all().order_by('pk')[i]
            for k, v in d.items():
                setattr(c, k, v)
            c.save()
            print(f"  ✅ Category {c.pk}: {d['name_fr']}")
        except IndexError:
            break
    print("✅ Categories translated")


def fill_blog():
    data = [
        {'title_fr': 'Comment choisir le meilleur traceur GPS pour votre véhicule au Maroc',
         'title_en': 'How to Choose the Best GPS Tracker for Your Vehicle in Morocco',
         'title_ar': 'كيف تختار أفضل جهاز تتبع GPS لمركبتك في المغرب',
         'excerpt_fr': 'Guide complet pour sélectionner le traceur GPS 4G le plus adapté à vos besoins au Maroc.',
         'excerpt_en': 'Complete guide to selecting the 4G GPS tracker best suited to your needs in Morocco.',
         'excerpt_ar': 'دليل شامل لاختيار أفضل جهاز تتبع GPS 4G مناسب لاحتياجاتك في المغرب.',
         'meta_description_fr': 'Guide pour choisir le traceur GPS adapté à votre véhicule au Maroc.',
         'meta_description_en': 'Guide to choosing the right GPS tracker for your vehicle in Morocco.',
         'meta_description_ar': 'دليل شامل لاختيار جهاز تتبع GPS المناسب لسيارتك في المغرب.'},
        {'title_fr': 'Migration 2G vers 4G : Pourquoi mettre à jour votre traceur GPS',
         'title_en': '2G to 4G Migration: Why You Should Upgrade Your GPS Tracker',
         'title_ar': 'الانتقال من 2G إلى 4G: لماذا يجب تحديث جهاز التتبع GPS',
         'excerpt_fr': 'Avec le déclin des réseaux 2G, découvrez pourquoi migrer vos traceurs GPS vers la 4G LTE.',
         'excerpt_en': 'With the phase-out of 2G networks, discover why to upgrade your GPS trackers to 4G LTE.',
         'excerpt_ar': 'مع التراجع التدريجي لشبكات 2G، تعرف على أسباب الترقية إلى 4G LTE.',
         'meta_description_fr': 'Pourquoi migrer de la 2G vers la 4G pour vos traceurs GPS au Maroc.',
         'meta_description_en': 'Why migrate from 2G to 4G for your GPS trackers in Morocco.',
         'meta_description_ar': 'أسباب الانتقال من 2G إلى 4G لأجهزة التتبع في المغرب.'},
    ]
    for i, d in enumerate(data):
        try:
            post = BlogPost.objects.all().order_by('pk')[i]
            for k, v in d.items():
                setattr(post, k, v)
            post.save()
            print(f"  ✅ BlogPost {post.pk}: {d['title_fr']}")
        except IndexError:
            break
    print("✅ BlogPosts translated")


def fill_reseller_tiers():
    data = [
        {'title_fr': 'Pack Découverte', 'title_en': 'Starter Pack', 'title_ar': 'باقة الاكتشاف',
         'desc_fr': "Idéal pour les installateurs débutants souhaitant tester notre gamme.",
         'desc_en': 'Ideal for new installers looking to test our product range.',
         'desc_ar': 'مثالية للمركبين المبتدئين الراغبين في تجربة منتجاتنا.',
         'badge_text_fr': 'DÉBUTANT', 'badge_text_en': 'STARTER', 'badge_text_ar': 'مبتدئ',
         'volume_label_fr': '5-15 / mois', 'volume_label_en': '5-15 / month', 'volume_label_ar': '5-15 / شهرياً',
         'discount_text_fr': 'Remise 10%', 'discount_text_en': '10% Discount', 'discount_text_ar': 'خصم 10%',
         'features_fr': "Tarifs grossiste\nSupport technique\nFormation installation\nStock disponible Fès",
         'features_en': "Wholesale pricing\nTechnical support\nInstallation training\nAvailable stock in Fez",
         'features_ar': "أسعار الجملة\nدعم تقني\nتدريب على التركيب\nمخزون متوفر في فاس",
         'cta_text_fr': 'Postuler Maintenant', 'cta_text_en': 'Apply Now', 'cta_text_ar': 'قدّم طلبك الآن'},
        {'title_fr': 'Pack Pro Installateur', 'title_en': 'Pro Installer Pack', 'title_ar': 'باقة المركب المحترف',
         'desc_fr': 'Pour les installateurs et intégrateurs confirmés avec volume régulier.',
         'desc_en': 'For confirmed installers and integrators with regular volume.',
         'desc_ar': 'للمركبين والموزعين المعتمدين ذوي الحجم المنتظم.',
         'badge_text_fr': 'PRO', 'badge_text_en': 'PRO', 'badge_text_ar': 'احترافي',
         'volume_label_fr': '15-50 / mois', 'volume_label_en': '15-50 / month', 'volume_label_ar': '15-50 / شهرياً',
         'discount_text_fr': 'Remise 20%', 'discount_text_en': '20% Discount', 'discount_text_ar': 'خصم 20%',
         'features_fr': "Tout du Pack Découverte\nRemise 20%\nPlateforme co-brandée\nPriorité de livraison",
         'features_en': "Everything in Starter\n20% Discount\nCo-branded platform\nDelivery priority",
         'features_ar': "كل ما في باقة الاكتشاف\nخصم 20%\nمنصة بشعارك\nأولوية التوصيل",
         'cta_text_fr': 'Postuler Maintenant', 'cta_text_en': 'Apply Now', 'cta_text_ar': 'قدّم طلبك الآن'},
        {'title_fr': 'Distributeur Régional', 'title_en': 'Regional Distributor', 'title_ar': 'موزع إقليمي',
         'desc_fr': 'Pour les distributeurs à grande échelle avec exclusivité régionale.',
         'desc_en': 'For large-scale distributors with regional exclusivity.',
         'desc_ar': 'للموزعين على نطاق واسع مع حصرية إقليمية.',
         'badge_text_fr': 'ÉLITE', 'badge_text_en': 'ELITE', 'badge_text_ar': 'نخبة',
         'volume_label_fr': '50+ / mois', 'volume_label_en': '50+ / month', 'volume_label_ar': '+50 / شهرياً',
         'discount_text_fr': 'Remise 30%+', 'discount_text_en': '30%+ Discount', 'discount_text_ar': '+خصم 30%',
         'features_fr': "Tout du Pack Pro\nRemise 30%+\nExclusivité zone\nMarque blanche complète\nServeur dédié",
         'features_en': "Everything in Pro\n30%+ Discount\nZone exclusivity\nFull white-label\nDedicated server",
         'features_ar': "كل ما في الباقة الاحترافية\n+خصم 30%\nحصرية المنطقة\nعلامة بيضاء كاملة\nخادم مخصص",
         'cta_text_fr': 'Nous Contacter', 'cta_text_en': 'Contact Us', 'cta_text_ar': 'تواصل معنا'},
    ]
    for i, d in enumerate(data):
        try:
            tier = ResellerTier.objects.all().order_by('order', 'pk')[i]
            for k, v in d.items():
                setattr(tier, k, v)
            tier.save()
            print(f"  ✅ ResellerTier {tier.pk}: {d['title_fr']}")
        except IndexError:
            break
    print("✅ ResellerTiers translated")


def fill_promotions():
    for p in Promotion.objects.all():
        if not getattr(p, 'title_en', None) or not getattr(p, 'title_ar', None):
            # Generic translation for promo fields
            if 'pack' in (p.title or '').lower() or 'véhicule' in (p.title or '').lower():
                p.price_unit_fr = p.price_unit or 'pack'
                p.price_unit_en = 'pack'
                p.price_unit_ar = 'باقة'
            if p.cta_text and not getattr(p, 'cta_text_en', None):
                p.cta_text_en = 'Get this offer'
                p.cta_text_ar = 'استفد من العرض'
            p.save()
            print(f"  ✅ Promotion {p.pk}: {p.title}")
    print("✅ Promotions updated")


def main():
    print("=" * 60)
    print("  M2web Maroc — FILLING ALL TRANSLATIONS (FR / EN / AR)")
    print("=" * 60)
    fill_company()
    fill_mobile_app()
    fill_app_features()
    fill_app_plans()
    fill_app_screenshots()
    fill_pillars()
    fill_testimonials()
    fill_services()
    fill_products()
    fill_categories()
    fill_blog()
    fill_reseller_tiers()
    fill_promotions()
    print("=" * 60)
    print("  ✅ ALL TRANSLATIONS FILLED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == '__main__':
    main()
