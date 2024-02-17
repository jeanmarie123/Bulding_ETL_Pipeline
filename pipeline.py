import yaml
from etl.extract import extract_data, extract_localite
from etl.transform import transform_data, table_imo, type_bien

# Import du pipeline de configuration
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

def run_pipeline():

    extra_imo_22_df = extract_data(config_data['imo_22_filepath'], config_data['imo_22_list_colonnes'])
    extra_imo_23_df = extract_data(config_data['imo_23_filepath'], config_data['imo_23_list_colonnes'])
    localite_df = extract_localite(config_data['localite'])

    tranf_imo_22_df = transform_data(extra_imo_22_df)
    tranf_imo_23_df = transform_data(extra_imo_23_df)

    imo_caracteristique_22 = table_imo(tranf_imo_22_df)
    localite_df_22 = type_bien(tranf_imo_22_df)

    imo_caracteristique_23 = table_imo(tranf_imo_22_df)
    localite_df_23 = type_bien(tranf_imo_22_df)


    return tranf_imo_22_df, tranf_imo_23_df, localite_df


if __name__ == "__main__":
    run_pipeline()