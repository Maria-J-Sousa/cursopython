import streamlit as st
import json
import os
import datetime

#nome do arquivo JSON
ARQUIVO_DADOS ="pacientes.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            return json.load(f)
    return{}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS,"w") as f:
        json.dump (dados, f, ensure_ascii=False, indent=4)

def criar_paciente(nome, cpf, idade, data_nascimento, endereco, planodesaude):
    return{
        "cpf": cpf,
        "nome": nome,
        "idade":idade,
        "data_nascimento":data_nascimento,
        "endereco":endereco,
        "planodesaude": planodesaude
    }

st.set_page_config( page_title="Cadastro de Pacientes", page_icon="🏥", layout="wide",)

# tem que dar 4 espaços em todo o programa dentro do cadastro, chamdo de indentação.
def cadastrar_paciente():

    st.title("CADASTRO PACIENTES")

    st.write("Comece o cadastro")

    st.subheader("Cadastrar Novo Paciente")
    
    with st.form(key="form_cadastro"):
        col1, col2 = st.columns(2)
        
        with col1:
            cpf = st.text_input("CPF (somente números)", max_chars=11)
            nome = st.text_input("Nome Completo")
            data_nascimento = st.date_input("Data de Nascimento", min_value=datetime.datetime(1900, 1, 1))
        
        with col2:
            endereco = st.text_input("Endereço")
            planodesaude = st.text_input('Plano de Saúde (Opcional):')
            idade = st.text_input("Idade")
            submit_button = st.form_submit_button("Cadastrar Paciente")

    if submit_button:
        if not cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return
        
        dados = carregar_dados()    
        if cpf in dados:
            st.error("Paciente com este CPF já cadastrado!")
            return
    
        paciente = criar_paciente(
            cpf=cpf,
            nome=nome,
            data_nascimento=data_nascimento.strftime("%d/%m/%Y"),
            endereco=endereco,
            idade=idade,
            planodesaude=planodesaude
            )
            
        dados[cpf] = paciente
        salvar_dados(dados)
            
        st.success("Paciente cadastrado com sucesso!")
        st.balloons()    


def listar_pacientes():

    st.subheader("Lista de Pacientes Cadastrados")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum paciente cadastrado ainda.")
        return
    
    # Filtro por nome
    filtro_nome = st.text_input("Filtrar por nome:")
    
    pacientes_filtrados = []
    for cpf, paciente in dados.items():
        if filtro_nome.lower() in paciente["nome"].lower():
            pacientes_filtrados.append((cpf, paciente))
    
    if not pacientes_filtrados:
        st.warning("Nenhum paciente encontrado com o filtro aplicado.")
        return
    
    for cpf, paciente in pacientes_filtrados:
        with st.expander(f"{paciente['nome']} - CPF: {cpf}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Data de Nascimento:** {paciente['data_nascimento']}")
                st.write(f"**Endereço:** {paciente['endereco']}")
               
def editar_paciente():
    st.subheader("Editar Paciente")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum paciente cadastrado para editar.")
        return
    
    cpf_selecionado = st.selectbox(
        "Selecione o paciente pelo CPF",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    paciente = dados[cpf_selecionado]
    
    with st.form(key="form_edicao"):
        col1, col2 = st.columns(2)
        
        with col1:
            novo_cpf = st.text_input("CPF (somente números)", value=paciente["cpf"], max_chars=11)
            nome = st.text_input("Nome Completo", value=paciente["nome"])
            idade =st.text_input("Idade do Paciente", value=paciente["idade"])
            data_nascimento = st.text_input("Data de Nascimento", value=paciente["data_nascimento"])
            
        with col2:
            endereco = st.text_input("Endereço", value=paciente["endereco"])
        submit_button = st.form_submit_button("Atualizar Paciente")
    
    if submit_button:
        if not novo_cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return
        
        # Se o CPF foi alterado, precisamos verificar se o novo CPF já existe (e não é o mesmo paciente)
        if novo_cpf != cpf_selecionado and novo_cpf in dados:
            st.error("Já existe um paciente com este novo CPF!")
            return
        
        # Remove o paciente antigo se o CPF foi alterado
        if novo_cpf != cpf_selecionado:
            dados.pop(cpf_selecionado)
        
        # Atualiza os dados do paciente
        paciente_atualizado = {
            "cpf": novo_cpf,
            "nome": nome,
            "idade": idade,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
            "data_cadastro": paciente["data_cadastro"]
        }
        
        dados[novo_cpf] = paciente_atualizado
        salvar_dados(dados)
        
        st.success("Paciente atualizado com sucesso!")

def excluir_paciente():
    st.subheader("Excluir Paciente")
    
    dados = carregar_dados()
    
    if dados:
        st.info("Nenhum paciente cadastrado para excluir.")
        return
    
    cpf_selecionado = st.selectbox(
        "Selecione o paciente pelo CPF para excluir",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    paciente = dados[cpf_selecionado]
    
    st.warning("Você está prestes a excluir o seguinte paciente:")
    st.json(paciente)
    
    if st.button("Confirmar Exclusão"):
        dados.pop(cpf_selecionado)
        salvar_dados(dados)
        st.success("Paciente excluído com sucesso!")

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
