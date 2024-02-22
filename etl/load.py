# import des librairie

import yaml
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# connexion à la base de données
con = psycopg2.connect(
        host = "localhost",
        database = "Immobilier",
        user = "postgres",
        password = "1234"
    )
cur = con.cursor()

# Import du pipeline de configuration
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

def load_data(imo_df_prepared: object, table_name):
    """
        Cette fonction permet de charger les donnees dans la base de données PostgreSQL en fonction des tables
        param:
    """

    # Creation d'une connection avec la base de données postgre
    engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/Immobilier')
    imo_df_prepared.to_sql(table_name, engine, if_exists = 'replace', index = False)
    print(f"Le processus de chargement des données de la table {table_name} est bien terminé.")
