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
    },
    {
        'msgid': 'Connexion',
        'en': 'Sign In',
        'ar': 'تسجيل الدخول',
        'fr': 'Connexion'
    },
    {
        'msgid': 'Connexion Plateforme Trackmaroc',
        'en': 'Sign in to Trackmaroc Platform',
        'ar': 'تسجيل الدخول إلى منصة تراك ماروك',
        'fr': 'Connexion Plateforme Trackmaroc'
    },
    {
        'msgid': 'Entreprise Marocaine de Télématique',
        'en': 'Moroccan Telematics Company',
        'ar': 'شركة مغربية رائدة في حلول التليماتيك',
        'fr': 'Entreprise Marocaine de Télématique'
    },
    {
        'msgid': 'Installation certifiée partout au Maroc',
        'en': 'Certified installation across Morocco',
        'ar': 'تركيب معتمد في جميع أنحاء المغرب',
        'fr': 'Installation certifiée partout au Maroc'
    },
    {
        'msgid': 'Cartes SIM M2M multi-opérateurs',
        'en': 'Multi-operator M2M SIM cards',
        'ar': 'شرائح M2M متعددة المشغلين',
        'fr': 'Cartes SIM M2M multi-opérateurs'
    },
    {
        'msgid': 'Support technique local et réactif',
        'en': 'Local and responsive technical support',
        'ar': 'دعم فني محلي وسريع الاستجابة',
        'fr': 'Support technique local et réactif'
    },
    {
        'msgid': 'Plateforme SaaS et serveurs dédiés',
        'en': 'SaaS platform and dedicated servers',
        'ar': 'منصة سحابية SaaS وخوادم مخصصة',
        'fr': 'Plateforme SaaS et serveurs dédiés'
    },
    {
        'msgid': "Années d'excellence en tracking GPS au Maroc",
        'en': 'Years of excellence in GPS tracking in Morocco',
        'ar': 'سنوات من التميز في التتبع عبر GPS بالمغرب',
        'fr': "Années d'excellence en tracking GPS au Maroc"
    },
    {
        'msgid': 'Navigation & Univers M2web',
        'en': 'Navigation & M2web Ecosystem',
        'ar': 'استكشف منظومة M2web',
        'fr': 'Navigation & Univers M2web'
    },
    {
        'msgid': 'Explorez Toutes Nos Solutions',
        'en': 'Explore All Our Solutions',
        'ar': 'استكشف جميع حلولنا',
        'fr': 'Explorez Toutes Nos Solutions'
    },
    {
        'msgid': 'Accédez facilement aux différentes sections de notre plateforme selon votre profil et vos exigences télématiques.',
        'en': 'Easily access different sections of our platform according to your profile and telematics requirements.',
        'ar': 'الوصول بسهولة إلى مختلف أقسام منصتنا وفقًا لاحتياجاتك ومتطلبات التليماتيك الخاصة بك.',
        'fr': 'Accédez facilement aux différentes sections de notre plateforme selon votre profil et vos exigences télématiques.'
    },
    {
        'msgid': 'Services & Matériel GPS',
        'en': 'GPS Services & Hardware',
        'ar': 'خدمات وأجهزة تتبع GPS',
        'fr': 'Services & Matériel GPS'
    },
    {
        'msgid': 'Découvrez nos traceurs 4G, sondes de carburant anti-vol, capteurs de température et coupe-circuit à distance certifiés.',
        'en': 'Discover our 4G trackers, anti-theft fuel sensors, temperature sensors and certified remote engine cutoff.',
        'ar': 'اكتشف أجهزة التتبع 4G وحساسات الوقود المضادة للسرقة وحساسات الحرارة وقواطع المحرك عن بعد المعتمدة.',
        'fr': 'Découvrez nos traceurs 4G, sondes de carburant anti-vol, capteurs de température et coupe-circuit à distance certifiés.'
    },
    {
        'msgid': 'Catalogue & Services',
        'en': 'Catalog & Services',
        'ar': 'الكتالوج والخدمات',
        'fr': 'Catalogue & Services'
    },
    {
        'msgid': 'Application Mobile Dédiée',
        'en': 'Dedicated Mobile App',
        'ar': 'تطبيق الهاتف المخصص',
        'fr': 'Application Mobile Dédiée'
    },
    {
        'msgid': 'Suivez votre flotte en temps réel sur smartphone. Alertes push, arrêt moteur d’urgence et historique détaillé de vos trajets.',
        'en': 'Track your fleet in real time on your smartphone. Push alerts, emergency engine cutoff, and detailed trip history.',
        'ar': 'تتبع أسطولك في الوقت الفعلي على هاتفك الذكي مع تنبيهات فورية، وإيقاف المحرك عن بعد، وسجل مفصل للرحلات.',
        'fr': 'Suivez votre flotte en temps réel sur smartphone. Alertes push, arrêt moteur d’urgence et historique détaillé de vos trajets.'
    },
    {
        'msgid': 'Découvrir l’Application',
        'en': 'Discover the App',
        'ar': 'اكتشف التطبيق',
        'fr': 'Découvrir l’Application'
    },
    {
        'msgid': 'Vente en Gros & Espace Revendeurs',
        'en': 'Wholesale & Reseller Portal',
        'ar': 'البيع بالجملة ومساحة الموزعين',
        'fr': 'Vente en Gros & Espace Revendeurs'
    },
    {
        'msgid': 'Tarifs distributeurs exclusifs pour revendeurs, électriciens auto et installateurs de géolocalisation partout au Maroc.',
        'en': 'Exclusive distributor prices for resellers, auto electricians, and GPS installers across Morocco.',
        'ar': 'أسعار خاصة للموزعين وكهربائيي السيارات ومركبي أجهزة التتبع في جميع مدن المغرب.',
        'fr': 'Tarifs distributeurs exclusifs pour revendeurs, électriciens auto et installateurs de géolocalisation partout au Maroc.'
    },
    {
        'msgid': 'Rejoindre le Réseau PRO',
        'en': 'Join the PRO Network',
        'ar': 'الانضمام إلى شبكة المحترفين',
        'fr': 'Rejoindre le Réseau PRO'
    },
    {
        'msgid': 'Plateforme & Serveur GPS',
        'en': 'GPS Platform & Server',
        'ar': 'منصة وخادم GPS',
        'fr': 'Plateforme & Serveur GPS'
    },
    {
        'msgid': 'Solutions Cloud SaaS dès 29 DH/mois, serveurs dédiés on-premise et personnalisation complète en Marque Blanche.',
        'en': 'Cloud SaaS solutions from 29 DH/month, dedicated on-premise servers, and full White Label customization.',
        'ar': 'حلول سحابية SaaS ابتداءً من 29 درهم/شهرياً، وخوادم خاصة، وعلامة تجارية بيضاء مخصصة بالكامل.',
        'fr': 'Solutions Cloud SaaS dès 29 DH/mois, serveurs dédiés on-premise et personnalisation complète en Marque Blanche.'
    },
    {
        'msgid': 'Voir les Formules & Tarifs',
        'en': 'View Plans & Pricing',
        'ar': 'عرض الباقات والأسعار',
        'fr': 'Voir les Formules & Tarifs'
    },
    {
        'msgid': 'Promotions & Offres Spéciales',
        'en': 'Promotions & Special Offers',
        'ar': 'عروض وتخفيضات خاصة',
        'fr': 'Promotions & Offres Spéciales'
    },
    {
        'msgid': 'Profitez de remises exclusives et de packs complets équipement + carte SIM + installation pour booster votre rentabilité.',
        'en': 'Enjoy exclusive discounts and complete packs (device + SIM card + installation) to maximize your profitability.',
        'ar': 'استفد من خصومات حصرية وحزم متكاملة تشمل الأجهزة وبطاقة SIM والتركيب لتعزيز مردوديتك.',
        'fr': 'Profitez de remises exclusives et de packs complets équipement + carte SIM + installation pour booster votre rentabilité.'
    },
    {
        'msgid': 'Consulter les Packs Promo',
        'en': 'View Promo Packs',
        'ar': 'تصفح باقات العروض',
        'fr': 'Consulter les Packs Promo'
    },
    {
        'msgid': 'Blog & Actualités Télématiques',
        'en': 'Blog & Telematics News',
        'ar': 'المدونة وأخبار التليماتيك',
        'fr': 'Blog & Actualités Télématiques'
    },
    {
        'msgid': 'Guides pratiques, conseils pour réduire la facture carburant, réglementations transport et innovations du secteur au Maroc.',
        'en': 'Practical guides, fuel-saving tips, transport regulations, and industry innovations in Morocco.',
        'ar': 'أدلة عملية، ونصائح لتقليل استهلاك الوقود، وقوانين النقل والابتكارات التكنولوجية في المغرب.',
        'fr': 'Guides pratiques, conseils pour réduire la facture carburant, réglementations transport et innovations du secteur au Maroc.'
    },
    {
        'msgid': 'Lire nos Derniers Articles',
        'en': 'Read Latest Articles',
        'ar': 'قراءة أحدث المقالات',
        'fr': 'Lire nos Derniers Articles'
    },
    {
        'msgid': 'Nos Piliers Technologiques',
        'en': 'Our Technological Pillars',
        'ar': 'ركائزنا التكنولوجية',
        'fr': 'Nos Piliers Technologiques'
    },
    {
        'msgid': 'Pourquoi les professionnels font confiance à M2web pour sécuriser et gérer leurs flottes.',
        'en': 'Why businesses and professionals trust M2web to secure and manage their fleets.',
        'ar': 'لماذا يثق المحترفون في M2web لتأمين وإدارة أساطيلهم.',
        'fr': 'Pourquoi les professionnels font confiance à M2web pour sécuriser et gérer leurs flottes.'
    },
    {
        'msgid': 'Constructeurs & Partenaires Technologiques',
        'en': 'Manufacturers & Technology Partners',
        'ar': 'المصنعون والشركاء التكنولوجيون',
        'fr': 'Constructeurs & Partenaires Technologiques'
    },
    {
        'msgid': 'Nous collaborons avec les leaders mondiaux de l’électronique et des télécommunications.',
        'en': 'We collaborate with global leaders in electronics and telecommunications.',
        'ar': 'نتعاون مع رواد العالم في مجالات الإلكترونيات والاتصالات.',
        'fr': 'Nous collaborons avec les leaders mondiaux de l’électronique et des télécommunications.'
    },
    {
        'msgid': 'Prêt à Transformer la Gestion de Votre Flotte ?',
        'en': 'Ready to Transform Your Fleet Management?',
        'ar': 'هل أنت جاهز لتطوير إدارة أسطولك؟',
        'fr': 'Prêt à Transformer la Gestion de Votre Flotte ?'
    },
    {
        'msgid': 'Contactez nos conseillers basés à Fès pour obtenir une démonstration sur mesure ou un devis personnalisé sans engagement.',
        'en': 'Contact our advisors based in Fez for a tailored demonstration or a free custom quote.',
        'ar': 'تواصل مع مستشارينا في فاس للحصول على عرض توضيحي مخصص أو مقايسة أسعار بدون أي التزام.',
        'fr': 'Contactez nos conseillers basés à Fès pour obtenir une démonstration sur mesure ou un devis personnalisé sans engagement.'
    },
    {
        'msgid': 'Demander un Devis Gratuit',
        'en': 'Request a Free Quote',
        'ar': 'طلب مقايسة أسعار مجانية',
        'fr': 'Demander un Devis Gratuit'
    },
    {
        'msgid': 'Tarifs & Forfaits Plateforme GPS',
        'en': 'GPS Platform Plans & Pricing',
        'ar': 'أسعار وباقات منصة GPS',
        'fr': 'Tarifs & Forfaits Plateforme GPS'
    },
    {
        'msgid': 'Formules Claires, Flexibles et Sans Frais Cachés',
        'en': 'Clear, Flexible Plans with No Hidden Fees',
        'ar': 'باقات واضحة ومرنة بدون أي رسوم خفية',
        'fr': 'Formules Claires, Flexibles et Sans Frais Cachés'
    },
    {
        'msgid': 'Que vous soyez gestionnaire d’une petite flotte, entreprise de transport ou intégrateur souhaitant lancer votre propre marque, nous avons la formule idéale.',
        'en': 'Whether you manage a small fleet, run a transport company, or are an integrator wanting to launch your own brand, we have the ideal plan.',
        'ar': 'سواء كنت تدير أسطولاً صغيراً، أو شركة نقل كبرى، أو موزعا ترغب في إطلاق علامتك الخاصة، لدينا الباقة المثالية لك.',
        'fr': 'Que vous soyez gestionnaire d’une petite flotte, entreprise de transport ou intégrateur souhaitant lancer votre propre marque, nous avons la formule idéale.'
    },
    {
        'msgid': 'Flottes & PME',
        'en': 'Fleets & SMBs',
        'ar': 'الأساطيل والمقاولات الصغرى والمتوسطة',
        'fr': 'Flottes & PME'
    },
    {
        'msgid': 'Abonnement mensuel tout compris par véhicule',
        'en': 'All-inclusive monthly subscription per vehicle',
        'ar': 'اشتراك شهري شامل لكل مركبة',
        'fr': 'Abonnement mensuel tout compris par véhicule'
    },
    {
        'msgid': '/ mois / véhicule (HT)',
        'en': '/ month / vehicle (excl. VAT)',
        'ar': '/ شهر / مركبة (دون احتساب الرسوم)',
        'fr': '/ mois / véhicule (HT)'
    },
    {
        'msgid': 'Hébergement Cloud 99.9% inclus',
        'en': '99.9% Cloud hosting included',
        'ar': 'استضافة سحابية بنسبة جاهزية 99.9% مشمولة',
        'fr': 'Hébergement Cloud 99.9% inclus'
    },
    {
        'msgid': 'Suivi temps réel & Historique 90 jours',
        'en': 'Real-time tracking & 90-day history',
        'ar': 'تتبع فوري مع سجل مسارات لمدة 90 يوماً',
        'fr': 'Suivi temps réel & Historique 90 jours'
    },
    {
        'msgid': 'Applications iOS & Android incluses',
        'en': 'iOS & Android apps included',
        'ar': 'تطبيقات iOS وأندرويد مشمولة',
        'fr': 'Applications iOS & Android incluses'
    },
    {
        'msgid': 'Alertes illimitées (SMS, Email, Push)',
        'en': 'Unlimited alerts (SMS, Email, Push)',
        'ar': 'تنبيهات غير محدودة (رسائل SMS، بريد إلكتروني، إشعارات فورية)',
        'fr': 'Alertes illimitées (SMS, Email, Push)'
    },
    {
        'msgid': 'Mises à jour & support technique',
        'en': 'Updates & technical support',
        'ar': 'تحديثات مستمرة ودعم فني',
        'fr': 'Mises à jour & support technique'
    },
    {
        'msgid': 'Choisir le SaaS',
        'en': 'Choose SaaS',
        'ar': 'اختيار باقة SaaS',
        'fr': 'Choisir le SaaS'
    },
    {
        'msgid': 'Le Plus Choisi • Revendeurs',
        'en': 'Most Popular • Resellers',
        'ar': 'الأكثر طلباً • للموزعين',
        'fr': 'Le Plus Choisi • Revendeurs'
    },
    {
        'msgid': 'Votre propre marque de télématique à 100%',
        'en': 'Your 100% own telematics brand',
        'ar': 'علامتك التجارية الخاصة بالتليماتيك 100%',
        'fr': 'Votre propre marque de télématique à 100%'
    },
    {
        'msgid': '/ mois (Serveur mutualisé PRO)',
        'en': '/ month (PRO Shared Server)',
        'ar': '/ شهر (خادم مشترك احترافي)',
        'fr': '/ mois (Serveur mutualisé PRO)'
    },
    {
        'msgid': 'Votre nom de domaine & logo personnalisés',
        'en': 'Your custom domain name & logo',
        'ar': 'اسم النطاق والشعار الخاص بك',
        'fr': 'Votre nom de domaine & logo personnalisés'
    },
    {
        'msgid': 'Charte graphique adaptée à votre marque',
        'en': 'Custom color palette matched to your brand',
        'ar': 'هوية بصرية وألوان متوافقة مع علامتك التجارية',
        'fr': 'Charte graphique adaptée à votre marque'
    },
    {
        'msgid': 'Apps iOS & Android à votre marque',
        'en': 'iOS & Android apps with your branding',
        'ar': 'تطبيقات iOS وأندرويد باسم علامتك التجارية',
        'fr': 'Apps iOS & Android à votre marque'
    },
    {
        'msgid': 'Gestion multi-clients illimitée',
        'en': 'Unlimited multi-client management',
        'ar': 'إدارة غير محدودة لحسابات الزبائن',
        'fr': 'Gestion multi-clients illimitée'
    },
    {
        'msgid': 'Remises grossistes sur le matériel GPS',
        'en': 'Wholesale hardware discounts',
        'ar': 'خصومات الجملة على أجهزة تتبع GPS',
        'fr': 'Remises grossistes sur le matériel GPS'
    },
    {
        'msgid': 'Support technique prioritaire N2',
        'en': 'Priority Level 2 technical support',
        'ar': 'دعم فني ذو أولوية من المستوى الثاني',
        'fr': 'Support technique prioritaire N2'
    },
    {
        'msgid': 'Lancer ma Marque',
        'en': 'Launch My Brand',
        'ar': 'إطلاق علامتي التجارية',
        'fr': 'Lancer ma Marque'
    },
    {
        'msgid': 'Souveraineté des Données',
        'en': 'Data Sovereignty',
        'ar': 'سيادة وأمان البيانات',
        'fr': 'Souveraineté des Données'
    },
    {
        'msgid': 'Licence Serveur',
        'en': 'Server License',
        'ar': 'ترخيص الخادم',
        'fr': 'Licence Serveur'
    },
    {
        'msgid': 'Licence on-premise sur vos propres infrastructures',
        'en': 'On-premise license on your own infrastructure',
        'ar': 'ترخيص محلي على خوادمك وبنيتك التحتية الخاصة',
        'fr': 'Licence on-premise sur vos propres infrastructures'
    },
    {
        'msgid': '/ licence unique à vie',
        'en': '/ one-time lifetime license',
        'ar': '/ ترخيص دائم لمرة واحدة',
        'fr': '/ licence unique à vie'
    },
    {
        'msgid': 'Paiement unique sans abonnement récurrent',
        'en': 'One-time payment with no recurring subscription',
        'ar': 'دفع لمرة واحدة بدون أي اشتراك دوري',
        'fr': 'Paiement unique sans abonnement récurrent'
    },
    {
        'msgid': 'Hébergé sur vos propres serveurs',
        'en': 'Hosted on your own servers',
        'ar': 'مستضاف على خوادمك الخاصة',
        'fr': 'Hébergé sur vos propres serveurs'
    },
    {
        'msgid': 'Nombre illimité de véhicules & comptes',
        'en': 'Unlimited vehicles and accounts',
        'ar': 'عدد غير محدود من المركبات والحسابات',
        'fr': 'Nombre illimité de véhicules & comptes'
    },
    {
        'msgid': 'Contrôle absolu & sécurité interne',
        'en': 'Absolute control & internal security',
        'ar': 'تحكم مطلق وأمان داخلي كامل',
        'fr': 'Contrôle absolu & sécurité interne'
    },
    {
        'msgid': 'API & accès direct à la base de données',
        'en': 'API & direct database access',
        'ar': 'واجهة برمجة التطبيقات (API) ووصول مباشر لقاعدة البيانات',
        'fr': 'API & accès direct à la base de données'
    },
    {
        'msgid': '1 an de mises à jour & support inclus',
        'en': '1 year of updates & support included',
        'ar': 'سنة واحدة من التحديثات والدعم مشمولة',
        'fr': '1 an de mises à jour & support inclus'
    },
    {
        'msgid': 'Acheter la Licence',
        'en': 'Purchase License',
        'ar': 'شراء الترخيص',
        'fr': 'Acheter la Licence'
    },
    {
        'msgid': 'Grands Comptes & Projets',
        'en': 'Enterprise & Key Accounts',
        'ar': 'المشاريع الكبرى والشركات الضخمة',
        'fr': 'Grands Comptes & Projets'
    },
    {
        'msgid': 'Sur Mesure',
        'en': 'Custom Solution',
        'ar': 'حل مخصص',
        'fr': 'Sur Mesure'
    },
    {
        'msgid': 'Développement spécifique & intégration ERP',
        'en': 'Custom development & ERP integration',
        'ar': 'تطوير خاص وربط متكامل مع أنظمة ERP',
        'fr': 'Développement spécifique & intégration ERP'
    },
    {
        'msgid': 'Sur Devis',
        'en': 'On Quote',
        'ar': 'حسب المقايسة',
        'fr': 'Sur Devis'
    },
    {
        'msgid': '/ cahier des charges personnalisé',
        'en': '/ custom specification sheet',
        'ar': '/ حسب دفتر التحملات المخصص',
        'fr': '/ cahier des charges personnalisé'
    },
    {
        'msgid': 'Intégration ERP & CRM (SAP, Sage, Odoo)',
        'en': 'ERP & CRM integration (SAP, Sage, Odoo)',
        'ar': 'ربط مع أنظمة ERP و CRM (مثل SAP، Sage، Odoo)',
        'fr': 'Intégration ERP & CRM (SAP, Sage, Odoo)'
    },
    {
        'msgid': 'Rapports télématiques personnalisés',
        'en': 'Custom telematics reports',
        'ar': 'تقارير تليماتيك مخصصة',
        'fr': 'Rapports télématiques personnalisés'
    },
    {
        'msgid': 'Intégration capteurs métier spécifiques',
        'en': 'Specialized industrial sensor integration',
        'ar': 'ربط حساسات صناعية خاصة',
        'fr': 'Intégration capteurs métier spécifiques'
    },
    {
        'msgid': 'Protocoles télématiques propriétaires',
        'en': 'Proprietary telematics protocols',
        'ar': 'بروتوكولات اتصال تليماتيك خاصة',
        'fr': 'Protocoles télématiques propriétaires'
    },
    {
        'msgid': 'SLA de support garanti & chef de projet',
        'en': 'Guaranteed support SLA & dedicated project manager',
        'ar': 'اتفاقية مستوى خدمة (SLA) مضمونة ومدير مشروع مخصص',
        'fr': 'SLA de support garanti & chef de projet'
    },
    {
        'msgid': 'Formation technique sur mesure',
        'en': 'Tailored technical training',
        'ar': 'تدريب تقني مخصص',
        'fr': 'Formation technique sur mesure'
    },
    {
        'msgid': 'Étudier mon Projet',
        'en': 'Submit My Project',
        'ar': 'دراسة مشروعي',
        'fr': 'Étudier mon Projet'
    },
    {
        'msgid': 'Tous nos prix sont exprimés en Dirhams marocains (DH) hors taxes. Remises dégressives disponibles selon volume de flotte.',
        'en': 'All prices are quoted in Moroccan Dirhams (DH) excluding VAT. Tiered volume discounts available.',
        'ar': 'جميع الأسعار معروضة بالدرهم المغربي (DH) دون احتساب الرسوم. تخفيضات تفضيلية حسب حجم الأسطول.',
        'fr': 'Tous nos prix sont exprimés en Dirhams marocains (DH) hors taxes. Remises dégressives disponibles selon volume de flotte.'
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
