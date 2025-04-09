import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca Premium")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (100, 150, 255)
PURPLE = (180, 70, 200)
GRAY = (100, 100, 100)
WOOD = (160, 130, 90)

# Fontes
try:
    font_large = pygame.font.SysFont('calibri', 60, bold=True)
    font_medium = pygame.font.SysFont('calibri', 45)
    font_small = pygame.font.SysFont('calibri', 30)
    font_info = pygame.font.SysFont('calibri', 25)
except:
    font_large = pygame.font.SysFont('arial', 60, bold=True)
    font_medium = pygame.font.SysFont('arial', 45)
    font_small = pygame.font.SysFont('arial', 30)
    font_info = pygame.font.SysFont('arial', 25)

# Dados do jogo
temas_palavras = {
    "Animais": [
        ("GIRAFA", "As girafas têm o mesmo número de vértebras no pescoço que os humanos: 7."),
        ("ORNITORRINCO", "O ornitorrinco é um dos poucos mamíferos que põem ovos."),
        ("AXOLOTE", "O axolote pode regenerar membros inteiros, incluindo partes do cérebro e coração.")
    ],
    "Países": [
        ("BUTAO", "Butão é o único país que mede sua prosperidade pelo Índice de Felicidade Nacional."),
        ("NEPAL", "O Nepal é o único país com bandeira que não é retangular."),
        ("CANADA", "O Canadá tem mais lagos que todos os outros países combinados.")
    ],
    "Ciência": [
        ("DIAMANTE", "Diamantes podem queimar a temperaturas extremamente altas."),
        ("VENUS", "Um dia em Vênus é mais longo que um ano em Vênus."),
        ("TARDIGRADO", "Tardígrados podem sobreviver no vácuo do espaço.")
    ]
}

frases_engracadas = [
    "Talvez você devesse tentar o jogo da memória...",
    "Isso foi... interessante. Vamos tentar de novo?",
    "Até meu cachorro acertaria essa!",
    "Não desista do seu dia job!",
    "Você está tentando perder de propósito?",
    "Acho que precisamos de mais café..."
]

def draw_hangman(attempts):
    # Base da forca
    pygame.draw.rect(screen, WOOD, (150, 500, 200, 15), border_radius=5)
    # Poste vertical
    pygame.draw.rect(screen, WOOD, (250, 200, 20, 300), border_radius=5)
    # Topo horizontal
    pygame.draw.rect(screen, WOOD, (250, 200, 150, 20), border_radius=5)
    # Corda
    pygame.draw.line(screen, GRAY, (400, 220), (400, 250), 3)
    
    # Boneco
    if attempts < 6:  # Cabeça
        pygame.draw.circle(screen, WHITE, (400, 275), 25, 3)
        # Expressão facial
        pygame.draw.arc(screen, WHITE, (390, 265, 8, 8), 3.14, 6.28, 2)  # Olhos
        pygame.draw.arc(screen, WHITE, (402, 265, 8, 8), 3.14, 6.28, 2)
        pygame.draw.arc(screen, WHITE, (395, 280, 10, 5), 3.14, 6.28, 2) # Boca feliz
    
    if attempts < 5:  # Corpo
        pygame.draw.line(screen, WHITE, (400, 300), (400, 375), 3)
    
    if attempts < 4:  # Braço esquerdo
        pygame.draw.line(screen, WHITE, (400, 320), (370, 340), 3)
    
    if attempts < 3:  # Braço direito
        pygame.draw.line(screen, WHITE, (400, 320), (430, 340), 3)
    
    if attempts < 2:  # Perna esquerda
        pygame.draw.line(screen, WHITE, (400, 375), (370, 415), 3)
    
    if attempts < 1:  # Perna direita
        pygame.draw.line(screen, WHITE, (400, 375), (430, 415), 3)

