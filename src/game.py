from map import Map
import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Загрузка карты
        self.map = Map(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Location\Map1.tmx")

        # Временная позиция камеры (центр карты)
        self.camera_pos = (self.map.tmx_data.width * self.map.tmx_data.tilewidth // 2,
                           self.map.tmx_data.height * self.map.tmx_data.tileheight // 2)

    def update(self, dt):
        # Обновление карты
        self.map.update(dt)

        # Здесь будет обновляться другая игровая логика

    def draw(self):
        # Очистка экрана
        self.screen.fill((0, 0, 0))  # Заполняем черным цветом

        # Перемещение камеры
        self.map.move_camera(self.camera_pos)

        # Отрисовка карты
        self.map.draw(self.screen)

        # Здесь будет отрисовка других игровых объектов