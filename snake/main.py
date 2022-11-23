import pygame
import sys
from snake import Snake
from food import Food


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 768


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption = 'SNAKE'
        self.clock = pygame.time.Clock()
        self.running = True

        # sprite group
        self.food_sprites = pygame.sprite.Group()
        self.food = Food(self.food_sprites)
        self.snake = Snake(self.food_sprites)

    def add_food(self):
        if not self.food_sprites.sprites():
            self.food = Food(self.food_sprites)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            # delta time
            dt = self.clock.tick() / 1000
            # update
            self.display_surface.fill('red')
            self.food_sprites.update(dt)
            self.snake.update(dt)
            self.add_food()
            # draw
            self.food_sprites.draw(self.display_surface)
            self.snake.draw(self.display_surface)
            # render frame
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
