import streamlit as st
import json
import os
import datetime

#nome do arquivo JSON
ARQUIVO_DADOS ="pacientes.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", enconding="utf-8") as f:
            return json.load(f)
        return{}


def salvar_dados(dados):
    with open(ARQUIVO_DADOS,"w", encoding="utf-8") as f:
        json.dump (dados, f, ensure_ascii=False, indent=4)

def criar_paciente(nome,cpf, idade, data_nascimento, endereco, planodesaude):
    return{
        "cpf": cpf,
        "nome": nome,
        "data_nascimento":data_nascimento,
        "endereco":endereco,
        "planodesaude": planodesaude
    }








    st.set_page_config( page_title="Cadastro de Pacientes", page_icon="🏥", layout="wide",)

# tem que dar 4 espaços em todo o programa dentro do cadastro, chamdo de indentação.
def cadastrar_paciente():
    

    st.title("CADASTRO PACIENTES")

    st.write("Comece o cadastro")

    data_minima = datetime.date(1980,1,1)
    data_maxima = datetime.date(2100,12,31)

    nome = st.text_input("Nome completo do paciente:")
    cpf = st.number_input('CPF do paciente:',step=1, value=0, format="% d")
    idade = st.number_input('Idade?',step=1, value=0, format="% d")
    data_nascimento = st.date_input('Nascimento?',format="DD/MM/YYYY", min_value=data_minima,max_value=data_maxima)
    endereco = st.text_input('Endereço Completo:')
    planoSaude = st.text_input('Plano de Saúde (Opcional):')

    if st.button("Cadastrar Paciente"):
        # Aqui você pode adicionar a lógica para salvar os dados do paciente
        st.success("Paciente cadastrado com sucesso!")
        st.balloons() # Adiciona um efeito visual de balões ao sucesso


    st.write('Observações sobre o paciente (Alergia, Deficiência...)')
    bio=st.text_area('')

def listar_pacientes():
    pass
def editar_paciente():
    pass
def excluir_paciente():
    pass


#Menu Lateral
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Selecione uma opção:",("Cadastrar Paciente","Listar Pacientes", "Editar Paciente","Excluir Paciente"))

#Navegação entre páginas
if opcao == "Cadastrar Paciente":
    cadastrar_paciente()
elif opcao == "Listar Pacientes":
    listar_pacientes()
elif opcao == "Editar Paciente":
    editar_paciente()
elif opcao == "Excluir Paciente":
    excluir_paciente()

#rodapé
st.sidebar.markdown("---")  
st.sidebar.markdown("Desenvolvido por Maria Sousa")  
st.sidebar.markdown(f"Total de pacientes: ")    






