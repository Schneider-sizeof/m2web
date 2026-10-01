import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r'c:\Users\Athen\Desktop\m2web')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.dev')
import django
django.setup()

from apps.core.models import CompanyInfo, WhyChooseUsPillar, Testimonial, Promotion
from apps.services.models import Service, Product
from apps.blog.models import Category, BlogPost

def update_company():
    c = CompanyInfo.objects.first()
    if c:
        c.stat_trackers_label_fr = 'Trackers Installés'
        c.stat_trackers_label_en = 'Trackers Installed'
        c.stat_trackers_label_ar = 'أجهزة تتبع مثبتة'

        c.stat_fleets_label_fr = 'Flottes Gérées'
        c.stat_fleets_label_en = 'Managed Fleets'
        c.stat_fleets_label_ar = 'أساطيل مدارة'

        c.stat_uptime_label_fr = 'Disponibilité Serveurs'
        c.stat_uptime_label_en = 'Server Uptime'
        c.stat_uptime_label_ar = 'جاهزية الخوادم'

        c.stat_experience_label_fr = "Années d'Expertise à Fès"
        c.stat_experience_label_en = 'Years of Expertise in Fez'
        c.stat_experience_label_ar = 'سنوات خبرة في فاس'

        c.meta_description_fr = 'M2web Maroc — Fournisseur N°1 de solutions GPS et gestion de flotte à Fès. Traceurs GPS en gros et au détail, installation et support technique.'
        c.meta_description_en = 'M2web Morocco — Leading provider of GPS tracking & fleet management solutions in Fez and across Morocco. Wholesale & retail trackers, installation & tech support.'
        c.meta_description_ar = 'M2web المغرب — المزود الرائد لحلول تتبع المركبات GPS وإدارة الأساطيل في فاس وجميع أنحاء المغرب. بيع بالجملة والتقسيط مع التركيب والدعم الفني.'

        c.save()
        print("Updated CompanyInfo stats and meta translations")

def update_pillars():
    pillars_data = [
        {
            'id': 1,
            'title_fr': 'Réseau 4G Multi-Opérateur',
            'title_en': 'Multi-Operator 4G Network',
            'title_ar': 'شبكة 4G متعددة المشغلين',
            'desc_fr': "Connectivité maximale garantie grâce à nos cartes SIM M2M multi-opérateurs couvrant l'ensemble du territoire marocain sans coupure.",
            'desc_en': 'Guaranteed maximum connectivity with multi-operator M2M SIM cards covering all of Morocco without interruption.',
            'desc_ar': 'اتصال مستمر ومضمون بفضل شرائح SIM M2M متعددة المشغلين تغطي كافة التراب المغربي بدون انقطاع.'
        },
        {
            'id': 2,
            'title_fr': 'Application Mobile & Web',
            'title_en': 'Mobile & Web Application',
            'title_ar': 'تطبيق الهاتف والويب',
            'desc_fr': 'Accédez à votre flotte 24h/24 et 7j/7 depuis votre smartphone iOS/Android ou votre navigateur avec une interface moderne et fluide.',
            'desc_en': 'Access your fleet 24/7 from your iOS/Android smartphone or web browser with a modern and fluid interface.',
            'desc_ar': 'تحكم في أسطولك على مدار الساعة 24/7 عبر هاتفك الذكي iOS/Android أو متصفح الويب بواجهة عصرية وسلسة.'
        },
        {
            'id': 3,
            'title_fr': 'Contrôle Carburant Anti-Vol',
            'title_en': 'Anti-Theft Fuel Monitoring',
            'title_ar': 'مراقبة الوقود ومكافحة السرقة',
            'desc_fr': 'Sondes de niveau haute précision pour détecter instantanément les chutes anormales, les vols et surveiller la consommation réelle.',
            'desc_en': 'High-precision level probes to instantly detect abnormal drops, fuel theft, and monitor actual consumption.',
            'desc_ar': 'مستشعرات دقيقة لمستوى الوقود لكشف أي انخفاض غير طبيعي وسرقة الوقود ومراقبة الاستهلاك الفعلي فورياً.'
        },
        {
            'id': 4,
            'title_fr': 'Installation & Support à Fès',
            'title_en': 'Installation & Support in Fez',
            'title_ar': 'التركيب والدعم في فاس',
            'desc_fr': 'Atelier dédié à Fès et équipe technique itinérante pour une installation soignée, rapide et un service après-vente de proximité.',
            'desc_en': 'Dedicated workshop in Fez and mobile technical team for fast, professional installation and responsive local support.',
            'desc_ar': 'ورشة متخصصة في فاس وفريق تقني متنقل لتركيب احترافي وسريع مع خدمة ما بعد البيع وقرب دائم من الزبون.'
        }
    ]
    for p in pillars_data:
        try:
            pillar = WhyChooseUsPillar.objects.get(pk=p['id'])
            pillar.title = p['title_fr']
            pillar.title_fr = p['title_fr']
            pillar.title_en = p['title_en']
            pillar.title_ar = p['title_ar']
            pillar.description = p['desc_fr']
            pillar.description_fr = p['desc_fr']
            pillar.description_en = p['desc_en']
            pillar.description_ar = p['desc_ar']
            pillar.save()
            print(f"Updated Pillar {p['id']}")
        except WhyChooseUsPillar.DoesNotExist:
            print(f"Pillar {p['id']} not found")

