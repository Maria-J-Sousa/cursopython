import pygame
import random
import sys
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 1000, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca Premium")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (231, 76, 60)
VERDE = (46, 204, 113)
AZUL = (52, 152, 219)
ROXO = (155, 89, 182)
AMARELO = (241, 196, 15)
CINZA = (120, 120, 120)
MADEIRA = (160, 82, 45)

# Gradiente de fundo
def desenhar_fundo():
    for y in range(ALTURA):
        # Interpolação linear para gradiente
        r = int(10 + (y/ALTURA)*50)
        g = int(20 + (y/ALTURA)*30)
        b = int(30 + (y/ALTURA)*40)
        pygame.draw.line(tela, (r, g, b), (0, y), (LARGURA, y))

# Fontes
try:
    fonte_titulo = pygame.font.Font("calibri.ttf", 60)
    fonte_palavra = pygame.font.Font("calibri.ttf", 48)
    fonte_curiosidade = pygame.font.Font("calibri.ttf", 28)
    fonte_normal = pygame.font.Font("calibri.ttf", 32)
    fonte_pequena = pygame.font.Font("calibri.ttf", 24)
except:
    fonte_titulo = pygame.font.SysFont('arial', 60, bold=True)
    fonte_palavra = pygame.font.SysFont('arial', 48)
    fonte_curiosidade = pygame.font.SysFont('arial', 28)
    fonte_normal = pygame.font.SysFont('arial', 32)
    fonte_pequena = pygame.font.SysFont('arial', 24)

# Banco de palavras e curiosidades
banco_palavras = {
    "Animais": [
        ("GIRAFA", "As girafas dormem apenas 30 minutos por dia em pequenos cochilos"),
        ("ELEFANTE", "Os elefantes podem reconhecer a si mesmos no espelho"),
        ("TUBARÃO", "Alguns tubarões podem viver mais de 100 anos")
    ],
    "Países": [
        ("BRASIL", "O Brasil tem a maior biodiversidade do planeta"),
        ("JAPÃO", "No Japão existem mais de 5 milhões de máquinas de venda automática"),
        ("CANADÁ", "O Canadá tem mais lagos que todos os outros países juntos")
    ],
    "Ciência": [
        ("DIAMANTE", "Diamantes podem queimar a 900°C"),
        ("VULCÃO", "O maior vulcão do sistema solar fica em Marte"),
        ("TARDÍGRADO", "Tardígrados podem sobreviver no vácuo do espaço")
    ]
}

