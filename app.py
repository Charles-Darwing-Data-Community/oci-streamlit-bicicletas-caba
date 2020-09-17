import streamlit as st
import pandas as pd 

st.title('Bicicletas Públicas Argentina')

DATA_URL = ("https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte/bicicletas-publicas/recorridos-realizados-2020.csv")


def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data