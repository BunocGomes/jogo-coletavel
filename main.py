# main.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, COIN_SOUND, KEY_SOUND, DIAMOND_SOUND, PORTAL_SOUND
from player import Player
from inventory import Inventory
from level import LevelTree

pygame.init()

# Configurações de som
pygame.mixer.init()
coin_sound = pygame.mixer.Sound(COIN_SOUND)
key_sound = pygame.mixer.Sound(KEY_SOUND)
diamond_sound = pygame.mixer.Sound(DIAMOND_SOUND)
portal_sound = pygame.mixer.Sound(PORTAL_SOUND)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu Jogo")
clock = pygame.time.Clock()

player = Player()
inventory = Inventory()
level_tree = LevelTree()
current_level_node = level_tree.root  # Começa no nível 1

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(current_level_node.collectibles)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Verifica colisões com coletáveis
    collisions = pygame.sprite.spritecollide(player, current_level_node.collectibles, True)
    for item in collisions:
        inventory.add_item(item)
        inventory.organize()
        inventory.display()

        # Tocar som de coleta
        if item.type == 'coin':
            coin_sound.play()
        elif item.type == 'key':
            key_sound.play()
        elif item.type == 'diamond':
            diamond_sound.play()

    # Verifica colisão com o portal
    if current_level_node.portal and pygame.sprite.collide_rect(player, current_level_node.portal):
        keys_collected = sum(1 for item in inventory.slots if item and item.type == 'key')
        if current_level_node.is_unlocked(keys_collected):
            portal_sound.play()
            if current_level_node.left:
                current_level_node = current_level_node.left
            elif current_level_node.right:
                current_level_node = current_level_node.right
            all_sprites.add(current_level_node.collectibles)
            if current_level_node.portal:
                all_sprites.add(current_level_node.portal)

    # Desenha tudo na tela
    screen.fill(WHITE)
    all_sprites.draw(screen)
    if current_level_node.portal:
        screen.blit(current_level_node.portal.image, current_level_node.portal.rect)
    pygame.display.flip()

pygame.quit()