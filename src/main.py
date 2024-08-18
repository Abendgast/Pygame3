import pygame
import sys
from game import Game

#  ініціалізація
pygame.init()

# налаштування вікна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My RPG Game")

# екземпляр гри
game = Game(screen)

# основний цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # оновлення логіки
    game.update()

    # малювання
    game.draw()

    # оновлення екрану
    pygame.display.flip()

    # обмеження FPS
    clock.tick(60)