import pygame
import random
from pygame import mixer 
from menu import *


class Game():
    def __init__(self):

        #background game image
        self.game_back = pygame.image.load("game_back.png")

        #sprite variable
        self.clock = pygame.time.Clock()
        self.cat = pygame.Surface((20,20))
        self.cat.fill((255,0,0))
        self.w = 100
        self.h = 100
        self.left = 0
        self.press = pygame.event.get


        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1440, 810
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.Quit = QuitMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        #GAME LOOP
        while self.playing:

            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)

            
            #background image
            self.display.blit(self.game_back, (0, 0))

            #unused text
            #self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            
            self.window.blit(self.display, (0,0))


            #GAME PLAY!!

            #sprite drawn
            self.window.blit(self.cat, (self.w,self.h))


            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.w -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.w += 1
                    elif event.key == pygame.K_DOWN:
                        self.h += 1
                    elif event.key == pygame.K_UP:
                        self.h -= 1
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()

            #clock
            self.clock.tick(60)










            
            pygame.display.update()
            self.reset_keys()

            




    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)




