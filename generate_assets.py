from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import os
import numpy as np
from scipy.io.wavfile import write
import random

# Configurações
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
BACKGROUNDS_DIR = os.path.join(ASSETS_DIR, 'backgrounds')

# Cria as pastas se não existirem
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(SOUNDS_DIR, exist_ok=True)
os.makedirs(BACKGROUNDS_DIR, exist_ok=True)

# Inicializa o Pygame
pygame.init()

# Função para salvar imagens
def generate_images():
    # Tamanho das imagens
    size = (32, 32)

    # Player (quadrado verde)
    player_image = pygame.Surface(size)
    player_image.fill((0, 255, 0))  # Verde
    pygame.image.save(player_image, os.path.join(IMAGES_DIR, 'player.png'))

    # Coin (círculo amarelo)
    coin_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(coin_image, (255, 223, 0), (16, 16), 16)  # Amarelo
    pygame.image.save(coin_image, os.path.join(IMAGES_DIR, 'coin.png'))

    # Key (retângulo azul)
    key_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.rect(key_image, (0, 0, 255), (8, 4, 16, 24))  # Azul
    pygame.image.save(key_image, os.path.join(IMAGES_DIR, 'key.png'))

    # Diamond (losango ciano)
    diamond_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.polygon(diamond_image, (0, 255, 255), [(16, 4), (28, 16), (16, 28), (4, 16)])  # Ciano
    pygame.image.save(diamond_image, os.path.join(IMAGES_DIR, 'diamond.png'))

    # Portal (círculo vermelho)
    portal_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(portal_image, (255, 0, 0), (16, 16), 16)  # Vermelho
    pygame.image.save(portal_image, os.path.join(IMAGES_DIR, 'portal.png'))

    # Parede (bloco cinza)
    wall_image = pygame.Surface(size)
    wall_image.fill((100, 100, 100))  # Cinza
    pygame.image.save(wall_image, os.path.join(IMAGES_DIR, 'wall.png'))

    # Árvore (bloco marrom com círculo verde)
    tree_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.rect(tree_image, (139, 69, 19), (12, 16, 8, 16))  # Tronco marrom
    pygame.draw.circle(tree_image, (34, 139, 34), (16, 12), 12)  # Copa verde
    pygame.image.save(tree_image, os.path.join(IMAGES_DIR, 'tree.png'))

    # Pedra (bloco cinza escuro)
    rock_image = pygame.Surface(size)
    rock_image.fill((50, 50, 50))  # Cinza escuro
    pygame.image.save(rock_image, os.path.join(IMAGES_DIR, 'rock.png'))

    # Caminho (bloco bege)
    path_image = pygame.Surface(size)
    path_image.fill((210, 180, 140))  # Bege
    pygame.image.save(path_image, os.path.join(IMAGES_DIR, 'path.png'))

    # Arbusto (bloco verde escuro)
    bush_image = pygame.Surface(size)
    bush_image.fill((34, 139, 34))  # Verde escuro
    pygame.image.save(bush_image, os.path.join(IMAGES_DIR, 'bush.png'))

    # Flor (bloco com círculos coloridos)
    flower_image = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(flower_image, (255, 0, 0), (16, 16), 8)  # Centro vermelho
    pygame.draw.circle(flower_image, (255, 255, 0), (8, 8), 6)  # Pétala amarela
    pygame.draw.circle(flower_image, (255, 255, 0), (24, 8), 6)  # Pétala amarela
    pygame.draw.circle(flower_image, (255, 255, 0), (8, 24), 6)  # Pétala amarela
    pygame.draw.circle(flower_image, (255, 255, 0), (24, 24), 6)  # Pétala amarela
    pygame.image.save(flower_image, os.path.join(IMAGES_DIR, 'flower.png'))

