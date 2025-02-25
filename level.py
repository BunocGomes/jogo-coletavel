# level.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
from collectibles import Coin, Key, Diamond, Portal

class LevelNode:
    def __init__(self, level_num, required_keys):
        self.level_num = level_num
        self.required_keys = required_keys
        self.collectibles = pygame.sprite.Group()
        self.portal = None  # Portal principal
        self.portal2 = None  # Portal secundário (ou de vitória)
        self.portal_unlocked = False
        self.portal2_unlocked = False
        self.left = None
        self.right = None
        self.generate_collectibles()

    def generate_collectibles(self):
        if self.level_num == 1:
            self.collectibles.add(Coin(100, 100))
            self.collectibles.add(Key(200, 200))
            self.portal = Portal(50, SCREEN_HEIGHT - 100)  # Portal para o nível 2
            self.portal2 = Portal(50, 50)  # Portal para o nível 3

        elif self.level_num == 2:
            self.collectibles.add(Diamond(300, 300))
            self.collectibles.add(Key(400, 400))  # Apenas 1 chave agora
            self.portal = Portal(50, SCREEN_HEIGHT - 100)  # Portal de volta para o nível 1

        elif self.level_num == 3:
            self.collectibles.add(Key(500, 500))
            self.collectibles.add(Key(600, 600))
            self.collectibles.add(Diamond(700, 700))  # Diamante para o portal de vitória
            self.portal = Portal(50, 50)  # Portal de volta para o nível 1
            self.portal2 = Portal(700, 500)  # Novo portal de vitória

    def is_unlocked(self, keys_collected):
        return keys_collected >= self.required_keys

class LevelTree:
    def __init__(self):
        self.root = LevelNode(1, 0)  # Nível 1: 0 chaves
        self.root.left = LevelNode(2, 1)  # Nível 2: 1 chave
        self.root.right = LevelNode(3, 2)  # Nível 3: 2 chaves

    def get_current_level(self, current_level_num):
        return self._find_level(self.root, current_level_num)

    def _find_level(self, node, level_num):
        if node is None:
            return None
        if node.level_num == level_num:
            return node
        left_result = self._find_level(node.left, level_num)
        if left_result:
            return left_result
        return self._find_level(node.right, level_num)