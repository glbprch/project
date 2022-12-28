import pygame.font
from pygame import *
pygame.font.init()
FONT = pygame.font.SysFont('calibry', 50) 


class Menu:
    def __init__(self):
        self.buttons = []
        self.functions = []
        self.current_option = 0

    def append_option(self, option, callback):
        self.buttons.append(FONT.render(option, True, (255, 255, 255)))
        self.functions.append(callback)

    def switch(self, direction):
        self.current_option = max(0, min(self.current_option + direction, len(self.buttons) - 1))

    def select(self):
        if self.current_option == 1:
            switch_scene(stats)
        self.functions[self.current_option]()

    def draw(self, surf, x, y, option):
        for index, opt in enumerate(self.buttons):
            option_rect = opt.get_rect()
            option_rect.topleft = (x, y + index * option)
            if index == self.current_option:
                draw.rect(surf, pygame.Color('green'), option_rect)
            surf.blit(opt, option_rect)


class Wallpaper:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
    def run(self):
        while True:
            self.screen.fill ('black')
            
            pg.display.flip()
            [exit() for i in pg.events.get() if i.tipe == pg.QUIT]
            self.clock.tick()
            
    def run(self, screen):
        screen.fill((0, 0, 0))
        pass


def switch_scene(scene):
    global current_scene
    current_scene = scene


current_scene = None

menu = Menu()
menu.append_option('Новая игра', lambda: print('new game'))
menu.append_option('Статистика игрока', lambda: print('statistic'))
menu.append_option('Выйти', quit)
# создать бд и читать количесво побед от туда
all_games = FONT.render(f'Всего игр сыграно: {0}', True, (255, 0, 0))
wallpaper = Wallpaper()

def scene1():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Сапер')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    menu.switch(-1)
                elif event.key == K_s:
                    menu.switch(1)
                elif event.key == K_SPACE:
                    menu.select()
                    running = False
        wallpaper.run(screen)
        menu.draw(screen, 250, 300, 75)
        pygame.display.flip()
    pygame.quit()

def stats():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Сапер')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
                switch_scene(scene1)
        wallpaper.run(screen)
        draw.rect(screen, (255, 255, 255), (200, 200, 400, 400))
        screen.blit(all_games, (220, 300))
        pygame.display.flip()
    pygame.quit()


switch_scene(scene1)
while current_scene is not None:
    current_scene()
