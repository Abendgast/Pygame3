import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, game_map):
        super().__init__()
        # Завантаження анімації та рухів
        self.animations = self.load_animations(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Tilesets\Ninja Adventure - Asset Pack\Actor\Characters\RedNinja3\SeparateAnim\Walk.png")
        self.current_animation = self.animations["down"]
        self.frame_index = 0
        self.animation_speed = 0.1  # швидкість зміни кадрів
        self.sprint = False
        self.map = game_map

        self.image = self.current_animation[self.frame_index]
        self.rect = self.image.get_rect(center=position)
        self.speed = 100

    def load_animations(self, filepath):
        sprite_sheet = pygame.image.load(filepath).convert_alpha()
        animations = {
            "down": [],
            "up": [],
            "left": [],
            "right": []
        }
        # Розмір кадра
        frame_width = 16
        frame_height = 16

        # Нарізка кадрів
        for j in range(4):
            animations["down"].append(sprite_sheet.subsurface(pygame.Rect(0 * frame_width, j * frame_height, frame_width, frame_height)))
            animations["up"].append(sprite_sheet.subsurface(pygame.Rect(1 * frame_width, j * frame_height, frame_width, frame_height)))
            animations["left"].append(sprite_sheet.subsurface(pygame.Rect(2 * frame_width, j * frame_height, frame_width, frame_height)))
            animations["right"].append(sprite_sheet.subsurface(pygame.Rect(3 * frame_width, j * frame_height, frame_width, frame_height)))

        return animations

    def update(self, dt, keys):
        original_rect = self.rect.copy()
        dx, dy = 0, 0
        moving = False

        if keys[pygame.K_LCTRL]:
            self.sprint = True
            self.animation_speed = 0.2
            self.speed = 150
        else:
            self.sprint = False
            self.speed = 100
            self.animation_speed = 0.1

        if keys[pygame.K_w]:
            dy -= self.speed * dt
            self.current_animation = self.animations["up"]
            moving = True

        if keys[pygame.K_s]:
            dy += self.speed * dt
            self.current_animation = self.animations["down"]
            moving = True

        if keys[pygame.K_a]:
            dx -= self.speed * dt
            self.current_animation = self.animations["left"]
            moving = True

        if keys[pygame.K_d]:
            dx += self.speed * dt
            self.current_animation = self.animations["right"]
            moving = True

        # перевірка колізій X
        self.rect.x += dx
        if self.map.check_collision(self.rect):
            self.rect.x = original_rect.x  # повернення в дефолтне положення X

        # перевірка колізій Y
        self.rect.y += dy
        if self.map.check_collision(self.rect):
            self.rect.y = original_rect.y  # повернення в дефолтне положення Y

        # Анімація руху
        if moving:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.current_animation):
                self.frame_index = 0
            self.image = self.current_animation[int(self.frame_index)]
        else:
            self.frame_index = 0
            self.image = self.current_animation[int(self.frame_index)]