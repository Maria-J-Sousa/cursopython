import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 900, 650
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 50, 50)
VERDE = (50, 255, 50)
AZUL = (50, 150, 255)
AMARELO = (255, 255, 0)
CINZA = (100, 100, 100)
MADEIRA = (139, 69, 19)

# Fontes
try:
    fonte_grande = pygame.font.SysFont('calibri', 50, bold=True)
    fonte_media = pygame.font.SysFont('calibri', 40)
    fonte_pequena = pygame.font.SysFont('calibri', 30)
except:
    fonte_grande = pygame.font.SysFont('arial', 50, bold=True)
    fonte_media = pygame.font.SysFont('arial', 40)
    fonte_pequena = pygame.font.SysFont('arial', 30)

# Palavras e dicas
palavras = {
    "Animais": [
        ("GIRAFA", "Tem o mesmo número de vértebras no pescoço que humanos"),
        ("ELEFANTE", "Maior animal terrestre vivo"),
        ("TUBARÃO", "Existe há mais de 400 milhões de anos")
    ],
    "Países": [
        ("BRASIL", "Maior país da América do Sul"),
        ("JAPÃO", "Terra do sol nascente"),
        ("CANADÁ", "Tem a maior costa do mundo")
    ],
    "Esportes": [
        ("FUTEBOL", "Esporte mais popular do mundo"),
        ("BASQUETE", "Criado por James Naismith em 1891"),
        ("TÊNIS", "Wimbledon é o torneio mais antigo")
    ]
}

mensagens_divertidas = [
    "Quase lá! Tente novamente!",
    "Você pode fazer melhor!",
    "Não desista!",
    "A próxima você acerta!",
    "Continue tentando!"
]

def desenhar_forca(erros):
    # Base
    pygame.draw.rect(tela, MADEIRA, (100, 500, 200, 20))
    # Poste
    pygame.draw.rect(tela, MADEIRA, (175, 200, 20, 300))
    # Topo
    pygame.draw.rect(tela, MADEIRA, (175, 200, 150, 20))
    # Corda
    pygame.draw.line(tela, CINZA, (325, 200), (325, 230), 3)
    
    # Boneco
    if erros >= 1:  # Cabeça
        pygame.draw.circle(tela, BRANCO, (325, 255), 25, 3)
    if erros >= 2:  # Corpo
        pygame.draw.line(tela, BRANCO, (325, 280), (325, 380), 3)
    if erros >= 3:  # Braço esquerdo
        pygame.draw.line(tela, BRANCO, (325, 300), (295, 330), 3)
    if erros >= 4:  # Braço direito
        pygame.draw.line(tela, BRANCO, (325, 300), (355, 330), 3)
    if erros >= 5:  # Perna esquerda
        pygame.draw.line(tela, BRANCO, (325, 380), (295, 430), 3)
    if erros >= 6:  # Perna direita
        pygame.draw.line(tela, BRANCO, (325, 380), (355, 430), 3)

def desenhar_botao(texto, retangulo, cor, cor_hover):
    pos_mouse = pygame.mouse.get_pos()
    cor_atual = cor_hover if retangulo.collidepoint(pos_mouse) else cor
    
    pygame.draw.rect(tela, cor_atual, retangulo, border_radius=10)
    pygame.draw.rect(tela, BRANCO, retangulo, 2, border_radius=10)
    
    texto_surf = fonte_pequena.render(texto, True, BRANCO)
    tela.blit(texto_surf, (retangulo.centerx - texto_surf.get_width()//2, 
                          retangulo.centery - texto_surf.get_height()//2))
    
    return retangulo.collidepoint(pos_mouse)

def jogo_principal():
    relogio = pygame.time.Clock()
    
    # Selecionar palavra aleatória
    tema = random.choice(list(palavras.keys()))
    palavra, dica = random.choice(palavras[tema])
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 0
    fim_de_jogo = False
    vitoria = False
    
    executando = True
    while executando:
        tela.fill(PRETO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            
            if not fim_de_jogo and evento.type == pygame.KEYDOWN:
                if evento.key >= pygame.K_a and evento.key <= pygame.K_z:
                    letra = chr(evento.key).upper()
                    if letra not in letras_corretas and letra not in letras_erradas:
                        if letra in palavra:
                            letras_corretas.add(letra)
                            if all(l in letras_corretas for l in palavra):
                                fim_de_jogo = True
                                vitoria = True
                        else:
                            letras_erradas.add(letra)
                            tentativas += 1
                            if tentativas >= 6:
                                fim_de_jogo = True
                                vitoria = False
            
            if fim_de_jogo and evento.type == pygame.MOUSEBUTTONDOWN:
                if 'botao_reiniciar' in locals() and botao_reiniciar.collidepoint(evento.pos):
                    return True
        
        # Desenhar título
        titulo = fonte_grande.render("JOGO DA FORCA", True, AZUL)
        tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 30))
        
        # Desenhar tema e dica
        tema_texto = fonte_pequena.render(f"Tema: {tema} - Dica: {dica}", True, BRANCO)
        tela.blit(tema_texto, (LARGURA//2 - tema_texto.get_width()//2, 100))
        
        # Desenhar forca
        desenhar_forca(tentativas)
        
        # Desenhar palavra com espaçamento
        palavra_mostrada = " ".join([letra if letra in letras_corretas else "_" for letra in palavra])
        palavra_surf = fonte_media.render(palavra_mostrada, True, AMARELO)
        tela.blit(palavra_surf, (LARGURA//2 - palavra_surf.get_width()//2, 450))
        
        # Letras erradas
        if letras_erradas:
            erradas_texto = fonte_pequena.render("Letras erradas: " + ", ".join(letras_erradas), True, VERMELHO)
            tela.blit(erradas_texto, (50, 550))
        
        # Tentativas
        tentativas_texto = fonte_pequena.render(f"Erros: {tentativas}/6", True, BRANCO)
        tela.blit(tentativas_texto, (LARGURA - 200, 550))
        
        # Fim de jogo
        if fim_de_jogo:
            overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            tela.blit(overlay, (0, 0))
            
            if vitoria:
                resultado = fonte_grande.render("VOCÊ GANHOU!", True, VERDE)
                tela.blit(resultado, (LARGURA//2 - resultado.get_width()//2, 250))
            else:
                resultado = fonte_grande.render("FIM DE JOGO", True, VERMELHO)
                tela.blit(resultado, (LARGURA//2 - resultado.get_width()//2, 250))
                
                resposta = fonte_media.render(f"Palavra: {palavra}", True, BRANCO)
                tela.blit(resposta, (LARGURA//2 - resposta.get_width()//2, 320))
                
                mensagem = fonte_pequena.render(random.choice(mensagens_divertidas), True, AMARELO)
                tela.blit(mensagem, (LARGURA//2 - mensagem.get_width()//2, 370))
            
            # Botão de reiniciar
            botao_reiniciar = pygame.Rect(LARGURA//2 - 120, 450, 240, 60)
            if desenhar_botao("JOGAR NOVAMENTE", botao_reiniciar, AZUL, VERDE):
                pygame.draw.rect(tela, BRANCO, botao_reiniciar, 3, border_radius=10)
        
        pygame.display.flip()
        relogio.tick(30)
    
    return False

# Iniciar jogo
if __name__ == "__main__":
    reiniciar = True
    while reiniciar:
        reiniciar = jogo_principal()
    
    pygame.quit()
    sys.exit()