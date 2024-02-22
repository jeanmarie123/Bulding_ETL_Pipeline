import pandas as pd


col_rename = {"no disposition": "no_disposition", "date mutation": "date_mutation", "nature mutation": "nature_mutation", "valeur fonciere": "valeur_fonciere", 
              "code voie": "code_voie", "code postal": "code_postal", "code departement": "code_departement", "code commune": "code_commune", "nombre de lots": "nombre_de_lots", 
              "code type local": "code_type_local", "type local": "type_local", "surface reelle bati": "surface_reelle_bati", "nombre pieces principales": "nombre_pieces"}

def transform_data(imo_df):
    """
        Fonction permettant de transformer les données en réalisant plusieurs opérations (suppression ..)
        parametre : imo_df, c'est le detaframe qui a été extrait.
        output: dataframe netoyer. 
    """
    col_drop = ['No Volume', '1er lot', 'Surface Carrez du 1er lot', '2eme lot', 
                'Surface Carrez du 2eme lot', '3eme lot', 'Surface Carrez du 3eme lot', 
                '4eme lot', 'Surface Carrez du 4eme lot', '5eme lot', 'Surface Carrez du 5eme lot']
    
        # Suppression des colonnes ayant près de 96% des données manquantes
    imo_df = imo_df.drop(col_drop, axis = 1)

        # Converstion du type des colonnes et transformation des noms en miniscule
    imo_df['Date mutation'] = pd.to_datetime(imo_df['Date mutation'], format ='%d/%m/%Y')
    imo_df['Valeur fonciere'] = imo_df['Valeur fonciere'].str.replace(',', '.')
    imo_df['Valeur fonciere'] = imo_df['Valeur fonciere'].astype(float)
    imo_df.columns = imo_df.columns.str.lower()
    imo_df = imo_df.rename(columns = col_rename)

    print(f"Le fichier de données {imo_df} a été transformé correctement.")

    return imo_df


def table_imo(imo_df: object):
    """  
        Fonction permettant d'avoir une dataframe qui contient les informations des logements.
        param: imo_df :object
        output : imo_caracteristique
    """
    col_imod = ['nombre_de_lots', 'code_type_local', 'type_local',
                'surface_reelle_bati', 'nombre_pieces']
    imo_caracteristique = imo_df.drop(col_imod, axis = 1)
    imo_caracteristique['id_log'] = imo_caracteristique.index
    return imo_caracteristique


def type_bien(imo_df: object):
    """  
        Fonction permettant d'avoir une dataframe qui contient le type des logements.
        param: imo_df :object
        output : carbien_df
    """
    col_log = ['no_disposition', 'date_mutation', 'nature_mutation', 'valeur_fonciere',
               'code_voie', 'voie', 'code_postal', 'commune', 'code_departement','code_commune']
    carbien_df = imo_df.drop(col_log, axis = 1)
    carbien_df['id_log'] = carbien_df.index
    return carbien_df