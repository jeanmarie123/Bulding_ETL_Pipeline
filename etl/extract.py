import pandas as pd

def extract_data(filepath: object, col_select: list) -> object:
    """ 
        Fonction permettant de faire l extraction des donnees.
        parametre: - filepath de type str, lien de donnees sous format txt,
                   - liste des colonnes qu on veut avoir
        output: dataframe pandas extrait a partir du fichier de donnees txt
    """

    try:

        # lire les donnees puis les stocker 
        imo_df = pd.read_csv(filepath, delimiter = "|", low_memory = False)
        imo_df = imo_df[col_select]

        print(f"les données ont été bien extrait : {filepath}")
    
    # Gerer les exceptions si les fichiers manquent
    except FileNotFoundError as e:
        print(f" Erreur lors de l'extraction du fichier : {e}")

    except Exception as e: 
        print(f"Erreur : {e}")   

    return imo_df