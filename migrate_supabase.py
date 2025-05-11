import streamlit as st
from database import db

def main():
    print("Migration de la base de données vers Supabase/PostgreSQL...")
    try:
        db.init_db()
        print("Migration terminée ! Les tables sont créées sur Supabase/PostgreSQL.")
    except Exception as e:
        print("Erreur lors de la migration :", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
