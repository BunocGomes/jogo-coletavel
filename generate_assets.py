# generate_assets.py

import pygame
import os
import numpy as np
from scipy.io.wavfile import write

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

    # Cenário do nível 1 (fundo verde)
    background1 = pygame.Surface(size)
    background1.fill((0, 100, 0))  # Verde escuro
    pygame.image.save(background1, os.path.join(BACKGROUNDS_DIR, 'background1.png'))

    # Cenário do nível 2 (fundo azul)
    background2 = pygame.Surface(size)
    background2.fill((0, 0, 100))  # Azul escuro
    pygame.image.save(background2, os.path.join(BACKGROUNDS_DIR, 'background2.png'))

    # Cenário do nível 3 (fundo vermelho)
    background3 = pygame.Surface(size)
    background3.fill((100, 0, 0))  # Vermelho escuro
    pygame.image.save(background3, os.path.join(BACKGROUNDS_DIR, 'background3.png'))

# Gera os assets
generate_images()
generate_sounds()
generate_backgrounds()

print("Assets gerados com sucesso!")