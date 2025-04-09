import pygame
import random
import sys
import unicodedata
import os
import math
from pygame import gfxdraw

# Inicializa o pygame e o mixer de áudio
pygame.init()
pygame.mixer.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação - Curiosidades")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
DARK_GRAY = (50, 50, 50)
SHADOW_COLOR = (30, 30, 30)
ORANGE = (255, 165, 0)

# Carrega as fontes
try:
    font_large = pygame.font.SysFont('calibri', 48, bold=True)
    font_medium = pygame.font.SysFont('calibri', 36)
    font_small = pygame.font.SysFont('calibri', 24)
    font_placar = pygame.font.SysFont('calibri', 32, bold=True)
except:
    font_large = pygame.font.SysFont('arial', 48, bold=True)
    font_medium = pygame.font.SysFont('arial', 36)
    font_small = pygame.font.SysFont('arial', 24)
    font_placar = pygame.font.SysFont('arial', 32, bold=True)

# Efeitos sonoros
try:
    sound_acerto = pygame.mixer.Sound('acerto.wav')
    sound_tecla = pygame.mixer.Sound('tecla.wav')  # Som para quando digitar
except:
    # Sons padrão caso os arquivos não existam
    sound_acerto = pygame.mixer.Sound(buffer=bytearray([128, 128]))
    sound_tecla = pygame.mixer.Sound(buffer=bytearray([128, 128]))
    print("Arquivos de som não encontrados")

# Banco de palavras e dicas (com acentuação)
palavras_dicas = {
    "eiffel": ["Monumento famoso em Paris", "Foi construída para uma exposição mundial", "Tem um nome de engenheiro"],
    "oxigênio": ["Elemento essencial para a vida", "Compõe cerca de 21% da atmosfera terrestre", "Os mergulhadores usam tanques dele"],
    "amazônia": ["Maior floresta tropical do mundo", "Conhecida como 'pulmão do mundo'", "Localizada principalmente no Brasil"],
    "neurônio": ["Célula principal do sistema nervoso", "Transmite informações através de impulsos elétricos", "Temos cerca de 86 bilhões deles no cérebro"],
    "bigbang": ["Teoria sobre a origem do universo", "Ocorreu há cerca de 13,8 bilhões de anos", "O universo ainda está se expandindo por causa disso"],
    "diamante": ["Forma alotrópica do carbono", "Mineral mais duro conhecido", "Usado em joias e ferramentas de corte"],
    "coliseu": ["Antigo anfiteatro em Roma", "Cenário de batalhas de gladiadores", "Pode acomodar mais de 50 mil espectadores"],
    "açúcar": ["Substância cristalina doce", "Pode ser extraído da cana ou da beterraba", "Em excesso pode causar diabetes"],
    "coração": ["Órgão muscular que bombeia sangue", "Tem quatro câmaras nos mamíferos", "Simboliza o amor em muitas culturas"]
}

class Placar:
    def __init__(self):
        self.pontos = 0.0
        self.anim_offset = [0] * 20  # Offset para animação de cada caractere
        self.anim_time = 0
    
    def adicionar_vitoria(self):
        self.pontos += 1.0
    
    def adicionar_derrota(self):
        self.pontos -= 0.33
        self.pontos = max(self.pontos, 0.0)
    
    def atualizar_animacao(self):
        self.anim_time += 0.1
        for i in range(len(self.anim_offset)):
            # Efeito de onda senoidal para cada caractere
            self.anim_offset[i] = math.sin(self.anim_time + i * 0.5) * 3
    
    def mostrar(self, y):
        self.atualizar_animacao()
        placar_text = f"Pontuação: {self.pontos:.2f}"
        
        # Posição inicial
        x = WIDTH // 2 - font_placar.size(placar_text)[0] // 2
        
        # Renderiza cada caractere com animação individual
        for i, char in enumerate(placar_text):
            # Cor alternada para efeito mais visível
            color = YELLOW if i % 2 == 0 else ORANGE
            
            # Sombra
            shadow = font_placar.render(char, True, SHADOW_COLOR)
            screen.blit(shadow, (x + 2 + i * font_placar.size(char)[0], y + 2 + self.anim_offset[i]))
            
            # Texto principal
            text = font_placar.render(char, True, color)
            screen.blit(text, (x + i * font_placar.size(char)[0], y + self.anim_offset[i]))
        
        return pygame.Rect(x, y, font_placar.size(placar_text)[0], font_placar.size(placar_text)[1])

