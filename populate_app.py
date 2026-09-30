from apps.core.models import MobileApp, AppFeature, AppPlan

# Create MobileApp singleton
app = MobileApp.get_instance()
app.save()

# Create features
features_data = [
    {'title': 'Suivi en Temps Réel', 'description': 'Localisez tous vos véhicules sur une carte interactive avec une actualisation toutes les 10 secondes.', 'icon_class': 'bi bi-geo-alt-fill', 'order': 1},
    {'title': 'Notifications Instantanées', 'description': 'Recevez des alertes push pour les excès de vitesse, les entrées/sorties de zones et les événements moteur.', 'icon_class': 'bi bi-bell-fill', 'order': 2},
    {'title': 'Historique des Trajets', 'description': 'Consultez l\'historique complet des déplacements avec détails de vitesse, arrêts et kilométrage.', 'icon_class': 'bi bi-clock-history', 'order': 3},
    {'title': 'Géo-clôtures Intelligentes', 'description': 'Créez des zones personnalisées et soyez alerté dès qu\'un véhicule entre ou sort de la zone.', 'icon_class': 'bi bi-pentagon-fill', 'order': 4},
    {'title': 'Rapports & Statistiques', 'description': 'Générez des rapports détaillés de consommation, kilométrage et comportement de conduite.', 'icon_class': 'bi bi-bar-chart-fill', 'order': 5},
    {'title': 'Coupure Moteur à Distance', 'description': 'Immobilisez un véhicule à distance en cas de vol ou d\'urgence directement depuis l\'application.', 'icon_class': 'bi bi-shield-lock-fill', 'order': 6},
    {'title': 'Multi-Véhicules', 'description': 'Gérez tous vos véhicules depuis un seul tableau de bord intuitif et facile à utiliser.', 'icon_class': 'bi bi-truck', 'order': 7},
    {'title': 'Mode Hors-Ligne', 'description': 'Consultez les dernières positions connues même sans connexion internet active.', 'icon_class': 'bi bi-wifi-off', 'order': 8},
]
for fd in features_data:
    AppFeature.objects.get_or_create(title=fd['title'], defaults=fd)

# Create plans
plans_data = [
    {'name': 'Gratuit', 'badge': '', 'price': 0, 'period': 'free', 'max_vehicles': '1 véhicule', 'features': 'Suivi en temps réel\nHistorique 24h\nNotifications de base\n1 géo-clôture', 'cta_text': 'Commencer gratuitement', 'order': 1},
    {'name': 'Essentiel', 'badge': 'POPULAIRE', 'price': 49, 'period': 'month', 'max_vehicles': 'Jusqu\'à 5 véhicules', 'features': 'Suivi en temps réel\nHistorique 30 jours\nNotifications avancées\nGéo-clôtures illimitées\nRapports mensuels\nCoupure moteur à distance', 'cta_text': 'Essai gratuit 14 jours', 'is_featured': True, 'order': 2},
    {'name': 'Pro', 'badge': '', 'price': 149, 'period': 'month', 'max_vehicles': 'Jusqu\'à 20 véhicules', 'features': 'Tout dans Essentiel\nHistorique 12 mois\nRapports avancés & export\nContrôle carburant\nMulti-utilisateurs\nAPI d\'intégration\nSupport prioritaire', 'cta_text': 'Essai gratuit 14 jours', 'order': 3},
    {'name': 'Entreprise', 'badge': '', 'price': 0, 'period': 'month', 'max_vehicles': 'Véhicules illimités', 'features': 'Tout dans Pro\nVéhicules illimités\nMarque blanche\nServeur dédié\nFormation sur site\nGestionnaire de compte dédié\nSLA garanti 99.9%', 'cta_text': 'Contactez-nous', 'order': 4},
]
for pd in plans_data:
    AppPlan.objects.get_or_create(name=pd['name'], defaults=pd)

print('Done!')
