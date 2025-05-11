import os
import streamlit as st

def get_db_config():
    """Retourne la configuration de la base de données selon l'environnement."""
    if st.secrets.get("db_type") == "postgresql":
        # Configuration PostgreSQL pour Streamlit Cloud
        return {
            'db_type': 'postgresql',
            'host': st.secrets["db_host"],
            'port': st.secrets["db_port"],
            'database': st.secrets["db_name"],
            'user': st.secrets["db_user"],
            'password': st.secrets["db_password"]
        }
    else:
        # Configuration SQLite pour le développement local
        return {
            'db_type': 'sqlite',
            'db_path': 'data/memoires_db.sqlite'
        }

# Configuration de l'application
APP_CONFIG = {
    'app_name': 'Banque des Mémoires',
    'app_icon': '📚',
    'admin_email': 'admin@universite.com',
    'admin_password': 'admin123',
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'allowed_extensions': ['.pdf'],
    'upload_folder': 'uploads'
}

# Créer le dossier de données si nécessaire
if not os.path.exists('data'):
    os.makedirs('data')

# Créer le dossier d'uploads si nécessaire
if not os.path.exists(APP_CONFIG['upload_folder']):
    os.makedirs(APP_CONFIG['upload_folder'])

# Configuration PostgreSQL
DB_CONFIG = {
    "dbname": "memoires_db",
    "user": "postgres",
    "password": "votre_mot_de_passe",  # À changer
    "host": "localhost",
    "port": "5432"
}

# Configuration AWS S3
AWS_CONFIG = {
    "aws_access_key_id": "votre_access_key",  # À changer
    "aws_secret_access_key": "votre_secret_key",  # À changer
    "region_name": "eu-west-3",  # Par exemple, Europe (Paris)
    "bucket_name": "memoires-unstim"
}

# Autres configurations
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
ALLOWED_EXTENSIONS = {'pdf'} 