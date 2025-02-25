import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, COIN_SOUND, KEY_SOUND, DIAMOND_SOUND, PORTAL_SOUND, BACKGROUNDS_DIR, IMAGES_DIR
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

# Configurações da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu Jogo")
clock = pygame.time.Clock()

# Carrega os cenários
background1 = pygame.image.load(os.path.join(BACKGROUNDS_DIR, 'background1.png'))
background2 = pygame.image.load(os.path.join(BACKGROUNDS_DIR, 'background2.png'))
background3 = pygame.image.load(os.path.join(BACKGROUNDS_DIR, 'background3.png'))

# Carrega as imagens dos objetos estáticos
wall_image = pygame.image.load(os.path.join(IMAGES_DIR, 'wall.png'))
tree_image = pygame.image.load(os.path.join(IMAGES_DIR, 'tree.png'))
rock_image = pygame.image.load(os.path.join(IMAGES_DIR, 'rock.png'))
path_image = pygame.image.load(os.path.join(IMAGES_DIR, 'path.png'))
bush_image = pygame.image.load(os.path.join(IMAGES_DIR, 'bush.png'))
flower_image = pygame.image.load(os.path.join(IMAGES_DIR, 'flower.png'))

# Inicializa o jogador, inventário e árvore de níveis
player = Player()
inventory = Inventory()
level_tree = LevelTree()
current_level_node = level_tree.root  # Começa no nível 1

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(current_level_node.collectibles)

# Adiciona os portais ao grupo de sprites
if current_level_node.portal:
    all_sprites.add(current_level_node.portal)
if current_level_node.portal2:
    all_sprites.add(current_level_node.portal2)

# Cria paredes
walls = pygame.sprite.Group()
for x in range(0, SCREEN_WIDTH, 32):
    wall = pygame.sprite.Sprite()
    wall.image = wall_image
    wall.rect = wall.image.get_rect(topleft=(x, 0))
    walls.add(wall)
    wall = pygame.sprite.Sprite()
    wall.image = wall_image
    wall.rect = wall.image.get_rect(topleft=(x, SCREEN_HEIGHT - 32))
    walls.add(wall)
for y in range(32, SCREEN_HEIGHT - 32, 32):
    wall = pygame.sprite.Sprite()
    wall.image = wall_image
    wall.rect = wall.image.get_rect(topleft=(0, y))
    walls.add(wall)
    wall = pygame.sprite.Sprite()
    wall.image = wall_image
    wall.rect = wall.image.get_rect(topleft=(SCREEN_WIDTH - 32, y))
    walls.add(wall)

# Adiciona objetos estáticos (árvores, pedras, arbustos e flores)
static_objects = pygame.sprite.Group()
tree1 = pygame.sprite.Sprite()
tree1.image = tree_image
tree1.rect = tree1.image.get_rect(topleft=(175, 225))
static_objects.add(tree1)

tree2 = pygame.sprite.Sprite()
tree2.image = tree_image
tree2.rect = tree2.image.get_rect(topleft=(400, 300))
static_objects.add(tree2)

rock1 = pygame.sprite.Sprite()
rock1.image = rock_image
rock1.rect = rock1.image.get_rect(topleft=(500, 100))
static_objects.add(rock1)

bush1 = pygame.sprite.Sprite()
bush1.image = bush_image
bush1.rect = bush1.image.get_rect(topleft=(100, 400))
static_objects.add(bush1)

flower1 = pygame.sprite.Sprite()
flower1.image = flower_image
flower1.rect = flower1.image.get_rect(topleft=(300, 500))
static_objects.add(flower1)

# Adiciona o caminho (blocos de grama)
path_tiles = pygame.sprite.Group()
for x in range(100, 700, 64):
    path_tile = pygame.sprite.Sprite()
    path_tile.image = path_image
    path_tile.rect = path_tile.image.get_rect(topleft=(x, 400))
    path_tiles.add(path_tile)

# Adiciona todos os sprites ao grupo principal
all_sprites.add(walls)
all_sprites.add(static_objects)
all_sprites.add(path_tiles)

# Variável para controlar o tempo de espera do portal
portal_cooldown = 0  # Tempo restante em segundos

# Função para desenhar o fundo correspondente ao nível atual
def draw_background():
    if current_level_node.level_num == 1:
        screen.blit(background1, (0, 0))
    elif current_level_node.level_num == 2:
        screen.blit(background2, (0, 0))
    elif current_level_node.level_num == 3:
        screen.blit(background3, (0, 0))

# Alteração no código da função draw_hud
def draw_hud():
    # Fonte para o HUD
    font = pygame.font.SysFont('Arial', 24)

    # Exibe o número de chaves
    keys_text = font.render(f'Chaves: {inventory.items["key"]}', True, WHITE)
    screen.blit(keys_text, (10, 10))

    # Exibe o número de diamantes
    diamonds_text = font.render(f'Diamantes: {inventory.items["diamond"]}', True, WHITE)
    screen.blit(diamonds_text, (10, 40))

    # Exibe o nível atual
    level_text = font.render(f'Nível: {current_level_node.level_num}', True, WHITE)
    screen.blit(level_text, (SCREEN_WIDTH - 150, 10))

    # Exibe o progresso do jogador
    progress_text = font.render(f'Progresso: {inventory.items["key"]} / {current_level_node.required_keys}', True, WHITE)
    screen.blit(progress_text, (SCREEN_WIDTH - 250, 40))