def update_testimonials():
    testimonials_data = [
        {
            'id': 1,
            'role_fr': 'Directeur Général',
            'role_en': 'General Manager',
            'role_ar': 'المدير العام',
            'content_fr': 'M2web a transformé la gestion de notre flotte de 45 camions. Le suivi en temps réel et les alertes de consommation nous ont permis de réduire nos coûts carburant de 20%.',
            'content_en': 'M2web transformed the management of our 45-truck fleet. Real-time tracking and consumption alerts allowed us to reduce our fuel costs by 20%.',
            'content_ar': 'غيرت M2web إدارة أسطولنا المكون من 45 شاحنة بالكامل. مكننا التتبع في الوقت الفعلي وتنبيهات الاستهلاك من خفض تكاليف الوقود بنسبة 20%.'
        },
        {
            'id': 2,
            'role_fr': 'Responsable Logistique',
            'role_en': 'Logistics Manager',
            'role_ar': 'مسؤولة اللوجستيك',
            'content_fr': "Service impeccable et support technique réactif. Les traceurs GPS 4G sont fiables et l'application mobile est très intuitive. Je recommande vivement M2web.",
            'content_en': 'Impeccable service and responsive technical support. The 4G GPS trackers are reliable and the mobile app is very intuitive. I highly recommend M2web.',
            'content_ar': 'خدمة لا تشوبها شائبة ودعم فني متجاوب للغاية. أجهزة التتبع 4G موثوقة جداً وتطبيق الهاتف سهل الاستخدام. أوصي بشدة بـ M2web.'
        },
        {
            'id': 3,
            'role_fr': 'Gérant',
            'role_en': 'Managing Director',
            'role_ar': 'مسير شركة',
            'content_fr': 'Grâce à M2web, nous avons sécurisé notre parc de 80 véhicules de location. La coupure moteur à distance nous a sauvé plusieurs fois du vol.',
            'content_en': 'Thanks to M2web, we secured our fleet of 80 rental vehicles. The remote engine cutoff has saved us from vehicle theft multiple times.',
            'content_ar': 'بفضل M2web أمّنا أسطولنا المكون من 80 سيارة كراء. ميزة قطع المحرك عن بعد أنقذتنا من السرقة في عدة مناسبات.'
        },
        {
            'id': 4,
            'role_fr': 'Directeur Technique',
            'role_en': 'Technical Director',
            'role_ar': 'المدير التقني',
            'content_fr': 'Les capteurs de température et le suivi de la chaîne du froid nous permettent de garantir la qualité de nos livraisons. M2web comprend les besoins du transport frigorifique.',
            'content_en': 'Temperature sensors and cold chain monitoring allow us to guarantee delivery quality. M2web truly understands refrigerated transport needs.',
            'content_ar': 'تتيح لنا مستشعرات الحرارة ومراقبة سلسلة التبريد ضمان جودة شحناتنا بدقة. تفهم M2web تماماً متطلبات النقل المبرد.'
        }
    ]
    for t in testimonials_data:
        try:
            testi = Testimonial.objects.get(pk=t['id'])
            testi.role = t['role_fr']
            testi.role_fr = t['role_fr']
            testi.role_en = t['role_en']
            testi.role_ar = t['role_ar']
            testi.content = t['content_fr']
            testi.content_fr = t['content_fr']
            testi.content_en = t['content_en']
            testi.content_ar = t['content_ar']
            testi.save()
            print(f"Updated Testimonial {t['id']}")
        except Testimonial.DoesNotExist:
            print(f"Testimonial {t['id']} not found")

