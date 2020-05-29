import pygame
from principal_character.Character import Character

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jueguito")
running = True

player = Character(0,0)
screen.fill((255,255,255))
clock = pygame.time.Clock()

def show_player():
    screen.blit(pygame.image.load(player.get_image()),(player.get_x(),player.get_y()))

while running:
    clock.tick(20)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a and player.get_x() > -100:
            player.move("left")
        if event.key == pygame.K_w and player.get_y() > -100:
            player.move("up")
        if event.key == pygame.K_s and player.get_x() < 500:
            player.move("down")
        if event.key == pygame.K_d and player.get_y() < 700:
            player.move("right")
        if event.key == pygame.K_k:
            player.die()
    else:
        player.move("stand")

    screen.fill((255, 255, 255))
    show_player()
    pygame.display.update()