# collectibles.py

import pygame
from settings import COIN_IMAGE, KEY_IMAGE, DIAMOND_IMAGE, PORTAL_IMAGE, TILE_SIZE

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, type):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = type

class Coin(Collectible):
    def __init__(self, x, y):
        super().__init__(x, y, COIN_IMAGE, 'coin')

class Key(Collectible):
    def __init__(self, x, y):
        super().__init__(x, y, KEY_IMAGE, 'key')

class Diamond(Collectible):
    def __init__(self, x, y):
        super().__init__(x, y, DIAMOND_IMAGE, 'diamond')

class Portal(Collectible):
    def __init__(self, x, y):
        super().__init__(x, y, PORTAL_IMAGE, 'portal')