def update_services():
    services_data = [
        {
            'id': 1,
            'title_fr': 'Gestion de Flotte en Temps Réel',
            'title_en': 'Real-Time Fleet Management',
            'title_ar': 'إدارة الأساطيل في الوقت الفعلي',
            'desc_fr': 'Suivi en temps réel de votre flotte avec historique des trajets, alertes de vitesse, géo-clôtures et rapports détaillés.',
            'desc_en': 'Real-time fleet tracking with complete trip history, speed alerts, geofencing, and comprehensive reports.',
            'desc_ar': 'تتبع مباشر ولحظي لأسطولك مع سجل كامل للرحلات، تنبيهات السرعة، السياج الجغرافي وتقارير شاملة.'
        },
        {
            'id': 2,
            'title_fr': 'Contrôle Carburant & Éco-Conduite',
            'title_en': 'Fuel Monitoring & Eco-Driving',
            'title_ar': 'مراقبة الوقود والقيادة الاقتصادية',
            'desc_fr': 'Intégration de sondes de carburant pour auditer la consommation, détecter les vols de carburant et adopter une conduite économique.',
            'desc_en': 'Integration of high-precision fuel probes to audit consumption, detect fuel theft, and foster economical driving.',
            'desc_ar': 'دمج مستشعرات الوقود الدقيقة لتدقيق الاستهلاك، كشف السرقات، والتشجيع على القيادة الاقتصادية.'
        },
        {
            'id': 3,
            'title_fr': 'Sécurité & Coupure Moteur à Distance',
            'title_en': 'Security & Remote Engine Cutoff',
            'title_ar': 'الأمان وقطع المحرك عن بعد',
            'desc_fr': 'Protection antivol complète avec coupure du moteur à distance via SMS ou application mobile et alertes de remorquage.',
            'desc_en': 'Comprehensive anti-theft protection with remote engine shutdown via SMS or mobile app, and towing alerts.',
            'desc_ar': 'حماية شاملة ضد السرقة مع إمكانية إيقاف المحرك عن بعد عبر الرسائل القصيرة أو التطبيق وتنبيهات القطر.'
        },
        {
            'id': 4,
            'title_fr': 'Télématique & Chaîne du Froid',
            'title_en': 'Telematics & Cold Chain Monitoring',
            'title_ar': 'التتبع الذكي وسلسلة التبريد',
            'desc_fr': 'Capteurs de température pour le transport frigorifique garantissant le respect de la chaîne du froid avec alertes en temps réel.',
            'desc_en': 'Temperature sensors for refrigerated transport ensuring cold chain integrity with real-time temperature alerts.',
            'desc_ar': 'مستشعرات حرارة للنقل المبرد لضمان سلامة سلسلة التبريد مع تنبيهات فورية عند أي تغير في درجة الحرارة.'
        },
        {
            'id': 5,
            'title_fr': 'Installation & Support Technique',
            'title_en': 'Professional Installation & Support',
            'title_ar': 'التركيب والدعم التقني المتخصص',
            'desc_fr': 'Notre atelier à Fès et nos techniciens itinérants assurent une installation professionnelle et un support technique sur tout le Maroc.',
            'desc_en': 'Our dedicated workshop in Fez and mobile technicians provide clean, professional installation and technical support across Morocco.',
            'desc_ar': 'تضمن ورشتنا في فاس وفرقنا المتنقلة تركيباً احترافياً ودعماً تقنياً متميزاً في جميع أنحاء المغرب.'
        }
    ]
    for s in services_data:
        try:
            srv = Service.objects.get(pk=s['id'])
            srv.title = s['title_fr']
            srv.title_fr = s['title_fr']
            srv.title_en = s['title_en']
            srv.title_ar = s['title_ar']
            srv.description = s['desc_fr']
            srv.description_fr = s['desc_fr']
            srv.description_en = s['desc_en']
            srv.description_ar = s['desc_ar']
            srv.save()
            print(f"Updated Service {s['id']}")
        except Service.DoesNotExist:
            print(f"Service {s['id']} not found")

