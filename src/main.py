import pygame
import sys
from game import Game

# Инициализация Pygame
pygame.init()

# Настройки окна
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# Создаем экземпляр игры
game = Game(screen)

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление логики игры
    dt = clock.tick(60) / 1000  # Делим на 1000 для получения значения в секундах
    game.update(dt)

    # Отрисовка игры
    game.draw()

    # Обновление экрана
    pygame.display.flip()
