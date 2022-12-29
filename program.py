import pygame.font
from pygame import *
import random
import math

vec2, vec3 = pygame.math.Vector2, pygame.math.Vector3
pygame.font.init()
FONT = pygame.font.SysFont('calibry', 50)
RES = WIDTH, HEIGHT = 1600, 900
NUM_STARS = 101

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
        if self.current_option == 0:
            switch_scene(game)
        self.functions[self.current_option]()

    def draw(self, surf, x, y, option):
        for index, opt in enumerate(self.buttons):
            option_rect = opt.get_rect()
            option_rect.topleft = (x, y + index * option)
            if index == self.current_option:
                draw.rect(surf, pygame.Color('green'), option_rect)
            surf.blit(opt, option_rect)

class Star:
    def __init__(self, app):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass

class Starfild:
    def __init__(self, app):
        self.stars = [Star(app) for i in range(NUM_STARS)]
    
    def run(self):
        [star.update() for star in self.stars]
        [star.draw() for star in self.stars]
        
class Wallpaper:
    def __init__(self):
        # self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.starfild = Starfild(self)
        
        
    def run(self, screen):
        screen.fill((0, 0, 0))
        self.starfild.run()
        pygame.display.flip()
        self.clock.tick()
            # pass
    

class Game:
    def __init__(self, board, size):
        self.board = board
        self.size = size
        self.loadImages()
        # необходимо найти картинки

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.draw()
                pygame.display.flip()
        pygame.quit()

    def draw(self):
        point = (20, 50)
        for row in self.board.getBoard():
            for column in row:
                cell = pygame.Rect(point, (25, 25))
                image = self.images[self.getImage(column)]
                self.screen.blit(image, point)
                point = point[0] + 25, point[1] # вспомнить какой я хочу задавать размер клетки
            point = 20, point[1] + 25

    def loadImages(self):
        # сделать красивее и короче
        self.images = {}
        im = pygame.image.load('empty.png')
        im = pygame.transform.scale(im, (25, 25))
        self.images['not_empty'] = im
        im = pygame.image.load('not_e.png')
        im = pygame.transform.scale(im, (25, 25))
        self.images['empty'] = im
        im = pygame.image.load('bomb.png')
        im = pygame.transform.scale(im, (25, 25))
        self.images['bomb'] = im
        # image = pygame.image.load()

    def getImage(self, cell):
        string = 'bomb' if cell.getBomb() else 'empty'
        return string


# создается доска
class Board:
    def __init__(self, size, lot_bombs):
        self.size = size
        self.board = []
        self.win = False
        self.lost = False
        for x in range(size[0]):
            i = []
            for y in range(size[1]):
                bomb = random.random() < lot_bombs
                piece = StateBomb(bomb)
                i.append(piece)
            self.board.append(i)

    def getCell(self, index):
        return self.board[index[0]][index[1]]

    def getBoard(self):
        return self.board

class StateBomb:
    def __init__(self, bomb):
        self.bomb = bomb
        self.lot_bombs_around = 0
        self.clicked = False
        self.Flagged = False

    def getBomb(self):
        return self.bomb

    def click(self):
        return self.clicked

    def flag(self):
        return self.Flagged


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
change_str = pygame.font.SysFont('calibry', 30).render(f'клавиши S и W для выбора', True, (255, 255, 255))
cont = pygame.font.SysFont('calibry', 30).render(f'нажмите пробел для выхода', True, (255, 0, 0))
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
                switch_scene(None)
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
        screen.blit(change_str, (0, 775))
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
        screen.blit(cont, (220, 350))
        pygame.display.flip()
    pygame.quit()


def game():
    board = Board((20, 20), 0.25)
    screenSize = (800, 800)
    game = Game(board, screenSize)
    game.run()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # почему-то не работает
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #     running = False
            #     switch_scene(scene1)
    pygame.quit()


switch_scene(scene1)
while current_scene is not None:
    current_scene()
