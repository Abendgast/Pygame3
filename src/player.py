import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))  # Красный квадрат
        self.rect = self.image.get_rect(center=position)
        self.speed = 200  # Скорость движения игрока

    def update(self, dt, keys):
        # Движение игрока с использованием WASD
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