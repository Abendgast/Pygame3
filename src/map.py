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
        self.map_layer.zoom = 6.5  # масштабування

        # Створення групи спрайтів, яка включає картку та гравця
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)

        # Слой колізій
        self.collision_layer = self.get_collision_layer()

    def get_collision_layer(self):
        # Повернення тайлів колізії
        collision_tiles = []
        for x, y, gid in self.tmx_data.get_layer_by_name('Collision'):
            tile = self.tmx_data.get_tile_image_by_gid(gid)
            if tile:
                rect = pygame.Rect(x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight,
                                   self.tmx_data.tilewidth, self.tmx_data.tileheight)
                collision_tiles.append(rect)
        return collision_tiles

    def check_collision(self, rect):
        # Перевірка колізії
        for tile_rect in self.collision_layer:
            if rect.colliderect(tile_rect):
                return True
        return False

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
        self.group.add(player, layer=4)
