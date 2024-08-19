import pygame
import pytmx
import pyscroll


class Map:
    def __init__(self, filename):
        # Загрузка TMX карты
        self.tmx_data = pytmx.load_pygame(filename)

        # Создание данных для прокрутки карты
        map_data = pyscroll.data.TiledMapData(self.tmx_data)

        # Получение размера экрана (предполагаем, что он установлен в game.py)
        screen_width, screen_height = pygame.display.get_surface().get_size()

        # Создание группы для прокрутки с небольшим запасом по краям
        self.map_layer = pyscroll.BufferedRenderer(map_data, (screen_width, screen_height), clamp_camera=True)

        # Создание группы спрайтов с картой
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)

    def draw(self, surface):
        # Отрисовка карты
        self.group.draw(surface)

    def update(self, dt):
        # Обновление группы спрайтов (если необходимо)
        self.group.update(dt)

    def move_camera(self, position):
        # Перемещение камеры к указанной позиции
        self.group.center(position)