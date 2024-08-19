import pygame
from map import Map

class Game:
    def __init__(self, screen):
        self.screen = screen

        # Загрузка карты
        #self.map = Map(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Location\Map1.tmx")
        self.map = Map(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Tilesets\RPG\TiledMapEditor\SMD.tmx")



        # Изначальная позиция камеры (центр карты)
        self.camera_pos = (self.map.tmx_data.width * self.map.tmx_data.tilewidth // 2,
                           self.map.tmx_data.height * self.map.tmx_data.tileheight // 2)

    def update(self, dt):
        # Обновление карты (и других элементов)
        self.map.update(dt)

    def draw(self):
        # Очистка экрана
        self.screen.fill((0, 0, 0))

        # Центрирование камеры на позиции
        self.map.center_camera_on(self.camera_pos)

        # Отрисовка карты
        self.map.draw(self.screen)
