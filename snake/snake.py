import pygame
from pygame.math import Vector2 as vector


class Snake:
    def __init__(self, collision_sprites) -> None:
        self.body = []
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft=(640, 384))
        self.pos = vector(self.rect.topleft)
        self.pos_list = [vector(self.rect.topleft)]
        self.direction = vector(0, 1)
        self.speed = 200
        self.moving = True
        self.start_time = pygame.time.get_ticks()

        self.collision_sprites = collision_sprites

    def input(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.direction = vector(0, 1)
        elif keys[pygame.K_UP]:
            self.direction = vector(0, -1)
        # else:
        #     self.direction.x = 0
        elif keys[pygame.K_RIGHT]:
            self.direction = vector(1, 0)
        elif keys[pygame.K_LEFT]:
            self.direction = vector(-1, 0)
        # else:
        #     self.direction.x = 0

    # TODO: Why are vectors in self.pos_list the same at the end?????

    def move(self, dt):
        if self.moving and (pygame.time.get_ticks() - self.start_time >= self.speed):
            print(self.pos_list)
            position = vector(self.pos_list.copy()[0])
            print(position)
            position.x += self.direction.x * 64
            position.y += self.direction.y * 64
            print(position)
            self.pos_list.insert(0, position)
            print(self.pos_list)
            if self.food_collision():
                print('yum')
            else:
                self.pos_list.pop()
            print(self.pos_list)
            self.moving = False
        if not self.moving:
            self.start_time = pygame.time.get_ticks()
            self.moving = True

    def food_collision(self):
        for food in self.collision_sprites.sprites():
            if food.rect.colliderect(self.image.get_rect(topleft=self.pos_list[0])):
                food.kill()
                print('hit')
                return True
        return False

    def draw(self, surface):
        for block in self.pos_list:
            surface.blit(self.image, self.image.get_rect(topleft=block))

    def update(self, dt):
        self.input()
        self.move(dt)
