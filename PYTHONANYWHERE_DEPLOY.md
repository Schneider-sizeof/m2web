# Guide de Déploiement M2web Maroc sur PythonAnywhere

Ce guide détaille pas-à-pas la procédure pour héberger votre projet Django **M2web Maroc** sur **PythonAnywhere** en moins de 5 minutes.

---

## 📋 Prérequis & Identifiants Inclus

- Compte PythonAnywhere : Gratuit ou Débutant (https://www.pythonanywhere.com)
- Dépôt GitHub : https://github.com/Schneider-sizeof/m2web
- **Superutilisateur Admin pré-configuré** :
  - **Identifiant :** `m2web`
  - **Mot de passe :** `adminm2web`
  - **URL Admin :** `https://<votre_nom_utilisateur>.pythonanywhere.com/admin/`

---

## Étape 1 : Ouvrir une console Bash sur PythonAnywhere

1. Connectez-vous à votre compte sur [PythonAnywhere](https://www.pythonanywhere.com).
2. Rendez-vous dans l'onglet **Consoles**.
3. Sous la section **Start a new console**, cliquez sur **Bash**.

---

## Étape 2 : Cloner le projet depuis GitHub

Dans la console Bash, exécutez la commande suivante :

```bash
git clone https://github.com/Schneider-sizeof/m2web.git
cd m2web
```

---

## Étape 3 : Créer et activer l'environnement virtuel (Virtualenv)

Créez un environnement virtuel Python 3.10 ou 3.11 :

```bash
mkvirtualenv --python=/usr/bin/python3.10 m2web-env
```

*(Si `mkvirtualenv` n'est pas disponible, vous pouvez utiliser :)*
```bash
python3.10 -m venv ~/.virtualenvs/m2web-env
source ~/.virtualenvs/m2web-env/bin/activate
```

Installez les dépendances du projet :

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Étape 4 : Appliquer les migrations & rassembler les fichiers statiques

Exécutez les commandes suivantes toujours dans le dossier `~/m2web` avec l'environnement virtuel activé :

```bash
python manage.py migrate --settings=m2web_project.settings.pythonanywhere
python manage.py collectstatic --noinput --settings=m2web_project.settings.pythonanywhere
```

> **Note :** La base de données `db.sqlite3` contient déjà toutes les données (produits, services, partenaires, témoignages, coordonnées) ainsi que le superutilisateur `m2web` / `adminm2web`.  
> Si vous souhaitez recharger les données initiales à tout moment, lancez :
> ```bash
> python manage.py loaddata data_export.json --settings=m2web_project.settings.pythonanywhere
> ```

---

## Étape 5 : Configurer l'application Web sur PythonAnywhere

1. Allez dans l'onglet **Web** de votre tableau de bord PythonAnywhere.
2. Si vous n'avez pas encore d'application web, cliquez sur **Add a new web app**, choisissez **Manual configuration** (ne choisissez pas Django automatique), puis sélectionnez **Python 3.10**.
3. Configurez les chemins suivants :
   - **Source code** : `/home/<votre_username>/m2web`
   - **Working directory** : `/home/<votre_username>/m2web`
   - **Virtualenv** : `/home/<votre_username>/.virtualenvs/m2web-env`

---

## Étape 6 : Configurer le fichier WSGI

Dans l'onglet **Web**, sous la section **Code**, cliquez sur le lien du fichier **WSGI configuration file** (ex: `/var/www/<votre_username>_pythonanywhere_com_wsgi.py`).

Effacez tout le contenu existant et collez-y :

```python
import os
import sys

# Remplacez YOUR_USERNAME par votre nom d'utilisateur PythonAnywhere exact
username = 'YOUR_USERNAME'
project_home = f'/home/{username}/m2web'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'm2web_project.settings.pythonanywhere'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

*(Pensez à remplacer `YOUR_USERNAME` par votre nom d'utilisateur PythonAnywhere)*.  
Cliquez sur **Save** en haut à droite.

---

## Étape 7 : Configurer les dossiers statiques & médias

Dans l'onglet **Web**, faites défiler vers le bas jusqu'à la section **Static files** et ajoutez ces deux entrées :

| URL | Directory |
|---|---|
| `/static/` | `/home/<votre_username>/m2web/staticfiles` |
| `/media/` | `/home/<votre_username>/m2web/media` |

*(Remplacez `<votre_username>` par votre vrai nom d'utilisateur PythonAnywhere).*

---

## Étape 8 : Recharger le site & Tester !

1. En haut de l'onglet **Web**, cliquez sur le grand bouton vert **Reload <votre_username>.pythonanywhere.com**.
2. Ouvrez votre site à l'adresse :
   ```text
   https://<votre_username>.pythonanywhere.com
   ```
3. Connectez-vous au panneau d'administration :
   ```text
   https://<votre_username>.pythonanywhere.com/admin/
   Identifiant : m2web
   Mot de passe : adminm2web
   ```

Toutes les sections du site (barre supérieure, téléphone, WhatsApp, hero, statistiques, piliers, services, traceurs GPS, bannières, avis, coordonnées) sont modifiables directement depuis le tableau de bord !
