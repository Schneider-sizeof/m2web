import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm2web_project.settings.dev')
django.setup()

from apps.core.models import Promotion

# Clear old promotions
Promotion.objects.all().delete()

promo1 = Promotion.objects.create(
    title_fr="Pack Sécurité & Antivol 4G",
    title_en="4G Security & Anti-Theft Pack",
    title_ar="باقة الأمان ومكافحة السرقة 4G",
    badge_fr="PROMO FLASH",
    badge_en="FLASH SALE",
    badge_ar="عرض فلاش",
    discount_label_fr="-25%",
    discount_label_en="-25%",
    discount_label_ar="-25%",
    summary_fr="Traceur GPS 4G haute précision avec coupure moteur à distance et alertes instantanées.",
    summary_en="High-precision 4G GPS tracker with remote engine cutoff and instant alerts.",
    summary_ar="جهاز تتبع GPS 4G عالي الدقة مع خاصية قطع المحرك عن بعد وتنبيهات فورية.",
    features_fr="Traceur GPS 4G étanche IP67\nRelais de coupure moteur à distance\nCarte SIM M2M 1 an incluse\nAccès plateforme Web & App Android/iOS\nGarantie 1 an échange à neuf\nInstallation gratuite à Fès",
    features_en="Waterproof IP67 4G GPS tracker\nRemote engine cutoff relay\n1-year M2M SIM card included\nWeb Platform & Android/iOS App access\n1-year replacement warranty\nFree installation in Fez",
    features_ar="جهاز تتبع GPS 4G مقاوم للماء IP67\nمرحل قطع المحرك عن بعد\nشريحة SIM M2M لمدة سنة مشمولة\nولوج لمنصة الويب وتطبيق أندرويد/iOS\nضمان استبدال فوري لمدة سنة\nتركيب مجاني في فاس",
    original_price=1200,
    promo_price=890,
    price_unit="pack",
    valid_until=date.today() + timedelta(days=30),
    cta_text_fr="Commander ce Pack",
    cta_text_en="Order this Pack",
    cta_text_ar="طلب هذه الباقة",
    is_active=True,
    is_featured=True,
    order=1,
)

promo2 = Promotion.objects.create(
    title_fr="Pack Flotte Entreprise (5 Véhicules)",
    title_en="Enterprise Fleet Pack (5 Vehicles)",
    title_ar="باقة أسطول الشركات (5 مركبات)",
    badge_fr="MEILLEURE VENTE",
    badge_en="BEST SELLER",
    badge_ar="الأكثر طلباً",
    discount_label_fr="Économisez 1000 DH",
    discount_label_en="Save 1000 DH",
    discount_label_ar="وفر 1000 درهم",
    summary_fr="La solution complète pour PME et transporteurs : géolocalisation en temps réel et rapports de trajets.",
    summary_en="The complete solution for SMEs and transporters: real-time tracking and route reports.",
    summary_ar="الحل الشامل للشركات الصغرى والمتوسطة وشركات النقل: تتبع في الوقت الفعلي وتقارير الرحلات.",
    features_fr="5 Traceurs GPS 4G professionnels\n5 Cartes SIM M2M avec data 1 an\nTableau de bord de gestion de flotte multi-utilisateurs\nRapports de kilométrage et vitesse\nAlertes de maintenance et vidange\nSupport technique prioritaire 24/7",
    features_en="5 Professional 4G GPS Trackers\n5 M2M SIM Cards with 1-year data\nMulti-user fleet management dashboard\nMileage and speed reporting\nMaintenance and service alerts\n24/7 Priority technical support",
    features_ar="5 أجهزة تتبع GPS 4G احترافية\n5 شرائح SIM M2M مع إنترنت لسنة\nلوحة تحكم لإدارة الأسطول متعددة المستخدمين\nتقارير الكيلومترات والسرعة\nتنبيهات الصيانة الدورية\nدعم فني أولوي 24/7",
    original_price=4500,
    promo_price=3490,
    price_unit="pack 5 véhicules",
    valid_until=date.today() + timedelta(days=45),
    cta_text_fr="Profiter de l'offre Flotte",
    cta_text_en="Get Fleet Offer",
    cta_text_ar="الاستفادة من عرض الأسطول",
    is_active=True,
    is_featured=True,
    order=2,
)

promo3 = Promotion.objects.create(
    title_fr="Pack Contrôle Carburant & Température",
    title_en="Fuel & Temperature Control Pack",
    title_ar="باقة مراقبة الوقود والحرارة",
    badge_fr="OFFRE SPÉCIALE",
    badge_en="SPECIAL OFFER",
    badge_ar="عرض خاص",
    discount_label_fr="-500 DH",
    discount_label_en="-500 DH",
    discount_label_ar="-500 درهم",
    summary_fr="Traceur 4G combiné à une sonde de carburant haute précision pour éliminer les vols et le gaspillage.",
    summary_en="4G tracker combined with a high-precision fuel sensor to eliminate theft and waste.",
    summary_ar="جهاز تتبع 4G مقترن بمستشعر وقود عالي الدقة لمنع السرقات وتقليل الهدر.",
    features_fr="Traceur GPS 4G pour poids lourds et engins\nSonde de niveau de carburant capacitive\nDétection instantanée des siphonnages\nCourbes de consommation réelles\nAlertes SMS & Push en cas de baisse anormale\nCalibrage et étalonnage inclus",
    features_en="4G GPS tracker for heavy trucks and machinery\nCapacitive fuel level probe\nInstant fuel theft/siphoning detection\nReal consumption trend charts\nInstant SMS & Push alerts for abnormal drops\nCalibration and setup included",
    features_ar="جهاز تتبع 4G للشاحنات والآليات الثقيلة\nمستشعر وقود سعوي عالي الدقة\nكشف فوري لسرقة وشفط الوقود\nمخططات استهلاك بيانية دقيقة\nتنبيهات فورية عند أي انخفاض غير طبيعي\nالمعايرة والضبط مشمولان",
    original_price=2390,
    promo_price=1890,
    price_unit="pack",
    valid_until=date.today() + timedelta(days=30),
    cta_text_fr="Commander ce Pack",
    cta_text_en="Order this Pack",
    cta_text_ar="طلب هذه الباقة",
    is_active=True,
    is_featured=True,
    order=3,
)

print(f"Created {Promotion.objects.count()} promotions with FR, EN, AR translations!")
