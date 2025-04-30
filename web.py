import streamlit as st

st.title("Olá mundo!")

st.write("Hello World! I am back!") #Escrevendo uma frase no navegador # O Write substitui o print"

nome = st.text_input('Qual o seu nome?')
idade = st.number_input('Idade?',step=1, value=0, format="% d")
Dtnascimento = st.date_input('Nasc?')

st.write(f'Olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio=st.text_area('')