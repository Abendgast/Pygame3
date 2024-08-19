import pygame
import pytmx
import pyscroll

class Map:
    def __init__(self, filename):
        # Загрузка TMX карты
        self.tmx_data = pytmx.util_pygame.load_pygame(filename)

        # Создание данных для прокрутки карты
        map_data = pyscroll.data.TiledMapData(self.tmx_data)

        # Настройка рендерера для отображения карты
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.map_layer = pyscroll.BufferedRenderer(map_data, (screen_width, screen_height))
        self.map_layer.zoom = 1  # Масштабирование, если необходимо

        # Создание группы спрайтов, которая включает карту и игрока
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer)

    def draw(self, surface):
        # Отрисовка карты и объектов
        self.group.draw(surface)

    def update(self, dt, keys):
        # Обновление логики группы, передаем `keys` для всех спрайтов
        for sprite in self.group.sprites():
            sprite.update(dt, keys)

    def center_camera_on(self, position):
        # Центрирование камеры на заданной позиции
        self.group.center(position)
