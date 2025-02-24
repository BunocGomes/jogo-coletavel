# settings.py

import os

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tamanho do tile
TILE_SIZE = 32

# Caminhos para assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
BACKGROUNDS_DIR = os.path.join(ASSETS_DIR, 'backgrounds')  # Nova constante

# Carregar imagens
PLAYER_IMAGE = os.path.join(IMAGES_DIR, 'player.png')
COIN_IMAGE = os.path.join(IMAGES_DIR, 'coin.png')
KEY_IMAGE = os.path.join(IMAGES_DIR, 'key.png')
DIAMOND_IMAGE = os.path.join(IMAGES_DIR, 'diamond.png')
PORTAL_IMAGE = os.path.join(IMAGES_DIR, 'portal.png')

# Carregar sons
COIN_SOUND = os.path.join(SOUNDS_DIR, 'coin_pickup.wav')
KEY_SOUND = os.path.join(SOUNDS_DIR, 'key_pickup.wav')
DIAMOND_SOUND = os.path.join(SOUNDS_DIR, 'diamond_pickup.wav')
PORTAL_SOUND = os.path.join(SOUNDS_DIR, 'portal_open.wav')