def update_products():
    products_data = [
        {
            'id': 1,
            'name_fr': 'Traceur GPS 4G OBD-II',
            'name_en': '4G OBD-II GPS Tracker',
            'name_ar': 'جهاز تتبع GPS 4G لمنفذ OBD-II',
            'desc_fr': 'Traceur GPS OBD-II plug & play avec connectivité 4G LTE, suivi en temps réel et lecture des données véhicule.',
            'desc_en': 'Plug & play OBD-II GPS tracker with 4G LTE connectivity, real-time tracking, and vehicle diagnostics.',
            'desc_ar': 'جهاز تتبع OBD-II سهل التركيب والتوصيل المباشر مع اتصال 4G LTE، تتبع فوري وتشخيص ذكي.',
            'specs_fr': "4G LTE\nOBD-II Port\nGPS + GLONASS + BeiDou\nAccéléromètre intégré\nApplication mobile iOS & Android",
            'specs_en': "4G LTE\nOBD-II Port\nGPS + GLONASS + BeiDou\nBuilt-in Accelerometer\niOS & Android Mobile App",
            'specs_ar': "4G LTE\nمنفذ OBD-II مباشر\nنظام GPS + GLONASS + BeiDou\nمستشعر تسارع مدمج\nتطبيق iOS وأندرويد",
            'price_fr': '450 - 600 MAD',
            'price_en': '450 - 600 MAD',
            'price_ar': '450 - 600 درهم'
        },
        {
            'id': 2,
            'name_fr': 'Traceur GPS 4G Filaire (Hardwired)',
            'name_en': '4G Hardwired GPS Tracker',
            'name_ar': 'جهاز تتبع GPS 4G سلكي احترافي',
            'desc_fr': 'Traceur GPS professionnel à installation filaire avec relais de coupure moteur et batterie de secours intégrée.',
            'desc_en': 'Professional hardwired GPS tracker with remote engine cutoff relay and integrated backup battery.',
            'desc_ar': 'جهاز تتبع احترافي بتركيب سلكي مخفي مع مرحل لقطع المحرك عن بعد وبطارية طوارئ مدمجة.',
            'specs_fr': "4G LTE\nInstallation filaire\nRelais coupure moteur\nBatterie de secours\nAntenne GPS haute sensibilité",
            'specs_en': "4G LTE\nHardwired installation\nEngine cutoff relay\nBackup battery\nHigh-sensitivity GPS antenna",
            'specs_ar': "4G LTE\nتركيب سلكي احترافي\nمرحل قطع المحرك\nبطارية طوارئ احتياطية\nهوائي GPS عالي الحساسية",
            'price_fr': '350 - 550 MAD',
            'price_en': '350 - 550 MAD',
            'price_ar': '350 - 550 درهم'
        },
        {
            'id': 3,
            'name_fr': 'Traceur GPS Magnétique Autonome',
            'name_en': 'Standalone Magnetic GPS Tracker',
            'name_ar': 'جهاز تتبع GPS مغناطيسي مستقل',
            'desc_fr': 'Traceur GPS autonome avec aimant puissant et batterie longue durée, idéal pour les conteneurs et remorques.',
            'desc_en': 'Standalone GPS tracker with powerful industrial magnet and long-life rechargeable battery, ideal for assets and trailers.',
            'desc_ar': 'جهاز تتبع مستقل بمغناطيس صناعي قوي وبطارية تدوم طويلاً، مثالي للمقطورات والحاويات والأصول المتنقلة.',
            'specs_fr': "4G LTE\nAimant puissant\nBatterie 5000mAh\nÉtanche IP67\nJusqu'à 90 jours d'autonomie",
            'specs_en': "4G LTE\nPowerful magnet\n5000mAh battery\nWaterproof IP67\nUp to 90 days battery life",
            'specs_ar': "4G LTE\nمغناطيس تثبيت قوي\nبطارية 5000 مللي أمبير\nمقاوم للماء IP67\nاستقلالية تدوم حتى 90 يوماً",
            'price_fr': '600 - 900 MAD',
            'price_en': '600 - 900 MAD',
            'price_ar': '600 - 900 درهم'
        },
        {
            'id': 4,
            'name_fr': 'Traceur Personnel / Asset Tracker',
            'name_en': 'Personal & Asset Tracker',
            'name_ar': 'جهاز تتبع شخصي وللأصول الثمينة',
            'desc_fr': 'Traceur GPS personnel compact et léger avec bouton SOS, idéal pour les personnes, colis et objets de valeur.',
            'desc_en': 'Compact and lightweight personal GPS tracker with emergency SOS button, ideal for workers, goods, and valuable assets.',
            'desc_ar': 'جهاز تتبع شخصي مدمج وخفيف الوزن مزود بزر استغاثة SOS، مثالي للأشخاص، الطرود والمقتنيات الثمينة.',
            'specs_fr': "4G LTE\nCompact et léger\nBouton SOS\nGéo-clôture\nHistorique de trajet\nApplication dédiée",
            'specs_en': "4G LTE\nCompact & Lightweight\nSOS emergency button\nGeofencing\nTrip history\nDedicated mobile app",
            'specs_ar': "4G LTE\nتصميم مدمج وخفيف\nزر استغاثة طارئ SOS\nسياج جغرافي ذكي\nسجل مسارات الرحلات\nتطبيق مخصص للهاتف",
            'price_fr': '250 - 400 MAD',
            'price_en': '250 - 400 MAD',
            'price_ar': '250 - 400 درهم'
        },
        {
            'id': 5,
            'name_fr': 'Sonde Carburant Capacitive',
            'name_en': 'Capacitive Fuel Level Sensor',
            'name_ar': 'مستشعر وقود سعوي عالي الدقة',
            'desc_fr': 'Sonde de niveau carburant capacitive haute précision pour la surveillance de la consommation et la détection de vol.',
            'desc_en': 'High-precision capacitive fuel level sensor for real-time consumption monitoring and theft prevention.',
            'desc_ar': 'مستشعر سعوي فائق الدقة لقياس مستوى الوقود في الوقت الفعلي ورصد الاستهلاك ومكافحة السرقة.',
            'specs_fr': "Précision ±1%\nLongueur ajustable\nCompatible tous réservoirs\nSortie analogique\nRésistant aux hydrocarbures",
            'specs_en': "Accuracy ±1%\nAdjustable length\nCompatible with all tanks\nAnalog/Digital output\nHydrocarbon-resistant",
            'specs_ar': "دقة قياس ±1%\nطول قابل للتعديل\nمتوافق مع جميع الخزانات\nمخرج تناظري ورقمي\nمقاوم للهيدروكربونات",
            'price_fr': '800 - 1200 MAD',
            'price_en': '800 - 1200 MAD',
            'price_ar': '800 - 1200 درهم'
        },
        {
            'id': 6,
            'name_fr': 'Capteur de Température',
            'name_en': 'Temperature Sensor',
            'name_ar': 'مستشعر درجة الحرارة',
            'desc_fr': 'Capteur de température pour le monitoring de la chaîne du froid avec alertes en temps réel.',
            'desc_en': 'Temperature monitoring sensor for cold chain logistics with real-time temperature deviation alerts.',
            'desc_ar': 'مستشعر مراقبة درجة الحرارة لنقل وتخزين المواد المبردة مع تنبيهات فورية عند أي تغير في الحرارة.',
            'specs_fr': "Plage -40°C à +80°C\nPrécision ±0.5°C\nÉtanche IP68\nCâble 3m\nIdéal chaîne du froid",
            'specs_en': "Range -40°C to +80°C\nAccuracy ±0.5°C\nWaterproof IP68\n3m cable\nIdeal for cold chain",
            'specs_ar': "نطاق من -40°C إلى +80°C\nدقة قياس ±0.5°C\nمقاوم للماء IP68\nكابل بطول 3 أمتار\nمثالي لسلسلة التبريد",
            'price_fr': '350 - 500 MAD',
            'price_en': '350 - 500 MAD',
            'price_ar': '350 - 500 درهم'
        }
    ]
    for p in products_data:
        try:
            prod = Product.objects.get(pk=p['id'])
            prod.name = p['name_fr']
            prod.name_fr = p['name_fr']
            prod.name_en = p['name_en']
            prod.name_ar = p['name_ar']
            prod.description = p['desc_fr']
            prod.description_fr = p['desc_fr']
            prod.description_en = p['desc_en']
            prod.description_ar = p['desc_ar']
            prod.specifications = p['specs_fr']
            prod.specifications_fr = p['specs_fr']
            prod.specifications_en = p['specs_en']
            prod.specifications_ar = p['specs_ar']
            prod.price_range = p['price_fr']
            prod.price_range_fr = p['price_fr']
            prod.price_range_en = p['price_en']
            prod.price_range_ar = p['price_ar']
            prod.save()
            print(f"Updated Product {p['id']}")
        except Product.DoesNotExist:
            print(f"Product {p['id']} not found")

