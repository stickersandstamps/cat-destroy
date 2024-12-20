import pygame
import random
from pygame import mixer 
from menu import *


class Game():
    def __init__(self):

        #background game image
        self.game_back = pygame.image.load("game_back.png")

        #clock variable
        self.clock = pygame.time.Clock()

        #sprite variable
        self.catW = 50
        self.cat = pygame.Surface((self.catW,self.catW))
        self.cat.fill((255,0,0))
        self.cat = pygame.image.load("cat.png")
        self.x = 100
        self.y = 100
        self.velocity = 10
        self.press = pygame.event.get
        
        #explosion sound
        mixer.init()
        self.effect = pygame.mixer.Sound("explosion.mp3")

        #hide variables
        self.can_hide = 5000
        self.fish_hide = 5000
        self.car_hide = 5000
        self.house_hide = 5000
        self.moon_hide = 5000
        self.earth_hide = 5000
        self.sun_hide = 5000

        #target object sprites
        self.bug = pygame.Surface((50,50))
        self.bugX, self.bugY = random.randint(0 + 50 , 1440 - 50),random.randint(0 + 50, 810 - 50)
        self.bug = pygame.image.load("bug.png")

        self.can = pygame.Surface((70,70))
        self.canX, self.canY = random.randint(0 + 70, 1440 - 70),random.randint(0 + 70, 810 - 70)
        self.can = pygame.image.load("can.png")

        self.fish = pygame.Surface((90,90))
        self.fishX, self.fishY = random.randint(0 + 90, 1440 - 90),random.randint(0 + 90, 810 - 90)
        self.fish = pygame.image.load("fish.png")

        self.car = pygame.Surface((110,110))
        self.carX, self.carY = random.randint(0 + 110, 1440 - 110),random.randint(0 + 110, 810 - 110)
        self.car = pygame.image.load("car.png")

        self.house = pygame.Surface((130,130))
        self.houseX, self.houseY = random.randint(0 + 130, 1440 -130),random.randint(0 + 130, 810 - 130)
        self.house = pygame.image.load("house.png")

        self.moon = pygame.Surface((150,150))
        self.moonX, self.moonY = random.randint(0 + 150, 1440 - 150),random.randint(0 + 150, 810 - 150)
        self.moon = pygame.image.load("moon.png")

        self.earth = pygame.Surface((170,170))
        self.earthX, self.earthY = random.randint(0 + 170, 1440 - 170),random.randint(0 + 170, 810 - 170)
        self.earth = pygame.image.load("earth.png")

        self.sun = pygame.Surface((190,190))
        self.sunX, self.sunY = random.randint(0 + 190, 1440 - 190),random.randint(0 + 190, 810 - 190)
        self.sun = pygame.image.load("sun.png")

        #level complete true/false
        self.level1 = False
        self.level2 = False
        self.level3 = False
        self.level4 = False
        self.level5 = False
        self.level6 = False
        self.level7 = False
        self.level8 = False

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
            self.window.blit(self.display, (0,0))

            #sprite drawn
            self.window.blit(self.cat, (self.x,self.y))

            #object sprites drawn
            self.window.blit(self.bug, (self.bugX, self.bugY))
            self.window.blit(self.can, (self.canX + self.can_hide, self.canY))
            self.window.blit(self.fish, (self.fishX + self.fish_hide, self.fishY))
            self.window.blit(self.car, (self.carX + self.car_hide, self.carY))
            self.window.blit(self.house, (self.houseX + self.house_hide, self.houseY))
            self.window.blit(self.moon, (self.moonX + self.moon_hide, self.moonY))
            self.window.blit(self.earth, (self.earthX + self.earth_hide, self.earthY))
            self.window.blit(self.sun, (self.sunX + self.sun_hide, self.sunY))

            if self.level1 == True:
                self.can_hide = 0
            if self.level2 == True:
                self.fish_hide = 0
            if self.level3 == True:
                self.car_hide = 0
            if self.level4 == True:
                self.house_hide = 0
            if self.level5 == True:
                self.moon_hide = 0
            if self.level6 == True:
                self.earth_hide = 0
            if self.level7 == True:
                self.sun_hide = 0

            #clock 
            self.clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            #movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] | keys[pygame.K_a]:
                if self.x > 0:
                    self.x -= self.velocity
            if keys[pygame.K_RIGHT] | keys[pygame.K_d]:
                if self.x < self.DISPLAY_W - 50:
                    self.x += self.velocity
            if keys[pygame.K_UP] | keys[pygame.K_w]:
                if self.y > 0:
                    self.y -= self.velocity
            if keys[pygame.K_DOWN] | keys[pygame.K_s]:
                if self.y < self.DISPLAY_H - 50:
                    self.y += self.velocity
            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            #check if cat hit any of the objects
            self.cat_rect = pygame.Rect((self.x, self.y), (self.catW, self.catW))
            #objects
            self.bug_rect = pygame.Rect((self.bugX, self.bugY), (50, 50))
            self.can_rect = pygame.Rect((self.canX + self.can_hide, self.canY), (70, 70))
            self.fish_rect = pygame.Rect((self.fishX + self.fish_hide, self.fishY), (90, 90))
            self.car_rect = pygame.Rect((self.carX + self.car_hide, self.carY), (110, 110))
            self.house_rect = pygame.Rect((self.houseX + self.house_hide, self.houseY), (130, 130))
            self.moon_rect = pygame.Rect((self.moonX + self.moon_hide, self.moonY), (150, 150))
            self.earth_rect = pygame.Rect((self.earthX + self.earth_hide, self.earthY), (170, 170))
            self.sun_rect = pygame.Rect((self.sunX + self.sun_hide, self.sunY), (190, 190))

            if self.cat_rect.colliderect(self.bug_rect):
                self.effect.play()
                self.bugX = 3000
                self.level1 = True

            if self.cat_rect.colliderect(self.can_rect):
                self.effect.play()
                self.canX = 3000
                self.level2 = True

            if self.cat_rect.colliderect(self.fish_rect):
                self.effect.play()
                self.fishX = 3000
                self.level3 = True

            if self.cat_rect.colliderect(self.car_rect):
                self.effect.play()
                self.carX = 3000
                self.level4 = True

            if self.cat_rect.colliderect(self.house_rect):
                self.effect.play()
                self.houseX = 3000
                self.level5 = True

            if self.cat_rect.colliderect(self.moon_rect):
                self.effect.play()
                self.moonX = 3000
                self.level6 = True

            if self.cat_rect.colliderect(self.earth_rect):
                self.effect.play()
                self.earthX = 3000
                self.level7 = True

            if self.cat_rect.colliderect(self.sun_rect):
                self.effect.play()
                self.sunX = 3000
                self.level8 = True

            if self.level8 == True:
                self.display.blit(self.game_back, (0, 0))
                self.draw_text('Thanks for playing!', 50, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 20)
                self.window.blit(self.display, (0,0))
                
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




