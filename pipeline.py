import yaml
from etl.extract import extract_data, extract_localite
from etl.transform import transform_data, table_imo, type_bien
from etl.load import load_data

# Import du pipeline de configuration
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

def run_pipeline():
    
    # Etape 1 : extraction des données
    extra_imo_22_df = extract_data(config_data['imo_22_filepath'], config_data['imo_22_list_colonnes'])
    extra_imo_23_df = extract_data(config_data['imo_23_filepath'], config_data['imo_23_list_colonnes'])
    zone_geographique = extract_localite(config_data['localite'])

    # Etape 2 : transformation des données
    tranf_imo_22_df = transform_data(extra_imo_22_df)
    tranf_imo_23_df = transform_data(extra_imo_23_df)

    caracteristique = table_imo(tranf_imo_22_df)
    imo_caracteristique_23 = table_imo(tranf_imo_23_df) 
    type_logement = type_bien(tranf_imo_22_df)
    type_logement_23 = type_bien(tranf_imo_23_df)

    # Chargement des données
    load_data(zone_geographique, 'zone_geographique')
    load_data(caracteristique, 'caracteristique')
    load_data(type_logement, 'type_logement')



if __name__ == "__main__":
    run_pipeline()