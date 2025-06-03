import pygame
import sys
import os

pygame.init()

# Configuración
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Super Alberto")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
GRIS = (100, 100, 100)

# Fuente
fuente = pygame.font.SysFont("arial", 50)
fuente_chica = pygame.font.SysFont("arial", 30)

clock = pygame.time.Clock()

# Cargar imagen de fondo
ruta_fondo = os.path.join("fondos", "dia.png")
fondo = pygame.image.load(ruta_fondo)
fondo= pygame.transform.scale(fondo, (ANCHO, ALTO))




# Función para dibujar texto centrado
def dibujar_texto(texto, fuente, color, superficie, x, y):
    render = fuente.render(texto, True, color)
    rect = render.get_rect()
    rect.center = (x, y)
    superficie.blit(render, rect)

# Menú principal
def menu_principal():
    while True:
        # Dibujar fondo
        VENTANA.blit(fondo, (0, 0))
        

        # Título
        dibujar_texto("Super Alberto", fuente, AMARILLO, VENTANA, ANCHO // 2, 150)

        # Botones
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        jugar_rect = pygame.Rect(300, 250, 200, 50)
        salir_rect = pygame.Rect(300, 330, 200, 50)

        # Dibujar botones
        pygame.draw.rect(VENTANA, GRIS, jugar_rect)
        pygame.draw.rect(VENTANA, GRIS, salir_rect)

        dibujar_texto("JUGAR", fuente_chica, BLANCO, VENTANA, 400, 275)
        dibujar_texto("SALIR", fuente_chica, BLANCO, VENTANA, 400, 355)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if jugar_rect.collidepoint(mouse):
                    return  # Salir del menú y entrar al juego
                if salir_rect.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)