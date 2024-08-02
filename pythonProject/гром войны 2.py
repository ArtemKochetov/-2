import pygame
import os


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


WIDTH = 1400
HEIGHT = 950
pygame.init()
pygame.display.init()
pygame.display.set_caption('гром войны 2')
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(load_image('icon.png'))
screen = pygame.display.get_surface()

clock = pygame.time.Clock()
taps = pygame.sprite.Group()


class Tap(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        super().__init__(group)
        image = load_image('money.png', -1)
        self.image = pygame.transform.scale(image, (60, 22))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.n = 0


def start_screen():
    with open('data/info', 'r') as read_file:
        info = [line.strip() for line in read_file]
        print(info)
        lvl = int(info[0])
        money = int(info[1])
        tank = str(info[2])
        read_file.close()
    img = pygame.transform.scale(load_image(f'{tank}.png'), (1000, 532))
    img_money = pygame.transform.scale(load_image('free-icon-money-1447.png'), (44, 44))
    intro_text = [f"Твой уровень: {lvl}"]
    font = pygame.font.Font(None, 50)
    screen.blit(img, (200, 250))
    while True:
        screen.fill('black')
        screen.blit(img, (200, 250))
        string_rendered = font.render(intro_text[0], True, pygame.Color('orange'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 900
        intro_rect.x = 25
        string_rendered2 = font.render(str(money), True, pygame.Color('orange'))
        intro_rect2 = string_rendered2.get_rect()
        intro_rect2.x = 1062
        intro_rect2.top = 900
        screen.blit(string_rendered, intro_rect)
        screen.blit(string_rendered2, intro_rect2)
        screen.blit(img_money, (1012, 894))
        for t in taps:
            t.n += 1
            if t.n > 20:
                taps.remove(t)
            t.rect.y -= 2
        taps.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 2):
                money += 10
                x, y = pygame.mouse.get_pos()
                Tap(taps, x - 10, y - 15)
        with open('data/info', 'w') as write_file:
            write_file.write(str(lvl) + '\n' + str(money) + '\n' + str(tank))
            write_file.close()
        clock.tick(60)
        pygame.display.flip()


start_screen()


def play():
    pygame.mouse.set_visible(True)
    ticks = 0
    speed = 1
    running = True
    playing = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if playing:
            pygame.display.flip()
        clock.tick(60)


play()
pygame.quit()
