import pygame


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
        self.screen.fill((0, 0, 0))  # Заполняем черным цветом

        # малювання об'єктів

        # малювання тексту
        font = pygame.font.Font(None, 36)
        text = font.render("My RPG Game", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))