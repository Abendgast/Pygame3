import pygame
from map import Map
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen

        # Завантаження карти
        self.map = Map(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Tilesets\RPG\TiledMapEditor\SMD.tmx")

        # Створення гравця у центрі карти
        start_pos = (self.map.tmx_data.width * self.map.tmx_data.tilewidth // 2,
                     self.map.tmx_data.height * self.map.tmx_data.tileheight // 2)
        self.player = Player(start_pos)

        # Додавання гравця у слої
        self.map.add_player_to_group(self.player)

        # Початкова позиція камери (центр картки)
        self.camera_pos = (self.map.tmx_data.width * self.map.tmx_data.tilewidth // 2,
                           self.map.tmx_data.height * self.map.tmx_data.tileheight // 2)

    def update(self, dt, keys):
        # Оновлення картки (та інших елементів)
        self.map.update(dt, keys)

    def draw(self):
        # Очистка екрану
        self.screen.fill((0, 0, 0))

        # Центрування камери на позиції гравця
        self.map.center_camera_on(self.player.rect.center)

        # Відображення карти та всіх об'єктів
        self.map.draw(self.screen)
