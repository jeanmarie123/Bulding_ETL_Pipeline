import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# connexion à la base de données
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/Immobilier')
pgcon = engine.connect()

# Nom des tables
z_g = 'zone_geographique'
t_l = 'type_logement'
c_a = 'caracteristique'

def read_data(nom_table):
    """ 
        Fonction permettant de lire les tables de données dans une base de données postgresql
        param: nom de la table de données
        output: table de données lue
    """
    data = pd.read_sql_query(f'SELECT * FROM {nom_table}', engine)
    return data