# Banque des Mémoires

Application de gestion et consultation des mémoires universitaires.

## Fonctionnalités

- Authentification des utilisateurs (administrateurs et utilisateurs standard)
- Gestion des mémoires universitaires
- Système de favoris
- Gestion des entités et filières
- Système de journalisation (logs)
- Interface utilisateur intuitive et moderne
- Compatible avec PostgreSQL (Supabase) pour la production
- Base de données SQLite intégrée pour le développement local

## Installation

1. Cloner le dépôt
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancer l'application :
```bash
streamlit run home.py
```

## Configuration

L'application fonctionne automatiquement avec :
- **PostgreSQL/Supabase** (recommandé pour la production, ex. : Streamlit Cloud)
- **SQLite** (par défaut en développement local)

### Développement local
- La base de données SQLite est créée automatiquement dans le dossier `data/`
- Les fichiers uploadés sont stockés dans le dossier `uploads/`

### Production (Streamlit Cloud ou Supabase)
- Configurez les variables de connexion dans `.streamlit/secrets.toml` :
```toml
db_type = "postgresql"
db_host = "<hôte_supabase>"
db_port = "5432"
db_name = "<nom_db>"
db_user = "<utilisateur>"
db_password = "<mot_de_passe>"
```
- Les tables seront créées automatiquement à la première exécution de l'application.
- Utilisez une base PostgreSQL dédiée (évitez d'utiliser la base "postgres" par défaut).

## Utilisation

1. Lancez l'application :
```bash
streamlit run home.py
```

2. Accédez à l'application dans votre navigateur (par défaut : http://localhost:8501)

## Structure du projet

- `home.py` : Application principale Streamlit
- `database.py` : Gestionnaire de base de données SQLite
- `storage.py` : Gestionnaire de stockage des fichiers
- `requirements.txt` : Dépendances du projet
- `data/` : Dossier contenant la base de données et les fichiers uploadés
  - `memoires_db.sqlite` : Base de données SQLite
  - `memoires/` : Stockage des fichiers PDF

## Déploiement

1. Créez un nouveau dépôt sur GitHub

2. Initialisez Git et poussez le code :
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/votre-username/banque-des-memoires.git
git push -u origin main
```

## Dépendances principales

- Streamlit : Interface utilisateur web
- psycopg2-binary : Connexion PostgreSQL/Supabase
- SQLite3 : Base de données locale
- Pandas : Manipulation des données
- PyPDF2 : Gestion des fichiers PDF

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
