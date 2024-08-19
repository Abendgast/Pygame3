import pygame
import sys
from game import Game

# Инициализация
pygame.init()

# Настройки окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GMainScreen")

# Экземпляр игры
game = Game(screen)

# Основной цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление логики
    dt = clock.tick(60) / 1000  # Получаем время, прошедшее с последнего кадра в секундах
    game.update(dt)

    # Отрисовка
    game.draw()

    # Обновление экрана
    pygame.display.flip()