import pygame
import pytmx
import pyscroll

class Map:
    def __init__(self, filename):
        # завантаження TMX карти
        self.tmx_data = pytmx.util_pygame.load_pygame(filename)

        # створення данных для прокрутки карти
        map_data = pyscroll.data.TiledMapData(self.tmx_data)

        # налаштування рендерера для відтворення карти
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.map_layer = pyscroll.BufferedRenderer(map_data, (screen_width, screen_height))
        self.map_layer.zoom = 1  # масштабування

        # Створення групи спрайтів, яка включає картку та гравця
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)

    def draw(self, surface):
        # Малювання карти та об'єктів
        self.group.draw(surface)

    def update(self, dt, keys):
        # Оновлення логіки групи, передаємо `keys` для всіх спрайтів
        for sprite in self.group.sprites():
            sprite.update(dt, keys)

    def center_camera_on(self, position):
        # Центрування камери на заданій позиції
        self.group.center(position)

    def add_player_to_group(self, player):
        # Добавляем игрока в нужный слой
        self.group.add(player, layer=3)  # Добавляем в третий слой (начиная с 0)
