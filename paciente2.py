import streamlit as st
import datetime

# --- Configurações da Página ---
st.set_page_config(
    page_title="Cadastro de Pacientes",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Estilos CSS Personalizados ---
st.markdown(
    """
    <style>
    body {
        color: #333;
        background-color: #f4f4f4;
    }
    .st-header {
        background-color: #007bff !important;
        color: white !important;
        padding: 1.5rem 0;
        border-radius: 5px;
    }
    .st-header h1 {
        color: white !important;
        text-align: center;
    }
    .st-subheader {
        color: #6c757d;
        margin-bottom: 1rem;
        text-align: center;
    }
    .st-text-input > div > div > input {
        border-radius: 5px;
        border: 1px solid #ced4da;
        padding: 0.5rem;
    }
    .st-number-input > div > div > input {
        border-radius: 5px;
        border: 1px solid #ced4da;
        padding: 0.5rem;
    }
    .st-date-input > div > div > input {
        border-radius: 5px;
        border: 1px solid #ced4da;
        padding: 0.5rem;
    }
    .st-text-area > div > div > textarea {
        border-radius: 5px;
        border: 1px solid #ced4da;
        padding: 0.5rem;
        min-height: 100px;
    }
    .st-button > button {
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.75rem 1.5rem;
        cursor: pointer;
    }
    .st-button > button:hover {
        background-color: #218838;
    }
    .info-box {
        background-color: #e9ecef;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
        color: #495057;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Conteúdo Principal ---
st.markdown("<div class='st-header'><h1>Cadastro de Pacientes</h1></div>", unsafe_allow_html=True)
st.markdown("<p class='st-subheader'>Preencha os dados do paciente abaixo:</p>", unsafe_allow_html=True)

data_minima = datetime.date(1900, 1, 1)  # Ajustei a data mínima
data_maxima = datetime.date.today()

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome Completo:")
        documentoPaciente = st.number_input('CPF:', step=1, value=0, format="%d")
        datNascimento = st.date_input('Data de Nascimento:', format="DD/MM/YYYY", min_value=data_minima, max_value=data_maxima)
    with col2:
        idade = st.number_input('Idade:', step=1, value=0, format="%d")
        endereco = st.text_input('Endereço Completo:')
        planoSaude = st.text_input('Plano de Saúde (Opcional):')

st.write("Observações sobre o paciente (Alergia, deficiência..)" \
"")
bio = st.text_area('', height=80)

if st.button("Cadastrar Paciente"):
    # Aqui você pode adicionar a lógica para salvar os dados do paciente
    st.success("Paciente cadastrado com sucesso!")
    st.balloons() # Adiciona um efeito visual de balões ao sucesso

# --- Informações Adicionais (Sidebar) ---
with st.sidebar:
    st.header("Informações")
    st.markdown("Este é um formulário simples para cadastrar pacientes.")
    st.markdown("Preencha todos os campos obrigatórios para realizar o cadastro.")
    st.markdown("Para sugestões de melhorias, entre em contato.")
    st.markdown("---")
    st.markdown(f"**Data Atual:** {datetime.date.today().strftime('%d/%m/%Y')}")