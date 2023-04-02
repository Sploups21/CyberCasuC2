# CyberCasuC2

## Support

> Obtenir le code

```bash
$ git clone https://github.com/Sploups21/CyberCasuC2/blob/main/README.md
$ cd Client-C2
```

> Démarrer l'application sous Docker

```bash
$ docker-compose pull   # Télécharger les dépendances
$ docker-compose build  # Installation locale
$ docker-compose up -d  # Démarrer l'application 
```

Visiter `http://localhost:85` dans votre navigateur. L'application devrait être opérationnelle.

<br />

## Structure des fichiers du site 

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # Répertoire principal
   |    |    |-- routes.py                 # Définition des routes principales
   |    |
   |    |-- authentication/                # Gestion des routes d'authentification (login et register)
   |    |    |-- routes.py                 # Définition des routes d'authentification
   |    |    |-- models.py                 # Definition des modèles d'authentification et d'inscription  
   |    |    |-- forms.py                  # Définition des formulaires d'authentification (login et register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # Fichiers CSS, Javascripts, Images, SCSS
   |    |
   |    |-- templates/                     # Modèles utilisés pour charger les pages
   |    |    |-- includes/                 # Morceaux et composants HTML
   |    |    |    |-- navigation.html      # Composant du menu supérieur
   |    |    |    |-- sidebar.html         # Composant de la barre de navigation
   |    |    |    |-- footer.html          # Pied de page de l'application
   |    |    |    |-- scripts.html         # Scripts communs pour les pages
   |    |    |
   |    |    |-- layouts/                   # Pages Maitre
   |    |    |    |-- base-fullscreen.html  # Utilisé par les pages d'authentication 
   |    |    |    |-- base.html             # Utilisé par les pages communes
   |    |    |
   |    |    |-- accounts/                  # Pages d'authentication 
   |    |    |    |-- login.html            # Page Login 
   |    |    |    |-- register.html         # Page Register
   |    |    |
   |    |    |-- home/                      # Pages du kit d'interface utilisateur
   |    |         |-- index.html            # Page principale (index)
   |    |         |-- 404-page.html         # Page d'erreur 404 
   |    |         |-- console.html          # Page console
   |    |         |-- logout.html           # Page logout
   |    |    
   |    config.py                           # Configurer l'application
   |    __init__.py                         # Initialiser l'application
   |
   |-- requirements.txt                     # Modules de développement - stockage SQLite
   |-- requirements-mysql.txt               # Modules de développement  - Mysql DMBS
   |-- requirements-pqsql.txt               # Modules de développement  - PostgreSql DMBS
   |
   |-- Dockerfile                           # Déploiement
   |-- docker-compose.yml                   # Déploiement
   |-- gunicorn-cfg.py                      # Déploiement   
   |-- nginx                                # Déploiement
   |    |-- appseed-app.conf                # Déploiement 
   |
   |-- .env                                 # Injecter la configuration via l'environnement
   |-- run.py                               # Démarrer l'application - Passerelle WSGI
   |
   |-- ************************************************************************
```