# Loop principal do jogo
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza o tempo de espera do portal
    if portal_cooldown > 0:
        portal_cooldown -= 1 / FPS  # Reduz o tempo restante

    # Atualiza o jogador
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Verifica colisões com paredes
    if pygame.sprite.spritecollide(player, walls, False):
        # Reverte o movimento do jogador se colidir com uma parede
        if keys[pygame.K_LEFT]:
            player.rect.x += player.speed
        if keys[pygame.K_RIGHT]:
            player.rect.x -= player.speed
        if keys[pygame.K_UP]:
            player.rect.y += player.speed
        if keys[pygame.K_DOWN]:
            player.rect.y -= player.speed

    # Verifica colisões com coletáveis
    collisions = pygame.sprite.spritecollide(player, current_level_node.collectibles, True)
    for item in collisions:
        inventory.add_item(item)
        inventory.display()  # Exibe o inventário atualizado

        # Tocar som de coleta
        if item.type == 'coin':
            coin_sound.play()
        elif item.type == 'key':
            key_sound.play()
        elif item.type == 'diamond':
            diamond_sound.play()

    # Verifica colisão com os portais
    if current_level_node.portal and pygame.sprite.collide_rect(player, current_level_node.portal):
        if portal_cooldown <= 0:  # Verifica se o portal pode ser acessado
            if current_level_node.portal_unlocked:
                # Se o portal já estiver desbloqueado, permite a transição
                portal_sound.play()
                if current_level_node.level_num == 1:
                    # Portal no nível 1 (canto inferior esquerdo) leva ao nível 2
                    current_level_node = level_tree.root.left
                    # Reinicia o estado do portal
                    current_level_node.portal_unlocked = False
                    current_level_node.portal2_unlocked = False
                elif current_level_node.level_num == 2:
                    # Portal no nível 2 leva de volta ao nível 1
                    current_level_node = level_tree.root
                elif current_level_node.level_num == 3:
                    # Portal no nível 3 leva de volta ao nível 1
                    current_level_node = level_tree.root

                # Atualiza os sprites para o novo nível
                all_sprites.empty()
                all_sprites.add(player)
                all_sprites.add(current_level_node.collectibles)
                if current_level_node.portal:
                    all_sprites.add(current_level_node.portal)
                if current_level_node.portal2:
                    all_sprites.add(current_level_node.portal2)
                all_sprites.add(walls)
                all_sprites.add(static_objects)
                all_sprites.add(path_tiles)

                # Ativa o tempo de espera do portal (2 segundos)
                portal_cooldown = 2
            else:
                # Se o portal não estiver desbloqueado, verifica se o jogador tem chaves suficientes
                keys_collected = inventory.items['key']
                if current_level_node.is_unlocked(keys_collected):
                    # Gasta as chaves para desbloquear o portal
                    inventory.items['key'] -= current_level_node.required_keys
                    current_level_node.portal_unlocked = True
                    print(f"Portal desbloqueado! Chaves restantes: {inventory.items['key']}")
                else:
                    print("Chaves insuficientes! Colete mais chaves.")

    # Verifica colisão com o portal2 (portal de vitória no nível 3)
    if current_level_node.portal2 and pygame.sprite.collide_rect(player, current_level_node.portal2):
        if portal_cooldown <= 0:  # Verifica se o portal pode ser acessado
            if current_level_node.level_num == 3:  # Portal de vitória
                if inventory.items['diamond'] >= 1:
                    print("PARABÉNS! VOCÊ VENCEU O JOGO!")
                    running = False  # Encerra o jogo
                else:
                    print("Você precisa de um diamante para usar este portal!")
            else:
                if current_level_node.portal2_unlocked:
                    portal_sound.play()
                    if current_level_node.level_num == 1:
                        current_level_node = level_tree.root.right
                        current_level_node.portal_unlocked = False

                    # Atualiza os sprites para o novo nível
                    all_sprites.empty()
                    all_sprites.add(player)
                    all_sprites.add(current_level_node.collectibles)
                    if current_level_node.portal:
                        all_sprites.add(current_level_node.portal)
                    if current_level_node.portal2:
                        all_sprites.add(current_level_node.portal2)
                    all_sprites.add(walls)
                    all_sprites.add(static_objects)
                    all_sprites.add(path_tiles)

                    # Ativa o tempo de espera do portal (2 segundos)
                    portal_cooldown = 2
                else:
                    keys_collected = inventory.items['key']
                    if current_level_node.is_unlocked(keys_collected):
                        inventory.items['key'] -= current_level_node.required_keys
                        current_level_node.portal2_unlocked = True
                        print(f"Portal desbloqueado! Chaves restantes: {inventory.items['key']}")
                    else:
                        print("Chaves insuficientes! Colete mais chaves.")

    # Desenha o fundo e os sprites
    draw_background()
    all_sprites.draw(screen)
    
    # Desenha o HUD
    draw_hud()
    
    # Atualiza a tela
    pygame.display.flip()

pygame.quit()