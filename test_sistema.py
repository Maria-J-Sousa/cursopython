#todo arquivo de teste tem que começar com o nome test no nome do arquivo depois coloca _ e o nome que quiser
from cliente import cadastrar_cliente
from emails import gerar_email 

def test_cadastrar_cliente():
    cliente = cadastrar_cliente("joão da silva")
    assert cliente["nome"] == "João Da Silva" #Comando assert vai tretornar verdadeiro ou falso

def test_gerar_email():
    email = gerar_email("MARIA FERNANDA")
    assert email == "Olá. maria fernanda. Seja bem-vindo ao nosso sistema!"