# Banque des Mémoires

Application de gestion et consultation des mémoires universitaires.

## Fonctionnalités

- Authentification des utilisateurs (administrateurs et utilisateurs standard)
- Gestion des mémoires universitaires
- Système de favoris
- Gestion des entités et filières
- Système de journalisation (logs)
- Interface utilisateur intuitive et moderne
- Base de données SQLite intégrée

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

L'application utilise une base de données PostgreSQL en production et SQLite en développement local.

### Développement local
- La base de données SQLite est créée automatiquement dans le dossier `data/`
- Les fichiers uploadés sont stockés dans le dossier `uploads/`

### Production (Streamlit Cloud)
- Configurez les variables d'environnement dans les secrets Streamlit
- Utilisez une base de données PostgreSQL externe

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
- SQLite3 : Base de données
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
