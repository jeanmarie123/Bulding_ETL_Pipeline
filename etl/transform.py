import pandas as pd

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

    return imo_df


def table_imo(imo_df: object):
    """  
        Fonction permettant d'avoir une dataframe qui contient les informations des logements.
        param: imo_df :object
        output : imo_caracteristique
    """
    col_imod = ['nombre de lots', 'code type local', 'type local',
                'surface reelle bati', 'nombre pieces principales']
    imo_caracteristique = imo_df.drop(col_imod, axis = 1)
    return imo_caracteristique


def type_bien(imo_df: object):
    """  
        Fonction permettant d'avoir une dataframe qui contient le type des logements.
        param: imo_df :object
        output : carbien_df
    """
    col_log = ['no disposition', 'date mutation', 'nature mutation', 'valeur fonciere',
               'code voie', 'voie', 'code postal', 'commune', 'code departement','code commune']
    carbien_df = imo_df.drop(col_log, axis = 1)
    carbien_df['id_log'] = carbien_df.index
    return carbien_df