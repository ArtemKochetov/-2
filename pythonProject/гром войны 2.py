import pygame
import os

WIDTH = 1400
HEIGHT = 950
pygame.init()
pygame.display.set_caption('Арканоид')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load('data/1682210358_papik-pro-p-stikeri-var-tander-vektor-36.jpg'))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():

    with open('data/info', 'r') as read_file:
        info = [line.strip() for line in read_file]
        print(info)
        lvl = int(info[0])
        money = int(info[1])
        tank = str(info[2])
        read_file.close()
    img = pygame.transform.scale(load_image(f'{tank}.png'), (1000, 532))
    img_money = pygame.transform.scale(load_image('gold-coin-money-symbol-icon-png.webp'), (34, 34))
    intro_text = [f"Твой уровень: {lvl}", str(money)]
    font = pygame.font.Font(None, 50)
    while True:
        screen.blit(img, (200, 250))
        string_rendered = font.render(intro_text[0], True, pygame.Color('orange'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 900
        intro_rect.x = 25
        string_rendered2 = font.render(intro_text[1], True, pygame.Color('orange'))
        intro_rect2 = string_rendered2.get_rect()
        intro_rect2.top = 900
        intro_rect2.x = 1062
        screen.blit(string_rendered, intro_rect)
        screen.blit(string_rendered2, intro_rect2)
        screen.blit(img_money, (1020, 898))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                pass
        pygame.display.flip()


start_screen()


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
