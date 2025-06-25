import pygame

class Jugador:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.velocidad_x = 5
        self.velocidad_y = 0
        self.gravedad = 0.8
        self.salto = -15
        self.en_suelo = False

        # Cargar el spritesheet y extraer el tercer sprite de la segunda fila
        spritesheet = pygame.image.load("assets/alberto.png").convert_alpha()
        sprite_rect = pygame.Rect(2 * 32, 1 * 32, 32, 32)
        self.sprite = spritesheet.subsurface(sprite_rect)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad_x
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad_x
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.velocidad_y = self.salto
            self.en_suelo = False

    def aplicar_gravedad(self):
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

    def verificar_colisiones(self, plataformas):
        self.en_suelo = False
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma):
                if self.velocidad_y > 0:
                    self.rect.bottom = plataforma.top
                    self.velocidad_y = 0
                    self.en_suelo = True

    def dibujar(self, ventana):
        ventana.blit(self.sprite, (self.rect.x, self.rect.y))
