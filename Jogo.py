#pyGame é uma biblioteca de jogo. Pedir para a IA ""

import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Fonte
fonte = pygame.font.Font(None, 36)

# Lista de palavras e dicas
palavras = {
    "python": "Uma linguagem de programação popular.",
    "pygame": "Uma biblioteca para desenvolvimento de jogos em Python.",
    "computador": "Uma máquina eletrônica que processa dados.",
    "teclado": "Um dispositivo de entrada para digitar texto.",
    "mouse": "Um dispositivo de entrada para controlar o cursor na tela.",
    "monitor": "Um dispositivo de saída que exibe imagens e texto.",
    "internet": "Uma rede global de computadores.",
    "jogo": "Uma atividade divertida com regras.",
    "programacao": "O processo de escrever código para computadores.",
    "desenvolvimento": "O processo de criar software ou jogos."
}

# Função para escolher uma palavra aleatória
def escolher_palavra():
    palavra = random.choice(list(palavras.keys()))
    dica = palavras[palavra]
    return palavra, dica

# Função para exibir texto na tela
def exibir_texto(texto, cor, posicao):
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, posicao)

# Função principal do jogo
def jogo():
    palavra, dica = escolher_palavra()
    tentativas = 3
    acertou = False

    while tentativas > 0 and not acertou:
        tela.fill(branco)
        exibir_texto(f"Dica: {dica}", preto, (50, 50))
        exibir_texto(f"Tentativas restantes: {tentativas}", preto, (50, 100))
        exibir_texto("Digite sua tentativa:", preto, (50, 150))

        pygame.display.flip()

        # Obter a tentativa do jogador
        tentativa = ""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.KEYDOWN:
                    if evento.unicode.isalpha():
                        tentativa += evento.unicode
                    elif evento.key == pygame.K_RETURN:
                        break

            tela.fill(branco)
            exibir_texto(f"Dica: {dica}", preto, (50, 50))
            exibir_texto(f"Tentativas restantes: {tentativas}", preto, (50, 100))
            exibir_texto("Digite sua tentativa:", preto, (50, 150))
            exibir_texto(tentativa, preto, (50, 200))
            pygame.display.flip()

        # Verificar se a tentativa está correta
        if tentativa.lower() == palavra:
            acertou = True
            tela.fill(branco)
            exibir_texto("Parabéns! Você acertou!", verde, (largura_tela // 2 - 150, altura_tela // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
        else:
            tentativas -= 1
            tela.fill(branco)
            exibir_texto("Incorreto! Tente novamente.", vermelho, (largura_tela // 2 - 150, altura_tela // 2))
            pygame.display.flip()
            pygame.time.delay(2000)

    # Exibir mensagem de fim de jogo
    tela.fill(branco)
    if acertou:
        exibir_texto("Você acertou!", verde, (largura_tela // 2 - 100, altura_tela // 2))
    else:
        exibir_texto(f"Você perdeu! A palavra era: {palavra}", vermelho, (largura_tela // 2 - 150, altura_tela // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

    # Perguntar se o jogador quer jogar novamente
    while True:
        tela.fill(branco)
        exibir_texto("Jogar novamente? (S/N)", preto, (largura_tela // 2 - 150, altura_tela // 2))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.unicode.lower() == "s":
                    jogo()
                    return
                elif evento.unicode.lower() == "n":
                    pygame.quit()
                    return

# Iniciar o jogo
jogo()