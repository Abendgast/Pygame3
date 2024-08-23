import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((8, 16))
        self.image.fill((47, 31, 255))
        self.rect = self.image.get_rect(center=position)
        self.speed = 200

    def update(self, dt, keys):

        dx = 0
        dy = 0
        if keys[pygame.K_w]:
            dy = -self.speed * dt
        if keys[pygame.K_s]:
            dy = self.speed * dt
        if keys[pygame.K_a]:
            dx = -self.speed * dt
        if keys[pygame.K_d]:
            dx = self.speed * dt

        # Обновление позиции игрока
        self.rect.x += dx
        self.rect.y += dy
