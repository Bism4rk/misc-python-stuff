import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:\\Users\\reich\\Downloads\\misc-python-stuff\\Learning\\pizzas.csv')

modelo = LinearRegression() 
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x, y) 

st.title('Prevendo o preço de uma pizza com Machine Learning!')
st.divider()
diametro = st.number_input('Qual o diâmetro da pizza?')

if diametro:
    preco = modelo.predict([[diametro]])[0][0]
    st.write(f'O preço da pizza de {diametro} cm é R$ {preco:.2f}!')