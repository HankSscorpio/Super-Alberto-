import pygame
import copy
from puntos import guardar_puntaje
from menu_principal import menu_principal

# Niveles
def crear_niveles(ANCHO, ALTO):
    return [
        [pygame.Rect(0, ALTO - 20, ANCHO, 20), pygame.Rect(100, 480, 100, 20), pygame.Rect(300, 520, 100, 20), pygame.Rect(500, 440, 100, 20), pygame.Rect(650, 300, 120, 20)],
        [pygame.Rect(0, ALTO - 20, ANCHO, 20), pygame.Rect(120, 350, 100, 20), pygame.Rect(350, 300, 150, 20), pygame.Rect(600, 400, 100, 20), pygame.Rect(300, 500, 100, 20)],
        [pygame.Rect(0, ALTO - 20, ANCHO, 20), pygame.Rect(80, 500, 60, 20), pygame.Rect(200, 460, 60, 20), pygame.Rect(320, 420, 60, 20), pygame.Rect(500, 460, 100, 20), pygame.Rect(620, 300, 120, 20)],
        [pygame.Rect(0, ALTO - 20, ANCHO, 20), pygame.Rect(600, 500, 120, 20), pygame.Rect(450, 400, 100, 20), pygame.Rect(300, 300, 80, 20), pygame.Rect(150, 200, 80, 20)],
        [pygame.Rect(0, ALTO - 20, ANCHO, 20), pygame.Rect(150, 500, 80, 20), pygame.Rect(350, 450, 80, 20), pygame.Rect(250, 350, 80, 20), pygame.Rect(500, 300, 120, 20), pygame.Rect(700, 250, 80, 20)],
        [pygame.Rect(0, ALTO - 20, ANCHO, 20), pygame.Rect(100, 400, 60, 20), pygame.Rect(300, 370, 100, 20), pygame.Rect(550, 340, 60, 20), pygame.Rect(600, 200, 120, 20)],
    ]

# Monedas
monedas = [
    [pygame.Rect(110, 450, 20, 20), pygame.Rect(680, 270, 20, 20)],
    [pygame.Rect(370, 270, 20, 20), pygame.Rect(630, 370, 20, 20)],
    [pygame.Rect(330, 390, 20, 20), pygame.Rect(670, 270, 20, 20)],
    [pygame.Rect(160, 170, 20, 20), pygame.Rect(460, 370, 20, 20)],
    [pygame.Rect(265, 320, 20, 20), pygame.Rect(720, 220, 20, 20)],
    [pygame.Rect(620, 170, 20, 20), pygame.Rect(310, 340, 20, 20)],
]

# Copia reinicio
monedas_originales = copy.deepcopy(monedas)

# Crear niveles globalmente
ANCHO, ALTO = 900, 675
niveles = crear_niveles(ANCHO, ALTO)

# Fondos
def cargar_fondos(ancho, alto):
    return [
        pygame.transform.scale(pygame.image.load("fondos/dia.png").convert(), (ancho, alto)),
        pygame.transform.scale(pygame.image.load("fondos/tarde.png").convert(), (ancho, alto)),
        pygame.transform.scale(pygame.image.load("fondos/noche.png").convert(), (ancho, alto)),
    ]

def get_fondo_por_nivel(nivel, fondos):
    if nivel in [0, 1]:
        return fondos[0]
    elif nivel in [2, 3]:
        return fondos[1]
    else:
        return fondos[2]

# Avanzar de nivel
def avanzar_nivel(jugador, pantalla_actual, ANCHO, ALTO, monedas, nombre_jugador, puntaje, VENTANA):
    if jugador.rect.right > ANCHO:
        if pantalla_actual < len(niveles) - 1:
            pantalla_actual += 1
            jugador.rect.left = 0
        else:
            # Guardar puntaje
            guardar_puntaje(nombre_jugador, puntaje)

            # Mostrar "¡GANASTE!"
            fuente = pygame.font.SysFont("arial", 60, bold=True)
            texto = fuente.render("¡GANASTE!", True, (255, 255, 255))
            rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
            VENTANA.blit(texto, rect)
            pygame.display.flip()

            # Espera antes de volver al menú
            pygame.time.delay(3000)

            # Volver al menú
            menu_principal(ANCHO, ALTO)

            # Reiniciar juego
            jugador.rect.x = 100
            jugador.rect.y = ALTO - 82
            pantalla_actual = 0
            monedas[:] = [list(m) for m in monedas_originales]
            puntaje = 0

    return pantalla_actual, puntaje