import pygame
import sys
from menu_principal import menu_principal

pygame.init()
menu_principal()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Super Alberto")

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (100, 100, 100)

clock = pygame.time.Clock()
FPS = 60

# Fondo para el nivel 0
fondo_dia = pygame.image.load("fondos/dia.png").convert()
fondo_dia = pygame.transform.scale(fondo_dia, (ANCHO, ALTO))


# Jugador
jugador_ancho = 32
jugador_alto = 32
jugador_x = 100
jugador_y = ALTO - jugador_alto - 50
velocidad_x = 5
velocidad_y = 0
gravedad = 0.8
salto = -15
en_suelo = False

# Pantallas

niveles = [
    [  # Nivel 0
        pygame.Rect(0, ALTO - 20, ANCHO, 20), 
        pygame.Rect(150, 500, 100, 20),
        pygame.Rect(100, 400, 100, 20),
        pygame.Rect(300, 450, 100, 20),
        pygame.Rect(500, 350, 120, 20),
        pygame.Rect(650, 280, 100, 20),  
    ],
    [  # Nivel 1
        pygame.Rect(0, ALTO - 20, ANCHO, 20),
        pygame.Rect(200, 520, 120, 20),
        pygame.Rect(400, 520, 100, 20),
        pygame.Rect(300, 400, 120, 20),
        pygame.Rect(500, 320, 80, 20),
        pygame.Rect(200, 250, 100, 20),  
    ],
    [  # Nivel 2
        pygame.Rect(0, ALTO - 20, ANCHO, 20),
        pygame.Rect(100, 500, 80, 20),
        pygame.Rect(250, 450, 100, 20),
        pygame.Rect(150, 350, 100, 20),
        pygame.Rect(350, 300, 100, 20),
        pygame.Rect(600, 380, 100, 20),  
        pygame.Rect(620, 250, 100, 20),  
    ],
]

# Monedas por pantalla (coordenadas x, y, ancho, alto)
monedas = [
    [pygame.Rect(520, 300, 20, 20)],  # Nivel 0
    [pygame.Rect(620, 260, 20, 20)],  # Nivel 1
    [pygame.Rect(620, 240, 20, 20)],  # Nivel 2
]

pantalla_actual = 0

# Pared invisible 
pared_invisible = pygame.Rect(0, 0, 1, ALTO)

# Bucle principal
while True:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad_x
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad_x
    if teclas[pygame.K_SPACE] and en_suelo:
        velocidad_y = salto
        en_suelo = False

    # Pared invisible solo en pantalla 0
    if pantalla_actual == 0 and jugador_x < pared_invisible.right:
        jugador_x = pared_invisible.right

    # Cambio de pantalla hacia la derecha
    if jugador_x > ANCHO:
        if pantalla_actual < len(niveles) - 1:
            pantalla_actual += 1
            jugador_x = 0  

    # Cambio de pantalla hacia la izquierda
    if jugador_x < 0:
        if pantalla_actual > 0:
            pantalla_actual -= 1
            jugador_x = ANCHO - jugador_ancho  

    # Gravedad
    velocidad_y += gravedad
    jugador_y += velocidad_y

    # Rectángulo del jugador
    
    jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)

    # Colisiones
    en_suelo = False
    for plataforma in niveles[pantalla_actual]:
        if jugador_rect.colliderect(plataforma):
            if velocidad_y > 0:
                jugador_y = plataforma.top - jugador_alto
                velocidad_y = 0
            en_suelo = True
            jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)

    # Dibujar fondo
    if pantalla_actual in [0, 1, 2]:
        VENTANA.blit(fondo_dia, (0, 0))
    else:
        VENTANA.fill(NEGRO)

    for moneda in monedas[pantalla_actual]:
        pygame.draw.circle(VENTANA, (255, 215, 0), moneda.center, 10)

    
    pygame.draw.rect(VENTANA, AZUL, jugador_rect)
    for plataforma in niveles[pantalla_actual]:
        pygame.draw.rect(VENTANA, GRIS, plataforma)

    pygame.display.flip()