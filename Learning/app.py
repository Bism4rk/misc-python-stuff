import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:\\Users\\reich\\Downloads\\misc-python-stuff\\Learning APIs\\pizzas.csv')

modelo = LinearRegression() 
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x, y) 

st.title('Prevendo o preço de uma pizza')