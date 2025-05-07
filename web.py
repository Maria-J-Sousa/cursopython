import streamlit as st
import datetime

st.title("Olá mundo!")

st.write("Hello World! I am back!") #Escrevendo uma frase no navegador # O Write substitui o print"

data_minima = datetime.date(1980,1,1)
data_maxima = datetime.date(2100,12,31)

nome = st.text_input('Qual o seu nome?')
idade = st.number_input('Idade?',step=1, value=0, format="% d")
dataNascimento = st.date_input('Nasc?',format="DD/MM/YYYY", min_value=data_minima,max_value=data_maxima)

st.write(f'Olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio=st.text_area('')

#pra rodar na web : escrever no terminal 'STREAMLIT RUN web.py'