def draw_button(text, rect, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    color = hover_color if rect.collidepoint(mouse_pos) else color
    
    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=10)
    
    text_surf = font_small.render(text, True, WHITE)
    screen.blit(text_surf, (rect.centerx - text_surf.get_width()//2, 
                           rect.centery - text_surf.get_height()//2))
    
    return rect.collidepoint(mouse_pos)

def main():
    clock = pygame.time.Clock()
    
    # Selecionar palavra e tema
    tema = random.choice(list(temas_palavras.keys()))
    palavra, curiosidade = random.choice(temas_palavras[tema])
    letras_acertadas = set()
    letras_erradas = set()
    tentativas = 6
    game_over = False
    vitoria = False
    
    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over and event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letra = chr(event.key).upper()
                    if letra not in letras_acertadas and letra not in letras_erradas:
                        if letra in palavra:
                            letras_acertadas.add(letra)
                            if all(l in letras_acertadas for l in palavra):
                                game_over = True
                                vitoria = True
                        else:
                            letras_erradas.add(letra)
                            tentativas -= 1
                            if tentativas == 0:
                                game_over = True
                                vitoria = False
            
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    return True
        
        # Desenhar título
        title = font_large.render("JOGO DA FORCA", True, PURPLE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        
        # Desenhar tema
        theme_rect = pygame.Rect(WIDTH//2 - 180, 100, 360, 40)
        pygame.draw.rect(screen, GRAY, theme_rect, border_radius=20)
        pygame.draw.rect(screen, WHITE, theme_rect, 2, border_radius=20)
        theme_text = font_info.render(f"TEMA: {tema}", True, WHITE)
        screen.blit(theme_text, (WIDTH//2 - theme_text.get_width()//2, 110))
        
        # Desenhar forca
        draw_hangman(tentativas)
        
        # Desenhar palavra
        display_word = "   ".join([letra if letra in letras_acertadas else "_" for letra in palavra])
        word = font_medium.render(display_word, True, WHITE)
        screen.blit(word, (WIDTH//2 - word.get_width()//2, 450))
        
        # Letras erradas
        if letras_erradas:
            wrong_text = font_info.render("Letras erradas:", True, RED)
            screen.blit(wrong_text, (50, 550))
            
            letters = font_small.render(", ".join(letras_erradas), True, RED)
            screen.blit(letters, (50, 580))
        
        # Tentativas
        attempts_text = font_info.render(f"Tentativas restantes: {tentativas}", True, WHITE)
        screen.blit(attempts_text, (WIDTH - 250, 550))
        
        # Game over
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            if vitoria:
                result = font_large.render("PARABÉNS!", True, GREEN)
                screen.blit(result, (WIDTH//2 - result.get_width()//2, 250))
                
                curiosity_box = pygame.Rect(WIDTH//2 - 300, 320, 600, 100)
                pygame.draw.rect(screen, GRAY, curiosity_box, border_radius=15)
                pygame.draw.rect(screen, GREEN, curiosity_box, 2, border_radius=15)
                
                curiosity_text = font_info.render(curiosidade, True, WHITE)
                screen.blit(curiosity_text, (WIDTH//2 - curiosity_text.get_width()//2, 350))
            else:
                result = font_large.render("FIM DE JOGO", True, RED)
                screen.blit(result, (WIDTH//2 - result.get_width()//2, 250))
                
                answer = font_medium.render(f"A palavra era: {palavra}", True, WHITE)
                screen.blit(answer, (WIDTH//2 - answer.get_width()//2, 320))
                
                funny_line = font_info.render(random.choice(frases_engracadas), True, RED)
                screen.blit(funny_line, (WIDTH//2 - funny_line.get_width()//2, 370))
            
            # Botão de jogar novamente
            replay_button = pygame.Rect(WIDTH//2 - 120, 450, 240, 60)
            if draw_button("JOGAR NOVAMENTE", replay_button, BLUE, PURPLE):
                pygame.draw.rect(screen, WHITE, replay_button, 3, border_radius=10)
        
        pygame.display.flip()
        clock.tick(30)
    
    return False

if __name__ == "__main__":
    jogar_novamente = True
    while jogar_novamente:
        jogar_novamente = main()
    
    pygame.quit()
    sys.exit()