def update_categories():
    categories_data = [
        {
            'id': 1,
            'name_fr': 'Guides GPS',
            'name_en': 'GPS Guides',
            'name_ar': 'دليل أجهزة GPS',
            'desc_fr': 'Guides et tutoriels sur les traceurs GPS',
            'desc_en': 'Guides and tutorials on GPS trackers and fleet management',
            'desc_ar': 'شروحات وإرشادات حول أجهزة التتبع وإدارة الأساطيل'
        },
        {
            'id': 2,
            'name_fr': 'Actualités',
            'name_en': 'News',
            'name_ar': 'الأخبار والمستجدات',
            'desc_fr': 'Actualités du secteur GPS et télématique au Maroc',
            'desc_en': 'Industry news on GPS tracking and telematics in Morocco',
            'desc_ar': 'آخر أخبار ومستجدات قطاع التتبع الجغرافي والتليماتيك بالمغرب'
        },
        {
            'id': 3,
            'name_fr': 'Gestion de Flotte',
            'name_en': 'Fleet Management',
            'name_ar': 'إدارة الأساطيل',
            'desc_fr': 'Conseils pour la gestion de flotte automobile',
            'desc_en': 'Practical advice and strategies for vehicle fleet management',
            'desc_ar': 'نصائح وإرشادات عملية لإدارة أساطيل السيارات والشاحنات'
        }
    ]
    for c in categories_data:
        try:
            cat = Category.objects.get(pk=c['id'])
            cat.name = c['name_fr']
            cat.name_fr = c['name_fr']
            cat.name_en = c['name_en']
            cat.name_ar = c['name_ar']
            cat.description = c['desc_fr']
            cat.description_fr = c['desc_fr']
            cat.description_en = c['desc_en']
            cat.description_ar = c['desc_ar']
            cat.save()
            print(f"Updated Category {c['id']}")
        except Category.DoesNotExist:
            print(f"Category {c['id']} not found")

