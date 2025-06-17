import pygame

class Jugador:
    def __init__(self, x, y, ancho=32, alto=32, salto=-15, gravedad=0.8):
        self.ancho = ancho
        self.alto = alto
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.vel_x = 5
        self.vel_y = 0
        self.gravedad = gravedad
        self.salto = salto
        self.en_suelo = False

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.vel_x
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.vel_x
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = self.salto
            self.en_suelo = False

    def aplicar_gravedad(self):
        self.vel_y += self.gravedad
        self.rect.y += self.vel_y

    def verificar_colisiones(self, plataformas):
        self.en_suelo = False
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma):
                if self.vel_y > 0:
                    self.rect.bottom = plataforma.top
                    self.vel_y = 0
                    self.en_suelo = True

    def dibujar(self, ventana, color=(0, 0, 255)):
        pygame.draw.rect(ventana, color, self.rect)
