import pygame
import sys
from random import randint
from snake import Snake
from food import Food
from pygame.math import Vector2 as vector
from settings import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption = 'SNAKE'
        self.clock = pygame.time.Clock()
        self.running = True

        # font
        self.font = pygame.font.Font(None, 80)

        # sprite group
        self.food_sprites = pygame.sprite.Group()
        self.food = Food(vector(128, 128), self.food_sprites)
        self.snake = Snake(self.food_sprites)

    def add_food(self):
        if not self.food_sprites.sprites():
            pos = self.get_rand_loc()
            self.food = Food(pos, self.food_sprites)

    def get_rand_loc(self):
        pos = vector((randint(0, (WINDOW_WIDTH - 64) / 64)) * 64,
                     (randint(0, (WINDOW_HEIGHT - 64) / 64)) * 64)
        while pos in self.snake.pos_list:
            pos = vector((randint(0, (WINDOW_WIDTH - 64) / 64)) * 64,
                         (randint(0, (WINDOW_HEIGHT - 64) / 64)) * 64)
        return pos

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            # delta time
            dt = self.clock.tick() / 1000
            if self.snake.alive:
                # update
                self.display_surface.fill('red')
                self.food_sprites.update(dt)
                self.snake.update(dt)

                self.add_food()
                # draw
                self.food_sprites.draw(self.display_surface)
                self.snake.draw(self.display_surface)
            else:
                self.over()
            # render frame
            pygame.display.update()

    def over(self):
        text_surf_1 = self.font.render('GAME OVER', True, 'white')
        self.display_surface.blit(text_surf_1, text_surf_1.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)))

        text_surf_2 = self.font.render('press start to retry', True, 'white')
        self.display_surface.blit(text_surf_2, text_surf_2.get_rect(
            midtop=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 80)))
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.reset()

    def reset(self):
        self.food_sprites.empty()
        self.food = Food(vector(128, 128), self.food_sprites)
        self.snake = Snake(self.food_sprites)


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
