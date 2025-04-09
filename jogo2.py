import pygame
import random
import sys
import unicodedata

# Inicialização
pygame.init()
pygame.mixer.init()

# Configurações da tela
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação - Curiosidades do Brasil")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
BLUE = (0, 100, 200)
YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (100, 100, 100)
BRASIL_GREEN = (0, 156, 59)
BRASIL_YELLOW = (255, 223, 0)
BRASIL_BLUE = (0, 39, 118)

# Fontes
try:
    font_title = pygame.font.SysFont('calibri', 60, bold=True)
    font_large = pygame.font.SysFont('calibri', 48, bold=True)
    font_medium = pygame.font.SysFont('calibri', 36)
    font_small = pygame.font.SysFont('calibri', 28)
    font_placar = pygame.font.SysFont('calibri', 42, bold=True)
except:
    font_title = pygame.font.SysFont('arial', 60, bold=True)
    font_large = pygame.font.SysFont('arial', 48, bold=True)
    font_medium = pygame.font.SysFont('arial', 36)
    font_small = pygame.font.SysFont('arial', 28)
    font_placar = pygame.font.SysFont('arial', 42, bold=True)

# Efeitos sonoros
try:
    sound_acerto = pygame.mixer.Sound('acerto.wav')
    sound_tecla = pygame.mixer.Sound('tecla.wav')
except:
    sound_acerto = pygame.mixer.Sound(buffer=bytearray([128, 128]))
    sound_tecla = pygame.mixer.Sound(buffer=bytearray([128, 128]))

# Banco de palavras sobre o Brasil
palavras_dicas = {
    "amazônia": ["Maior floresta tropical do mundo", "Tem aproximadamente 7 milhões de km²", "Possui cerca de 390 bilhões de árvores"],
    "carnaval": ["Maior festa popular do país", "Atrai milhões de turistas anualmente", "No Rio, os desfiles duram até 80 minutos cada"],
    "futebol": ["Esporte mais popular no Brasil", "A seleção brasileira possui 5 títulos mundiais", "Pelé marcou 1.281 gols em 1.363 jogos"],
    "café": ["Brasil produz 1/3 do café mundial", "Principal produto de exportação no século XIX", "São Paulo cresceu graças às plantações de café"],
    "samba": ["Gênero musical surgido no Rio", "Patrimônio Cultural Imaterial da Humanidade", "Estilo tocado nas escolas de samba do carnaval"],
    "capoeira": ["Arte marcial criada por escravos", "Combina dança, música e acrobacias", "Reconhecida como Patrimônio Cultural da Humanidade"],
    "bossa nova": ["Gênero musical surgido nos anos 50", "'Garota de Ipanema' é a música brasileira mais famosa", "Tom Jobim e João Gilberto são seus maiores nomes"],
    "açaí": ["Fruto típico da região norte", "Consumido por 94% dos brasileiros", "Rico em antioxidantes e energia"],
    "pão de açúcar": ["Monumento natural no Rio", "Tem 396 metros de altura", "Nome vem das formas de açúcar no século XVI"],
    "ipê": ["Árvore símbolo do Brasil", "Floresce em amarelo, roxo ou branco", "Cada cor representa uma região do país"]
}

