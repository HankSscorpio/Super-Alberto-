import pygame
import sys
from menu_principal import menu_principal
from jugador import Jugador
from niveles import niveles, monedas, cargar_fondos, get_fondo_por_nivel, avanzar_nivel
from puntos import guardar_puntaje, obtener_top_3

# Inicializar
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

# Nombre del jugador
fuente_nombre = pygame.font.SysFont("arial", 32)
nombre_jugador = ""
escribiendo = True

# Ingreso del nombre antes de iniciar
while escribiendo:
    VENTANA.fill((0, 0, 0))
    texto = fuente_nombre.render("Ingresá tu nombre y presioná ENTER:", True, (255, 255, 255))
    nombre_surface = fuente_nombre.render(nombre_jugador, True, (255, 255, 0))
    VENTANA.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 200))
    VENTANA.blit(nombre_surface, (ANCHO // 2 - nombre_surface.get_width() // 2, 260))
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN and nombre_jugador:
                escribiendo = False
            elif evento.key == pygame.K_BACKSPACE:
                nombre_jugador = nombre_jugador[:-1]
            elif len(nombre_jugador) < 12 and evento.unicode.isprintable():
                nombre_jugador += evento.unicode

# Puntaje inicial
puntaje = 0
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

    # Verificar gravedad y colisiones
    jugador.aplicar_gravedad()
    jugador.verificar_colisiones(niveles[pantalla_actual])

    # Avanzar nivel o volver al menú si terminó
    pantalla_actual, puntaje = avanzar_nivel(
        jugador, pantalla_actual, ANCHO, ALTO, monedas, nombre_jugador, puntaje, VENTANA
    )

    # Fondo
    fondo_actual = get_fondo_por_nivel(pantalla_actual, fondos)
    VENTANA.blit(fondo_actual, (0, 0))

    # Recolección de monedas
    monedas_nivel = monedas[pantalla_actual]
    for moneda in monedas_nivel[:]:
        if jugador.rect.colliderect(moneda):
            monedas_nivel.remove(moneda)
            sonido_moneda.play()
            puntaje += 10

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

    pygame.display.flip()
    