from email.policy import default

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # Завантаження анімації та рухів
        self.animations = self.load_animations(r"C:\Users\Spril\Work\Pygame3\Pygame3\assets\images\Tilesets\Ninja Adventure - Asset Pack\Actor\Characters\SamuraiRed\SeparateAnim\Walk.png")
        self.current_animation = self.animations["down"]
        self.frame_index = 0
        self.animation_speed = 0.1  # швидкість зміни кадрів
        self.sprint = False

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
        for j in range(4):  # теперь перебираем кадры для каждого направления
            animations["down"].append(sprite_sheet.subsurface(pygame.Rect(0 * frame_width, j * frame_height, frame_width, frame_height)))
            animations["up"].append(sprite_sheet.subsurface(pygame.Rect(1 * frame_width, j * frame_height, frame_width, frame_height)))
            animations["left"].append(sprite_sheet.subsurface(pygame.Rect(2 * frame_width, j * frame_height, frame_width, frame_height)))
            animations["right"].append(sprite_sheet.subsurface(pygame.Rect(3 * frame_width, j * frame_height, frame_width, frame_height)))

        return animations

    def update(self, dt, keys):
        dx = 0
        dy = 0
        moving = False  # Флаг для отслеживания движения
        #
        if self.sprint:
            self.animation_speed = 0.2
            self.speed = 150

        if keys[pygame.K_LCTRL]:
            self.sprint = True
        else:
            self.sprint = False
            self.speed = 100
            self.animation_speed = 0.1

        if keys[pygame.K_w]:
            dy = -self.speed * dt
            self.current_animation = self.animations["up"]
            moving = True

        elif keys[pygame.K_s]:
            dy = self.speed * dt
            self.current_animation = self.animations["down"]
            moving = True

        elif keys[pygame.K_a]:
            dx = -self.speed * dt
            self.current_animation = self.animations["left"]
            moving = True

        elif keys[pygame.K_d]:
            dx = self.speed * dt
            self.current_animation = self.animations["right"]
            moving = True




        #
        # if keys[pygame.K_w] and keys[pygame.K_LCTRL]:
        #     dy = -self.speed * dt
        #     self.current_animation = self.animations["up"]
        #     moving = True
        #     self.sprint = True
        # elif keys[pygame.K_s] and keys[pygame.KMOD_SHIFT]:
        #     dy = self.speed * dt
        #     self.current_animation = self.animations["down"]
        #     moving = True
        #     self.sprint = True
        # elif keys[pygame.K_a] and keys[pygame.KMOD_SHIFT]:
        #     dx = -self.speed * dt
        #     self.current_animation = self.animations["left"]
        #     moving = True
        #     self.sprint = True
        # elif keys[pygame.K_d] and keys[pygame.KMOD_SHIFT]:
        #     dx = self.speed * dt
        #     self.current_animation = self.animations["right"]
        #     moving = True
        #     self.sprint = True
        #
        # else:
        #     self.sprint = False






        # Оновлення позиції
        self.rect.x += dx
        self.rect.y += dy

        if moving:
            # Оновлення кадра анімації тільки при русі
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.current_animation):
                self.frame_index = 0
            self.image = self.current_animation[int(self.frame_index)]
        else:
            # если нет движения, возвращаемся на первый кадр текущей анимации
            self.frame_index = 0
            self.image = self.current_animation[int(self.frame_index)]