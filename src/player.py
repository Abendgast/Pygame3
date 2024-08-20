import pygame

from src.colors import colorSAND, colorRED


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # Радіус кулі
        radius = 8  # Пів ширини/висоти поверхні

        # Створення поверхні з прозорим фоном для кулі
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

        # Малювання кулі
        pygame.draw.circle(self.image, colorRED, (radius, radius), radius)

        # Створення прямокутника для визначення позиції кулі
        self.rect = self.image.get_rect(center=position)
        self.speed = 200  # швидкість гравця

    def update(self, dt, keys):
        # керування WASD
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

        # оновлення позиції
        self.rect.x += dx
        self.rect.y += dy