import pygame
from map import Map
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen

        # Загрузка карты

        # self.map = Map(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Location\Map1.tmx") #(резерв)
        self.map = Map(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Tilesets\RPG\TiledMapEditor\SMD.tmx")

        # Создание игрока в центре карты
        start_pos = (self.map.tmx_data.width * self.map.tmx_data.tilewidth // 2,
                     self.map.tmx_data.height * self.map.tmx_data.tileheight // 2)
        self.player = Player(start_pos)

        # Добавление игрока в группу спрайтов карты
        self.map.group.add(self.player)

        # Изначальная позиция камеры (центр карты)
        self.camera_pos = (self.map.tmx_data.width * self.map.tmx_data.tilewidth // 2,
                           self.map.tmx_data.height * self.map.tmx_data.tileheight // 2)

    def update(self, dt, keys):
        # Обновление карты (и других элементов)
        self.map.update(dt, keys)

    def draw(self):
        # Очистка экрана
        self.screen.fill((0, 0, 0))

        # Центрирование камеры на позиции игрока
        self.map.center_camera_on(self.player.rect.center)

        # Отрисовка карты и всех объектов
        self.map.draw(self.screen)