# Efeitos visuais
class EfeitoParticula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tamanho = random.randint(2, 5)
        self.cor = random.choice([VERDE, AMARELO, AZUL, ROXO])
        self.vel_x = random.uniform(-1, 1)
        self.vel_y = random.uniform(-3, -1)
        self.tempo_vida = 30

    def atualizar(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.tempo_vida -= 1
        return self.tempo_vida > 0

    def desenhar(self, superficie):
        pygame.draw.circle(superficie, self.cor, (int(self.x), int(self.y)), self.tamanho)

def desenhar_forca(erros):
    # Base
    pygame.draw.rect(tela, MADEIRA, (150, 550, 250, 20), border_radius=5)
    # Poste
    pygame.draw.rect(tela, MADEIRA, (275, 250, 25, 300), border_radius=5)
    # Topo
    pygame.draw.rect(tela, MADEIRA, (275, 250, 175, 25), border_radius=5)
    # Corda
    pygame.draw.line(tela, CINZA, (450, 250, 450, 290), 4)
    
    # Boneco
    if erros >= 1:  # Cabeça
        pygame.draw.circle(tela, BRANCO, (450, 320), 30, 3)
    if erros >= 2:  # Corpo
        pygame.draw.line(tela, BRANCO, (450, 350, 450, 450), 4)
    if erros >= 3:  # Braço esquerdo
        pygame.draw.line(tela, BRANCO, (450, 380, 410, 420), 4)
    if erros >= 4:  # Braço direito
        pygame.draw.line(tela, BRANCO, (450, 380, 490, 420), 4)
    if erros >= 5:  # Perna esquerda
        pygame.draw.line(tela, BRANCO, (450, 450, 410, 500), 4)
    if erros >= 6:  # Perna direita
        pygame.draw.line(tela, BRANCO, (450, 450, 490, 500), 4)

def animar_vitoria():
    particulas = []
    for _ in range(100):
        particulas.append(EfeitoParticula(random.randint(0, LARGURA), random.randint(0, ALTURA)))
    
    for _ in range(60):  # 1 segundo de animação
        desenhar_fundo()
        
        # Atualizar e desenhar partículas
        for p in particulas[:]:
            if not p.atualizar():
                particulas.remove(p)
            else:
                p.desenhar(tela)
        
        pygame.display.flip()
        pygame.time.delay(16)  # ~60 FPS

def jogo_principal():
    relogio = pygame.time.Clock()
    
    # Selecionar palavra aleatória
    tema = random.choice(list(banco_palavras.keys()))
    palavra, curiosidade = random.choice(banco_palavras[tema])
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 0
    fim_de_jogo = False
    vitoria = False
    
    executando = True
    while executando:
        desenhar_fundo()
        
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
            
            if fim_de_jogo and evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                return True
        
        # Desenhar título
        titulo = fonte_titulo.render("JOGO DA FORCA", True, ROXO)
        sombra = fonte_titulo.render("JOGO DA FORCA", True, PRETO)
        tela.blit(sombra, (LARGURA//2 - titulo.get_width()//2 + 3, 33))
        tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 30))
        
        # Desenhar tema
        tema_rect = pygame.Rect(LARGURA//2 - 200, 100, 400, 40)
        pygame.draw.rect(tela, (50, 50, 70), tema_rect, border_radius=20)
        pygame.draw.rect(tela, AZUL, tema_rect, 3, border_radius=20)
        tema_texto = fonte_normal.render(f"TEMA: {tema}", True, BRANCO)
        tela.blit(tema_texto, (LARGURA//2 - tema_texto.get_width()//2, 105))
        
        # Desenhar forca
        desenhar_forca(tentativas)
        
        # Desenhar palavra
        palavra_mostrada = "  ".join([letra if letra in letras_corretas else "_" for letra in palavra])
        palavra_surf = fonte_palavra.render(palavra_mostrada, True, AMARELO)
        tela.blit(palavra_surf, (LARGURA//2 - palavra_surf.get_width()//2, 480))
        
        # Letras erradas
        if letras_erradas:
            erradas_texto = fonte_pequena.render("Letras erradas:", True, VERMELHO)
            tela.blit(erradas_texto, (50, 600))
            
            letras_texto = fonte_normal.render(", ".join(letras_erradas), True, VERMELHO)
            tela.blit(letras_texto, (50, 630))
        
        # Tentativas
        tentativas_texto = fonte_pequena.render(f"Tentativas restantes: {6 - tentativas}", True, BRANCO)
        tela.blit(tentativas_texto, (LARGURA - 250, 600))
        
        # Fim de jogo
        if fim_de_jogo:
            overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            tela.blit(overlay, (0, 0))
            
            if vitoria:
                animar_vitoria()
                desenhar_fundo()
                
                resultado = fonte_titulo.render("PARABÉNS!", True, VERDE)
                tela.blit(resultado, (LARGURA//2 - resultado.get_width()//2, 200))
                
                # Caixa de curiosidade
                curiosidade_rect = pygame.Rect(LARGURA//2 - 350, 280, 700, 150)
                pygame.draw.rect(tela, (30, 30, 50), curiosidade_rect, border_radius=15)
                pygame.draw.rect(tela, VERDE, curiosidade_rect, 3, border_radius=15)
                
                titulo_curiosidade = fonte_normal.render("Você sabia?", True, AMARELO)
                tela.blit(titulo_curiosidade, (LARGURA//2 - titulo_curiosidade.get_width()//2, 300))
                
                # Quebra a curiosidade em linhas se for muito longa
                linhas = []
                palavras = curiosidade.split()
                linha_atual = ""
                
                for palavra in palavras:
                    teste = linha_atual + " " + palavra if linha_atual else palavra
                    if fonte_curiosidade.size(teste)[0] < 650:
                        linha_atual = teste
                    else:
                        linhas.append(linha_atual)
                        linha_atual = palavra
                if linha_atual:
                    linhas.append(linha_atual)
                
                for i, linha in enumerate(linhas):
                    linha_surf = fonte_curiosidade.render(linha, True, BRANCO)
                    tela.blit(linha_surf, (LARGURA//2 - linha_surf.get_width()//2, 350 + i*35))
            else:
                resultado = fonte_titulo.render("FIM DE JOGO", True, VERMELHO)
                tela.blit(resultado, (LARGURA//2 - resultado.get_width()//2, 200))
                
                resposta = fonte_palavra.render(f"A palavra era: {palavra}", True, BRANCO)
                tela.blit(resposta, (LARGURA//2 - resposta.get_width()//2, 280))
                
                mensagem = fonte_normal.render("Tente novamente, você consegue!", True, AMARELO)
                tela.blit(mensagem, (LARGURA//2 - mensagem.get_width()//2, 350))
            
            reiniciar_texto = fonte_pequena.render("Pressione R para jogar novamente", True, BRANCO)
            tela.blit(reiniciar_texto, (LARGURA//2 - reiniciar_texto.get_width()//2, 450))
        
        pygame.display.flip()
        relogio.tick(60)

    return False

# Iniciar jogo
if __name__ == "__main__":
    pygame.mixer.init()
    
    # Tela de abertura
    desenhar_fundo()
    titulo = fonte_titulo.render("JOGO DA FORCA", True, ROXO)
    subtitulo = fonte_normal.render("Pressione qualquer tecla para começar", True, BRANCO)
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, ALTURA//2 - 50))
    tela.blit(subtitulo, (LARGURA//2 - subtitulo.get_width()//2, ALTURA//2 + 50))
    pygame.display.flip()
    
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                aguardando = False
    
    # Loop principal do jogo
    reiniciar = True
    while reiniciar:
        reiniciar = jogo_principal()
    
    pygame.quit()
    sys.exit()