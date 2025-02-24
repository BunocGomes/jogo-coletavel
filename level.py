# level.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
from collectibles import Coin, Key, Diamond, Portal

class LevelNode:
    def __init__(self, level_num, required_keys):
        self.level_num = level_num
        self.required_keys = required_keys  # Chaves necessárias para desbloquear este nível
        self.collectibles = pygame.sprite.Group()
        self.portal = None  # Portal para o próximo nível
        self.left = None  # Nível filho à esquerda
        self.right = None  # Nível filho à direita
        self.generate_collectibles()

    def generate_collectibles(self):
        # Gera os coletáveis com base no número do nível
        if self.level_num == 1:
            self.collectibles.add(Coin(100, 100))
            self.collectibles.add(Key(200, 200))
        elif self.level_num == 2:
            self.collectibles.add(Diamond(300, 300))
            self.collectibles.add(Key(400, 400))
            self.collectibles.add(Key(500, 500))  # Segunda chave no nível 2
            self.portal = Portal(600, 600)  # Portal no nível 2
        elif self.level_num == 3:
            self.collectibles.add(Key(500, 500))
            self.collectibles.add(Key(600, 600))
            self.collectibles.add(Key(700, 700))

    def is_unlocked(self, keys_collected):
        # Verifica se o jogador tem chaves suficientes para desbloquear este nível
        return keys_collected >= self.required_keys

class LevelTree:
    def __init__(self):
        # Constrói a árvore de níveis
        self.root = LevelNode(1, 0)  # Nível 1 não requer chaves
        self.root.left = LevelNode(2, 2)  # Nível 2 requer 2 chaves
        self.root.right = LevelNode(3, 3)  # Nível 3 requer 3 chaves

    def get_current_level(self, current_level_num):
        # Retorna o nó do nível atual
        return self._find_level(self.root, current_level_num)

    def _find_level(self, node, level_num):
        # Função auxiliar para encontrar um nó na árvore
        if node is None:
            return None
        if node.level_num == level_num:
            return node
        left_result = self._find_level(node.left, level_num)
        if left_result:
            return left_result
        return self._find_level(node.right, level_num)