class Placar:
    def __init__(self):
        self.pontos = 0.0
    
    def adicionar_vitoria(self):
        self.pontos += 1.0
    
    def adicionar_derrota(self):
        self.pontos = max(self.pontos - 0.33, 0.0)
    
    def mostrar(self, y):
        placar_text = f"Pontuação: {self.pontos:.2f}"
        
        # Fundo do placar
        pygame.draw.rect(screen, BRASIL_GREEN, (WIDTH//2 - 220, y - 10, 440, 60), border_radius=15)
        pygame.draw.rect(screen, BRASIL_YELLOW, (WIDTH//2 - 210, y, 420, 40), border_radius=10)
        
        # Texto estático centralizado
        text_surface = font_placar.render(placar_text, True, BRASIL_BLUE)
        screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, y))
        
        return pygame.Rect(WIDTH//2 - 220, y - 10, 440, 60)

def remover_acentos(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto

def normalizar_texto(texto):
    return remover_acentos(texto).lower().strip()

def escolher_palavra():
    palavra = random.choice(list(palavras_dicas.keys()))
    return palavra, palavras_dicas[palavra]

def mostrar_texto(texto, fonte, cor, y, x=None, sombra=False):
    if x is None:
        x = (WIDTH - fonte.size(texto)[0]) // 2
    
    if sombra:
        shadow = fonte.render(texto, True, (30, 30, 30))
        screen.blit(shadow, (x + 3, y + 3))
    
    text_surface = fonte.render(texto, True, cor)
    screen.blit(text_surface, (x, y))
    return text_surface.get_rect(topleft=(x, y))

def tela_inicial(placar):
    while True:
        screen.fill(BLACK)
        
        # Fundo temático
        pygame.draw.rect(screen, (0, 50, 0), (0, 0, WIDTH, HEIGHT//3))
        pygame.draw.rect(screen, (200, 150, 0), (0, HEIGHT//3, WIDTH, HEIGHT//3))
        pygame.draw.rect(screen, (0, 30, 100), (0, 2*HEIGHT//3, WIDTH, HEIGHT//3))
        
        mostrar_texto("Jogo de Adivinhação", font_title, WHITE, 80, sombra=True)
        mostrar_texto("Curiosidades do Brasil", font_large, WHITE, 150, sombra=True)
        
        # Container central
        pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 350, 220, 700, 300), border_radius=20)
        mostrar_texto("Você tem 3 chances para adivinhar", font_small, WHITE, 250)
        mostrar_texto("Acerto: +1.00 ponto | Erro: -0.33 pontos", font_small, WHITE, 290)
        mostrar_texto("Use Backspace para apagar letras", font_small, WHITE, 330)
        
        placar.mostrar(400)
        
        btn_iniciar = mostrar_texto("Iniciar Jogo", font_medium, GREEN, 480)
        btn_sair = mostrar_texto("Sair", font_medium, RED, 540)
        
        pygame.display.flip()
        
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
        
        pygame.time.delay(10)

def jogo(placar):
    palavra, dicas = escolher_palavra()
    tentativas = 3
    acertou = False
    cursor_visible = True
    cursor_time = 0
    
    while tentativas > 0 and not acertou:
        screen.fill(BLACK)
        
        # Fundo temático
        pygame.draw.rect(screen, (0, 30, 0), (0, 0, WIDTH, HEIGHT))
        
        # Container principal
        pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 400, 50, 800, 600), border_radius=20)
        
        placar.mostrar(30)
        mostrar_texto(f"Tentativas restantes: {tentativas}", font_small, WHITE, 100)
        
        dica_idx = 3 - tentativas
        dica_completa = f"Dica {dica_idx + 1}: {dicas[dica_idx]} (Palavra com {len(palavra)} letras)"
        mostrar_texto(dica_completa, font_medium, WHITE, 170)
        
        # Caixa de entrada
        input_rect = pygame.Rect(WIDTH//2 - 200, 250, 400, 60)
        pygame.draw.rect(screen, LIGHT_GRAY, input_rect, border_radius=10)
        pygame.draw.rect(screen, WHITE, input_rect, 2, border_radius=10)
        
        user_text = ""
        input_active = True
        
        while input_active:
            cursor_time += 0.1
            if cursor_time >= 0.5:
                cursor_visible = not cursor_visible
                cursor_time = 0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and user_text:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        if user_text:
                            user_text = user_text[:-1]
                            sound_tecla.play()
                    elif event.unicode.isprintable():
                        user_text += event.unicode
                        sound_tecla.play()
            
            # Redesenha
            screen.fill(BLACK)
            pygame.draw.rect(screen, (0, 30, 0), (0, 0, WIDTH, HEIGHT))
            pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 400, 50, 800, 600), border_radius=20)
            
            placar.mostrar(30)
            mostrar_texto(f"Tentativas restantes: {tentativas}", font_small, WHITE, 100)
            mostrar_texto(dica_completa, font_medium, WHITE, 170)
            
            pygame.draw.rect(screen, LIGHT_GRAY, input_rect, border_radius=10)
            pygame.draw.rect(screen, WHITE, input_rect, 2, border_radius=10)
            
            text_surface = font_medium.render(user_text, True, WHITE)
            screen.blit(text_surface, (input_rect.x + 15, input_rect.y + 15))
            
            if cursor_visible:
                cursor_x = input_rect.x + 20 + text_surface.get_width()
                pygame.draw.line(screen, WHITE, (cursor_x, input_rect.y + 15), 
                                (cursor_x, input_rect.y + input_rect.height - 15), 3)
            
            pygame.display.flip()
            pygame.time.delay(10)
        
        if normalizar_texto(user_text) == normalizar_texto(palavra):
            acertou = True
            placar.adicionar_vitoria()
            sound_acerto.play()
        else:
            tentativas -= 1
    
    # Tela de resultado
    screen.fill(BLACK)
    pygame.draw.rect(screen, (0, 30, 0), (0, 0, WIDTH, HEIGHT))
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH//2 - 400, 100, 800, 500), border_radius=20)
    
    placar.mostrar(50)
    
    if acertou:
        mostrar_texto("Parabéns! Você acertou!", font_large, GREEN, 200)
        mostrar_texto(f"+1.00 ponto", font_medium, BRASIL_YELLOW, 260)
    else:
        mostrar_texto("Você errou!", font_large, RED, 200)
        mostrar_texto(f"A palavra era: {palavra}", font_medium, WHITE, 260)
        mostrar_texto("-0.33 pontos", font_medium, ORANGE, 320)
    
    mostrar_texto(palavras_dicas[palavra][2], font_small, WHITE, 380)  # Mostra a terceira dica como curiosidade extra
    
    btn_novamente = mostrar_texto("Nova Palavra", font_medium, GREEN, 450)
    btn_sair = mostrar_texto("Sair", font_medium, RED, 520)
    
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
        
        pygame.time.delay(10)

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
    