def remover_acentos(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto

def normalizar_texto(texto):
    return remover_acentos(texto).lower().strip()

def escolher_palavra():
    palavras_disponiveis = [p for p in palavras_dicas.keys()]
    if not palavras_disponiveis:
        return None, None
    palavra = random.choice(palavras_disponiveis)
    dicas = palavras_dicas[palavra]
    return palavra, dicas

def mostrar_texto_com_sombra(texto, fonte, cor, y, x=None, sombra=True):
    if x is None:
        x = (WIDTH - fonte.size(texto)[0]) // 2
    
    if sombra:
        shadow_surface = fonte.render(texto, True, SHADOW_COLOR)
        screen.blit(shadow_surface, (x + 2, y + 2))
    
    texto_surface = fonte.render(texto, True, cor)
    screen.blit(texto_surface, (x, y))
    return texto_surface.get_rect(topleft=(x, y))

def tela_inicial(placar):
    screen.fill(BLACK)
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 300, HEIGHT//2 - 200, 600, 400), border_radius=10)
    
    mostrar_texto_com_sombra("Jogo de Adivinhação", font_large, WHITE, 100)
    mostrar_texto_com_sombra("Descubra as curiosidades!", font_medium, WHITE, 160)
    mostrar_texto_com_sombra("Você tem 3 chances para adivinhar", font_small, WHITE, 210)
    mostrar_texto_com_sombra("Acerto: +1.00 ponto | Erro: -0.33 pontos", font_small, WHITE, 250)
    mostrar_texto_com_sombra("Use Backspace para apagar letras", font_small, WHITE, 290)
    
    placar.mostrar(30)
    
    btn_iniciar = mostrar_texto_com_sombra("Iniciar Jogo", font_medium, GREEN, 350)
    btn_sair = mostrar_texto_com_sombra("Sair", font_medium, RED, 420)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if btn_iniciar.collidepoint(mouse_pos):
                    return True
                if btn_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.time.delay(100)

def jogo(placar):
    palavra, dicas = escolher_palavra()
    if palavra is None:
        return False
    
    tentativas = 3
    acertou = False
    cursor_visible = True
    cursor_time = 0
    
    while tentativas > 0 and not acertou:
        screen.fill(BLACK)
        pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 350, HEIGHT//2 - 150, 700, 300), border_radius=10)
        
        placar.mostrar(30)
        mostrar_texto_com_sombra(f"Tentativas restantes: {tentativas}", font_small, WHITE, 80)
        
        dica_idx = 3 - tentativas
        mostrar_texto_com_sombra(f"Dica {dica_idx + 1}: {dicas[dica_idx]}", font_medium, WHITE, 150)
        
        input_rect = pygame.Rect(WIDTH//2 - 150, 250, 300, 50)
        pygame.draw.rect(screen, GRAY, input_rect, 2, border_radius=5)
        
        user_text = ""
        input_active = True
        
        while input_active:
            cursor_time += 0.1
            if cursor_time >= 0.5:  # Piscar o cursor a cada 0.5 segundos
                cursor_visible = not cursor_visible
                cursor_time = 0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                        sound_tecla.play()
                    else:
                        # Permite qualquer caractere (incluindo acentos)
                        user_text += event.unicode
                        sound_tecla.play()
            
            screen.fill(BLACK)
            pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 350, HEIGHT//2 - 150, 700, 300), border_radius=10)
            
            placar.mostrar(30)
            mostrar_texto_com_sombra(f"Tentativas restantes: {tentativas}", font_small, WHITE, 80)
            mostrar_texto_com_sombra(f"Dica {dica_idx + 1}: {dicas[dica_idx]}", font_medium, WHITE, 150)
            pygame.draw.rect(screen, GRAY, input_rect, 2, border_radius=5)
            
            texto_surface = font_medium.render(user_text, True, WHITE)
            screen.blit(texto_surface, (input_rect.x + 5, input_rect.y + 10))
            
            # Desenha o cursor piscante
            if cursor_visible and input_active:
                cursor_x = input_rect.x + 5 + texto_surface.get_width()
                pygame.draw.line(screen, WHITE, (cursor_x, input_rect.y + 5), 
                                (cursor_x, input_rect.y + input_rect.height - 5), 2)
            
            pygame.display.flip()
            pygame.time.delay(10)
        
        # Compara as palavras normalizadas
        if normalizar_texto(user_text) == normalizar_texto(palavra):
            acertou = True
            placar.adicionar_vitoria()
            sound_acerto.play()
        else:
            tentativas -= 1
    
    if not acertou:
        placar.adicionar_derrota()
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 350, HEIGHT//2 - 150, 700, 300), border_radius=10)
    
    placar.mostrar(30)
    
    if acertou:
        mostrar_texto_com_sombra("Parabéns! Você acertou! +1.00", font_large, GREEN, 200)
    else:
        mostrar_texto_com_sombra(f"Você errou! -0.33 | A palavra era: {palavra}", font_large, RED, 200)
    
    btn_novamente = mostrar_texto_com_sombra("Nova Palavra", font_medium, GREEN, 300)
    btn_sair = mostrar_texto_com_sombra("Sair", font_medium, RED, 370)
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if btn_novamente.collidepoint(mouse_pos):
                    return True
                if btn_sair.collidepoint(mouse_pos):
                    return False
        pygame.time.delay(100)

def main():
    placar = Placar()
    
    if tela_inicial(placar):
        continuar = True
        while continuar:
            continuar = jogo(placar)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()