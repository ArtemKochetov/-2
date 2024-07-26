import pygame
import os

WIDTH = 1000
HEIGHT = 800
pygame.init()
pygame.display.set_caption('Арканоид')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load('data/1682210358_papik-pro-p-stikeri-var-tander-vektor-36.jpg'))


def play():
    pygame.mouse.set_visible(True)
    ticks = 0
    speed = 1
    clock = pygame.time.Clock()
    running = True
    playing = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if playing:
            pygame.display.flip()
            if ticks >= speed:
                ticks = 0
        ticks += 1
        clock.tick(60)


play()
pygame.quit()
