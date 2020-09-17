import streamlit as st
import pandas as pd 

st.title('Bicicletas Públicas Argentina')

DATA_URL = ("https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte/bicicletas-publicas/recorridos-realizados-2020.csv")


def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

#Mensaje de espera
df_state =  st.text("Se están cargando los datos...")

#Se cargan solo 10000
@st.cache
data = load_data(10000)
