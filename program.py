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
        self.buttons.append(FONT.render(option, False, (255, 255, 255)))
        self.functions.append(callback)

    def switch(self, direction):
        self.current_option = max(0, min(self.current_option + direction, len(self.buttons) - 1))

    def select(self):
        self.functions[self.current_option]()

    def draw(self, surf, x, y, option):
        for index, opt in enumerate(self.buttons):
            option_rect = opt.get_rect()
            option_rect.topleft = (x, y + index * option)
            if index == self.current_option:
                draw.rect(surf, pygame.Color('green'), option_rect)
            surf.blit(opt, option_rect)


menu = Menu()
menu.append_option('New game', lambda: print('New game'))
menu.append_option('Player statistics', lambda: print('statistic'))
menu.append_option('Quit', quit)

if __name__ == '__main__':
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
        screen.fill((0, 0, 0))
        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()


    pygame.quit()

