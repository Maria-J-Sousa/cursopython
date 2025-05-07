import streamlit as st
import datetime

st.set_page_config(
    page_title="Cadastro de Pacientes",
    page_icon="🏥",
    layout="wide",)


st.title("CADASTRO PACIENTES")

st.write("Comece o cadastro")

data_minima = datetime.date(1980,1,1)
data_maxima = datetime.date(2100,12,31)

nome = st.text_input("Nome completo do paciente:")
documentoPaciente = st.number_input('CPF do paciente:',step=1, value=0, format="% d")
idade = st.number_input('Idade?',step=1, value=0, format="% d")
datNascimento = st.date_input('Nascimento?',format="DD/MM/YYYY", min_value=data_minima,max_value=data_maxima)
endereco = st.text_input('Endereço Completo:')
planoSaude = st.text_input('Plano de Saúde (Opcional):')

if st.button("Cadastrar Paciente"):
    # Aqui você pode adicionar a lógica para salvar os dados do paciente
    st.success("Paciente cadastrado com sucesso!")
    st.balloons() # Adiciona um efeito visual de balões ao sucesso




st.write('Observações sobre o paciente (Alergia, Deficiência...)')
bio=st.text_area('')