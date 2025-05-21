from util import formata_nome   

def gerar_email(nome: str) -> str:
    nome_formatado = formata_nome(nome)
    return f"Olá, {nome_formatado}. Seja bem-vindo!" 