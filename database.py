
import psycopg2
from psycopg2.extras import DictCursor
import hashlib
from datetime import datetime
from config import get_db_config

def adapt_query(query, db_type):
    # Bloc SQLite désactivé pour PostgreSQL
        return query.replace("%s", "?")
    return query

class DatabaseManager:
    def __init__(self):
        self.config = get_db_config()
        self.conn = None
        self.cursor = None

    def connect(self):
        if self.config['db_type'] == 'sqlite':
            # Connexion SQLite supprimée pour PostgreSQL
            self.cursor = self.conn.cursor()
        else:  # PostgreSQL
            self.conn = psycopg2.connect(
                host=self.config['host'],
                port=self.config['port'],
                database=self.config['database'],
                user=self.config['user'],
                password=self.config['password']
            )
            self.cursor = self.conn.cursor(cursor_factory=DictCursor)

    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None

    def init_db(self):
        """Initialise la base de données avec les tables nécessaires."""
        self.connect()
        try:
            # Table utilisateurs
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id SERIAL PRIMARY KEY,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                mot_de_passe TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                date_naissance TEXT,
                genre TEXT,
                telephone TEXT,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')

            # Table entites
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS entites (
                id SERIAL PRIMARY KEY,
                nom TEXT NOT NULL UNIQUE
            )
            ''')

            # Table filieres
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filieres (
                id SERIAL PRIMARY KEY,
                nom TEXT NOT NULL,
                entite_id INTEGER NOT NULL,
                FOREIGN KEY (entite_id) REFERENCES entites (id),
                UNIQUE(nom, entite_id)
            )
            ''')

            # Table sessions
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id SERIAL PRIMARY KEY,
                annee_universitaire TEXT NOT NULL UNIQUE
            )
            ''')

            # Table memoires
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS memoires (
                id SERIAL PRIMARY KEY,
                titre TEXT NOT NULL,
                auteurs TEXT NOT NULL,
                encadreur TEXT NOT NULL,
                resume TEXT,
                fichier_url TEXT NOT NULL,
                tags TEXT,
                filiere_id INTEGER NOT NULL,
                session_id INTEGER NOT NULL,
                version TEXT,
                date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (filiere_id) REFERENCES filieres (id),
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
            ''')

            # Table logs
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                action TEXT NOT NULL,
                user_id INTEGER,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES utilisateurs (id)
            )
            ''')

            # Vérifier si un admin existe déjà
            self.cursor.execute("SELECT COUNT(*) FROM utilisateurs WHERE role='admin'")
            admin_count = self.cursor.fetchone()[0]

            if admin_count == 0:
                # Créer l'admin par défaut
                from config import APP_CONFIG
                admin_password = hashlib.sha256(APP_CONFIG['admin_password'].encode()).hexdigest()
                self.cursor.execute(adapt_query("""
                INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role)
                VALUES (%s, %s, %s, %s, %s)
                """, self.config['db_type']), ('Administrateur', 'System', APP_CONFIG['admin_email'], admin_password, 'admin'))

            self.conn.commit()
        except Exception as e:
            print(f"Erreur lors de l'initialisation de la base de données : {e}")
            self.conn.rollback()
        finally:
            self.close()

    def register_user(self, nom, prenom, email, password, date_naissance, genre, telephone):
        """Inscrit un nouvel utilisateur."""
        self.connect()
        try:
            # Vérifier si l'email existe déjà
            self.cursor.execute(adapt_query("SELECT id FROM utilisateurs WHERE email=%s", self.config['db_type']), (email,))
            if self.cursor.fetchone():
                return False, "Cet email est déjà utilisé."

            # Hash du mot de passe
            hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

            # Insertion du nouvel utilisateur
            self.cursor.execute(adapt_query('''
            INSERT INTO utilisateurs 
            (nom, prenom, email, mot_de_passe, role, date_naissance, genre, telephone) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', self.config['db_type']), (nom, prenom, email, hashed_pwd, "user", date_naissance, genre, telephone))

            self.conn.commit()
            return True, "Inscription réussie !"
        except Exception as e:
            self.conn.rollback()
            return False, f"Erreur lors de l'inscription: {str(e)}"
        finally:
            self.close()

    def check_auth(self, email, password):
        """Vérifie les identifiants de connexion."""
        self.connect()
        try:
            hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
            self.cursor.execute(adapt_query("""
                SELECT id, nom || ' ' || prenom as nom_complet, role 
                FROM utilisateurs 
                WHERE email=%s AND mot_de_passe=%s
            """, self.config['db_type']), (email, hashed_pwd))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de l'authentification : {e}")
            return None
        finally:
            self.close()

    def add_log(self, action, user_id=None):
        """Ajoute une entrée dans les logs."""
        self.connect()
        try:
            self.cursor.execute(
                adapt_query("INSERT INTO logs (action, user_id, date) VALUES (%s, %s, %s)", self.config['db_type']),
                (action, user_id, datetime.now())
            )
            self.conn.commit()
        except Exception as e:
            print(f"Erreur lors de l'ajout du log : {e}")
            self.conn.rollback()
        finally:
            self.close()

# Créer une instance globale du gestionnaire de base de données
db = DatabaseManager() 