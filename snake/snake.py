import pygame
from pygame.math import Vector2 as vector
from settings import *


class Snake:
    def __init__(self, collision_sprites) -> None:
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft=(640, 384))
        self.pos = vector(self.rect.topleft)
        self.pos_list = [vector(self.rect.topleft)]
        self.direction = vector(0, 1)
        self.speed = 200
        self.moving = True
        self.start_time = pygame.time.get_ticks()

        self.collision_sprites = collision_sprites
        self.alive = True

    def input(self):

        keys = pygame.key.get_pressed()

        # only allow one direction at a time and not go backwards
        if keys[pygame.K_DOWN] and not self.direction == vector(0, -1):
            self.direction = vector(0, 1)
        elif keys[pygame.K_UP] and not self.direction == vector(0, 1):
            self.direction = vector(0, -1)
        elif keys[pygame.K_RIGHT] and not self.direction == vector(-1, 0):
            self.direction = vector(1, 0)
        elif keys[pygame.K_LEFT] and not self.direction == vector(1, 0):
            self.direction = vector(-1, 0)

    def move(self, dt):
        if self.moving and (pygame.time.get_ticks() - self.start_time >= self.speed):
            position = vector(self.pos_list.copy()[0])

            position.x += self.direction.x * 64
            position.y += self.direction.y * 64

            self.pos_list.insert(0, position)

            if self.food_collision():
                print('yum')
            else:
                self.pos_list.pop()
            self.body_collision()
            self.wall_collision()
            self.moving = False
        if not self.moving:
            self.start_time = pygame.time.get_ticks()
            self.moving = True

    def food_collision(self):
        for food in self.collision_sprites.sprites():
            if food.rect.colliderect(self.image.get_rect(topleft=self.pos_list[0])):
                food.kill()
                return True
        return False

    def body_collision(self):
        head = self.pos_list[0]
        for block in self.pos_list[1:]:
            if head == block:
                self.alive = False

    def wall_collision(self):
        if self.pos_list[0].x < 0 or self.pos_list[0].x >= WINDOW_WIDTH:
            self.alive = False
        if self.pos_list[0].y < 0 or self.pos_list[0].y >= WINDOW_HEIGHT:
            self.alive = False

    def draw(self, surface):
        for block in self.pos_list:
            surface.blit(self.image, self.image.get_rect(topleft=block))

    def update(self, dt):
        self.input()
        self.move(dt)
