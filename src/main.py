import pygame
import sys
from game import Game

# ініціалізація Pygame
pygame.init()

# налаштування вікна
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# створення екземпляру
game = Game(screen)


# Основний цикл
clock = pygame.time.Clock()
running = True  # прапор для керування циклом

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # прапор виходу

        # стан клавіш
        keys = pygame.key.get_pressed()

        # оновлення логіки
        dt = clock.tick(60) / 1000  # значення в секундах
        game.update(dt, keys)

        # малювання гри
        game.draw()

        # оновлення екрана
        pygame.display.flip()
except KeyboardInterrupt:
    pass  # вихід через перехоплення преривання

finally:
    pygame.quit()
    sys.exit()