# Função para gerar sons
def generate_sounds():
    # Configurações de som
    sample_rate = 44100
    duration = 1.0  # Duração do som em segundos
    frequency = 440  # Frequência do som em Hz

    # Gera um som de beep
    def generate_beep(freq, duration, volume=0.5):
        samples = int(sample_rate * duration)
        t = np.linspace(0, duration, samples, endpoint=False)
        wave = volume * np.sin(2 * np.pi * freq * t)
        return np.int16(wave * 32767)

    # Som de moeda (beep curto)
    coin_sound = generate_beep(880, 0.1)  # Beep agudo e curto
    write(os.path.join(SOUNDS_DIR, 'coin_pickup.wav'), sample_rate, coin_sound)

    # Som de chave (beep médio)
    key_sound = generate_beep(440, 0.3)  # Beep médio
    write(os.path.join(SOUNDS_DIR, 'key_pickup.wav'), sample_rate, key_sound)

    # Som de diamante (beep longo)
    diamond_sound = generate_beep(220, 0.5)  # Beep grave e longo
    write(os.path.join(SOUNDS_DIR, 'diamond_pickup.wav'), sample_rate, diamond_sound)

    # Som de portal (som descendente)
    portal_sound = generate_beep(880, 1.0)  # Som descendente
    write(os.path.join(SOUNDS_DIR, 'portal_open.wav'), sample_rate, portal_sound)

# Função para gerar cenários
def generate_backgrounds():
    # Tamanho do cenário
    size = (800, 600)  # Tamanho da tela

    # Cenário do nível 1 (fundo verde com textura)
    background1 = pygame.Surface(size)
    background1.fill((0, 100, 0))  # Verde escuro
    for i in range(0, SCREEN_WIDTH, 64):
        for j in range(0, SCREEN_HEIGHT, 64):
            pygame.draw.rect(background1, (0, 150, 0), (i, j, 64, 64), 2)  # Grade verde
    pygame.image.save(background1, os.path.join(BACKGROUNDS_DIR, 'background1.png'))

    # Cenário do nível 2 (fundo azul com textura)
    background2 = pygame.Surface(size)
    background2.fill((0, 0, 100))  # Azul escuro
    for i in range(0, SCREEN_WIDTH, 64):
        for j in range(0, SCREEN_HEIGHT, 64):
            pygame.draw.rect(background2, (0, 0, 150), (i, j, 64, 64), 2)  # Grade azul
    pygame.image.save(background2, os.path.join(BACKGROUNDS_DIR, 'background2.png'))

    # Cenário do nível 3 (fundo vermelho com textura)
    background3 = pygame.Surface(size)
    background3.fill((100, 0, 0))  # Vermelho escuro
    for i in range(0, SCREEN_WIDTH, 64):
        for j in range(0, SCREEN_HEIGHT, 64):
            pygame.draw.rect(background3, (150, 0, 0), (i, j, 64, 64), 2)  # Grade vermelha
    pygame.image.save(background3, os.path.join(BACKGROUNDS_DIR, 'background3.png'))

# Função para distribuir os itens sem sobreposição
def place_items_randomly():
    items = ['coin', 'key', 'diamond', 'portal', 'tree', 'rock', 'path', 'bush', 'flower']
    item_positions = []

    for item in items:
        # Gerar posição aleatória para cada item
        x = random.randint(0, SCREEN_WIDTH - 32)  # Garantir que o item não saia da tela
        y = random.randint(0, SCREEN_HEIGHT - 32)
        
        # Verificar se o item está sobrepondo outro item
        while any(abs(x - ix) < 32 and abs(y - iy) < 32 for ix, iy in item_positions):
            x = random.randint(0, SCREEN_WIDTH - 32)
            y = random.randint(0, SCREEN_HEIGHT - 32)
        
        item_positions.append((x, y))
        print(f"{item} posicionado em ({x}, {y})")

# Gera os assets
generate_images()
generate_sounds()
generate_backgrounds()

# Distribui itens aleatoriamente
place_items_randomly()

print("Assets gerados e itens distribuídos com sucesso!")
