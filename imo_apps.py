import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import os 
import warnings
from analytics.analyse import *
warnings.filterwarnings('ignore')

# Titre de la page via le web
st.set_page_config(page_title = "Dashboad imo France", page_icon = ":bar_chart:", layout = "wide")

st.subheader(" :bar_chart: Tendance de l'immobilier en France ")

z_g = 'zone_geographique'
t_l = 'type_logement'
c_a = 'caracteristique'

df = read_data(z_g)

tab1, tab2 = st.tabs(["Cat", "Dog"])

with tab1:
    input_text = st.text_area(label = "entrez votre input")
    st.write(input_text)
    st.dataframe(df)


with tab2:
    input_v = st.text_area(label = "entrez votre code")
    st.write(input_v)
    st.dataframe(df)




