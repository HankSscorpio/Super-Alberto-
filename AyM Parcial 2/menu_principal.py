import pygame
import sys

def menu_principal(ANCHO, ALTO):
    VENTANA = pygame.display.get_surface()

    # Cargar fondo de tarde
    fondo = pygame.image.load("fondos/tarde.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # Cargar y escalar imagen del título
    titulo_original = pygame.image.load("assets/titulo.png").convert_alpha()

    # Escalado manteniendo proporción con ancho máximo de 500
    max_ancho = 500
    escala = max_ancho / titulo_original.get_width()
    nuevo_ancho = int(titulo_original.get_width() * escala)
    nuevo_alto = int(titulo_original.get_height() * escala)
    titulo = pygame.transform.scale(titulo_original, (nuevo_ancho, nuevo_alto))
    
    # CENTRAR y BAJAR el título
    titulo_rect = titulo.get_rect(center=(ANCHO // 2, ALTO // 4))

    # Botones centrados
    boton_ancho, boton_alto = 200, 50
    espacio_vertical = 20  # espacio entre botones

    jugar_rect = pygame.Rect(0, 0, boton_ancho, boton_alto)
    salir_rect = pygame.Rect(0, 0, boton_ancho, boton_alto)

    # Colocarlos debajo del título con espaciado
    jugar_rect.center = (ANCHO // 2, titulo_rect.bottom + 80)
    salir_rect.center = (ANCHO // 2, jugar_rect.bottom + boton_alto + espacio_vertical)

    # Colores
    BLANCO = (255, 255, 255)
    GRIS = (50, 50, 50)

    fuente = pygame.font.SysFont("arial", 30)
    clock = pygame.time.Clock()

    while True:
        VENTANA.blit(fondo, (0, 0))

        # Dibujar título
        VENTANA.blit(titulo, titulo_rect)

        # Dibujar botones
        pygame.draw.rect(VENTANA, GRIS, jugar_rect, border_radius=10)
        pygame.draw.rect(VENTANA, GRIS, salir_rect, border_radius=10)

        texto_jugar = fuente.render("JUGAR", True, BLANCO)
        texto_salir = fuente.render("SALIR", True, BLANCO)

        VENTANA.blit(texto_jugar, texto_jugar.get_rect(center=jugar_rect.center))
        VENTANA.blit(texto_salir, texto_salir.get_rect(center=salir_rect.center))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if jugar_rect.collidepoint(pygame.mouse.get_pos()):
                    return
                if salir_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)
