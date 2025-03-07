# Projet Django : Navigateur web / web crawler

## Description du Projet

Ce projet Django, qui s'appelle **django-navigateur**, est un navigateur web / web crawler qui permet aux utilisateurs de rechercher et d'explorer des pages web. Après la création d'un compte et la connexion, l'utilisateur accède à une interface où il peut saisir une URL. Le projet extrait ensuite des informations clés de la page HTML, telles que les liens internes, les liens externes, les images, et les tableaux. Un historique des recherches est également sauvegardé, affichant la date et l'heure des requêtes précédentes. En bas de la page, l'utilisateur peut consulter les caractéristiques et l'historique des pages web visitées. Un graphique interactif montre le nom de domaine au centre, avec les liens internes à droite et les liens externes à gauche, offrant ainsi une vue d'ensemble visuelle des relations entre les pages.

## Structure du Projet

Le projet est structuré comme suit :

```plaintext 
django-navigateur/
│
├── browser/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── validators.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   ├── browser/
│   │   │   ├── home.css
│   │   │   ├── script.js
│   │   │   └── style.css
│   │   └── fonts/
│   ├── templates/
│   │   └── browser/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       └── registration.html
│   └── __pycache__/
│
├── navigateur/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
│
├── staticfiles/
│   ├── admin/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   ├── browser/
│   │   ├── home.css
│   │   ├── script.js
│   │   └── style.css
│   └── fonts/
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```


## Installation et Configuration

### Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)

### Étapes pour lancer le projet

1. **Cloner le dépôt GitHub** :

   ```bash
   git clone https://github.com/DaSilvaThomas/django-navigateur.git
   ```
   ```bash
   cd django-navigateur
   ```

2. **Créer un environnement virtuel** :

    ```bash
    python -m venv env
    ```

3. **Activer l'environnement virtuel** :

- Sur Windows :
    ```bash
    env\Scripts\activate
    ```

- Sur macOS/Linux :
    ```bash
    source env/bin/activate
    ```

4. **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

5. **Configurer la base de données** :

    Le projet utilise SQLite par défaut. Vous pouvez exécuter les migrations pour créer la base de données :
    ```bash
    python manage.py migrate
    ```
    
6. **(Optionnel) Créer un compte superutilisateur** :

   Si vous souhaitez accéder à l'interface d'administration Django, vous pouvez créer un compte superutilisateur en ligne de commande :
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancer le serveur de développement** :

    ```bash
    python manage.py runserver
    ```

8. **Accéder à l'application** :

    Ouvrez votre navigateur et accédez à http://localhost:8000/login/ pour la page de connexion.


## Fichiers Importants

- settings.py : Contient les configurations du projet, y compris les paramètres de sécurité.
- urls.py : Définit les routes URL de l'application et les associe aux vues correspondantes.
- models.py : Contient la définition des modèles de base de données.
- views.py : Contient les vues pour la connexion, la déconnexion, l'inscription et la page d'accueil.
- forms.py : Définit les formulaires de connexion et d'inscription.
- validators.py : Contient le validateur personnalisé pour la complexité des mots de passe.
- templates/ : Contient les templates HTML pour les pages de connexion, d'inscription et d'accueil.
- static/ : Contient les fichiers static du projet.
