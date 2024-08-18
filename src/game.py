import pygame

from src.colors import colorUI_BACKGROUND, colorWHITE, colorBLACK


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        # Інші атрибути (гравець, карта і т.д.)

    def update(self):
        # оновлення логіки
        pass

    def draw(self):
        # очищення екрана
        self.screen.fill(colorUI_BACKGROUND)

        # малювання об'єктів

        # малювання тексту
        font = pygame.font.Font(None, 38)
        text = font.render("Text here", True, colorWHITE)
        self.screen.blit(text, (10, 10))