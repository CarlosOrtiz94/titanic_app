# importar librerías
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 
import pickle

#importar archivos

data = pd.read_csv('')
modelo = pickle.load(open('modelo.pickle', 'rb'))

st.title('¿Habrías sobrevivido al Titanic?')



# exploración

st.header('Exploración inicial')

#visualización

#ingreso de datos

#predicción