def update_blog():
    posts_data = [
        {
            'id': 1,
            'title_fr': 'Comment choisir le meilleur traceur GPS pour votre véhicule au Maroc',
            'title_en': 'How to Choose the Best GPS Tracker for Your Vehicle in Morocco',
            'title_ar': 'كيف تختار أفضل جهاز تتبع GPS لمركبتك في المغرب',
            'excerpt_fr': 'Guide complet pour sélectionner le traceur GPS 4G le plus adapté aux besoins de votre entreprise ou véhicule personnel au Maroc.',
            'excerpt_en': 'Complete guide to selecting the 4G GPS tracker best suited to your company or personal vehicle in Morocco.',
            'excerpt_ar': 'دليل شامل لاختيار أفضل جهاز تتبع GPS 4G مناسب لاحتياجات شركتك أو سيارتك الخاصة في المغرب.',
            'meta_fr': 'Guide pour choisir le traceur GPS adapté à votre véhicule au Maroc. Comparatif 4G, OBD et filaire.',
            'meta_en': 'Guide to choosing the right GPS tracker for your vehicle in Morocco. 4G, OBD, and hardwired comparison.',
            'meta_ar': 'دليل شامل لاختيار جهاز تتبع GPS المناسب لسيارتك في المغرب. مقارنة أجهزة 4G وOBD والسلكية.'
        },
        {
            'id': 2,
            'title_fr': 'Migration 2G vers 4G : Pourquoi mettre à jour votre traceur GPS',
            'title_en': '2G to 4G Migration: Why You Should Upgrade Your GPS Tracker',
            'title_ar': 'الانتقال من 2G إلى 4G: لماذا يجب تحديث جهاز التتبع GPS الخاص بك',
            'excerpt_fr': 'Avec le déclin progressif des réseaux 2G, découvrez pourquoi et comment migrer vos traceurs GPS vers la 4G LTE pour garantir la continuité de votre suivi de flotte.',
            'excerpt_en': 'With the gradual phase-out of 2G networks, discover why and how to upgrade your GPS trackers to 4G LTE to ensure uninterrupted fleet tracking.',
            'excerpt_ar': 'مع التراجع التدريجي لشبكات الجيل الثاني 2G، تعرف على أسباب وكيفية الترقية إلى 4G LTE لضمان استمرارية تتبع أسطولك بدون انقطاع.',
            'meta_fr': 'Pourquoi migrer de la 2G vers la 4G pour vos traceurs GPS au Maroc. Avantages et conseils de transition.',
            'meta_en': 'Why migrate from 2G to 4G for your GPS trackers in Morocco. Benefits and migration tips.',
            'meta_ar': 'أسباب الانتقال من 2G إلى 4G لأجهزة التتبع في المغرب. المزايا ونصائح عملية للترقية.'
        }
    ]
    for p in posts_data:
        try:
            post = BlogPost.objects.get(pk=p['id'])
            post.title = p['title_fr']
            post.title_fr = p['title_fr']
            post.title_en = p['title_en']
            post.title_ar = p['title_ar']
            post.excerpt = p['excerpt_fr']
            post.excerpt_fr = p['excerpt_fr']
            post.excerpt_en = p['excerpt_en']
            post.excerpt_ar = p['excerpt_ar']
            post.meta_description = p['meta_fr']
            post.meta_description_fr = p['meta_fr']
            post.meta_description_en = p['meta_en']
            post.meta_description_ar = p['meta_ar']
            post.save()
            print(f"Updated BlogPost {p['id']}")
        except BlogPost.DoesNotExist:
            print(f"BlogPost {p['id']} not found")

def update_promotions():
    promos = Promotion.objects.all()
    for p in promos:
        if '5' in p.title:
            p.price_unit_fr = 'pack 5 véhicules'
            p.price_unit_en = '5-vehicle pack'
            p.price_unit_ar = 'باقة 5 مركبات'
        else:
            p.price_unit_fr = 'pack'
            p.price_unit_en = 'pack'
            p.price_unit_ar = 'باقة'
        p.save()
        print(f"Updated Promotion {p.pk} price_unit")

def main():
    print("--- UPDATING ALL DATABASE TRANSLATIONS ---")
    update_company()
    update_pillars()
    update_testimonials()
    update_services()
    update_products()
    update_categories()
    update_blog()
    update_promotions()
    print("--- ALL DATABASE TRANSLATIONS UPDATED SUCCESSFULLY ---")

if __name__ == '__main__':
    main()
