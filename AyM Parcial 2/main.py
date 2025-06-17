import pygame
import sys
from menu_principal import menu_principal
from jugador import Jugador
from niveles import niveles, monedas, cargar_fondos, get_fondo_por_nivel

# Inicialización
pygame.init()
ANCHO, ALTO = 900, 675
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Super Alberto")
menu_principal(ANCHO, ALTO)

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (100, 100, 100)
VERDE_CLARO = (144, 238, 144)

clock = pygame.time.Clock()
FPS = 60

# Fondos
fondos = cargar_fondos(ANCHO, ALTO)

# Imagen moneda
imagen_moneda = pygame.image.load("assets/moneda.png").convert_alpha()
imagen_moneda = pygame.transform.scale(imagen_moneda, (20, 20))

# Sonidos
pygame.mixer.music.load("sonidos/musica.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

sonido_moneda = pygame.mixer.Sound("sonidos/moneda.mp3")
sonido_moneda.set_volume(0.8)

# Jugador
jugador = Jugador(100, ALTO - 82)

# Estado del juego
pantalla_actual = 0
pared_invisible = pygame.Rect(0, 0, 1, ALTO)

# Bucle principal
while True:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    jugador.mover(teclas)

    # Límite izquierdo en nivel 0
    if pantalla_actual == 0 and jugador.rect.left < pared_invisible.right:
        jugador.rect.left = pared_invisible.right

    # Cambio de pantalla
    if jugador.rect.right > ANCHO:
        if pantalla_actual < len(niveles) - 1:
            pantalla_actual += 1
            jugador.rect.left = 0
    elif jugador.rect.left < 0:
        if pantalla_actual > 0:
            pantalla_actual -= 1
            jugador.rect.right = ANCHO

    jugador.aplicar_gravedad()
    jugador.verificar_colisiones(niveles[pantalla_actual])

    # Fondo
    fondo_actual = get_fondo_por_nivel(pantalla_actual, fondos)
    VENTANA.blit(fondo_actual, (0, 0))

    # Recolección de monedas
    monedas_nivel = monedas[pantalla_actual]
    for moneda in monedas_nivel[:]:
        if jugador.rect.colliderect(moneda):
            monedas_nivel.remove(moneda)
            sonido_moneda.play()

    # Dibujar monedas
    for moneda in monedas[pantalla_actual]:
        VENTANA.blit(imagen_moneda, moneda)

    # Dibujar jugador
    jugador.dibujar(VENTANA)

    # Dibujar plataformas
    for plataforma in niveles[pantalla_actual]:
        if plataforma.top == ALTO - 20:
            pygame.draw.rect(VENTANA, VERDE_CLARO, plataforma)
        else:
            pygame.draw.rect(VENTANA, GRIS, plataforma)

    # Ganaste
    if pantalla_actual == len(niveles) - 1:
        fuente = pygame.font.SysFont("arial", 60, bold=True)
        texto = fuente.render("¡GANASTE!", True, (255, 255, 255))
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        VENTANA.blit(texto, rect)

    pygame.display.flip()
