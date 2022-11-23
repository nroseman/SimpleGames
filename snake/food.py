import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((64, 64))
        self.image.fill('chartreuse')
        self.rect = self.image.get_rect(topleft=(128, 128))
