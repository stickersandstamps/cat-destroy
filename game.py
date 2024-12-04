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
        self.cat = pygame.Surface((50,50))
        self.cat.fill((255,0,0))
        self.cat = pygame.image.load("cat.png")
        self.x = 100
        self.y = 100
        self.velocity = 10
        self.press = pygame.event.get

        #explosion sound
        mixer.init()
        self.effect = pygame.mixer.Sound("explosion.mp3")


        #target object sprites
        #self.image = pygame.image.load("/path/to/image_file.png")
        self.bug = pygame.Surface((50,50))
        self.bugX, self.bugY = random.randint(0 + 50 , 1440 - 50),random.randint(0 + 50, 810 - 50)

        self.can = pygame.Surface((70,70))
        self.canX, self.canY = random.randint(0 + 70, 1440 - 70),random.randint(0 + 70, 810 - 70)

        self.fish = pygame.Surface((90,90))
        self.fishX, self.fishY = random.randint(0 + 90, 1440 - 90),random.randint(0 + 90, 810 - 90)

        self.car = pygame.Surface((110,110))
        self.carX, self.carY = random.randint(0 + 110, 1440 - 110),random.randint(0 + 110, 810 - 110)

        self.house = pygame.Surface((130,130))
        self.houseX, self.houseY = random.randint(0 + 130, 1440 -130),random.randint(0 + 130, 810 - 130)

        self.moon = pygame.Surface((150,150))
        self.moonX, self.moonY = random.randint(0 + 150, 1440 - 150),random.randint(0 + 150, 810 - 150)

        self.earth = pygame.Surface((170,170))
        self.earthX, self.earthY = random.randint(0 + 170, 1440 - 170),random.randint(0 + 170, 810 - 170)

        self.sun = pygame.Surface((190,190))
        self.sunX, self.sunY = random.randint(0 + 190, 1440 - 190),random.randint(0 + 190, 810 - 190)

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
            if self.level1 == True:
                self.window.blit(self.can, (self.canX, self.canY))




            # if self.cat.get_rect().colliderect(self.can.get_rect()):
            #     self.level2 = True
            # if self.cat.get_rect().colliderect(self.fish.get_rect()):
            #     self.level3 = True
            # if self.cat.get_rect().colliderect(self.car.get_rect()):
            #     self.level4 = True
            # if self.cat.get_rect().colliderect(self.house.get_rect()):
            #     self.level5 = True
            # if self.cat.get_rect().colliderect(self.moon.get_rect()):
            #     self.level6 = True
            # if self.cat.get_rect().colliderect(self.earth.get_rect()):
            #     self.level7 = True
            # if self.cat.get_rect().colliderect(self.sun.get_rect()):
            #     self.level8 = True


            #draw sprites at random locations
            
            # level 1
            # if self.level1 == False:
            #     self.window.blit(self.bug, (self.bugX, self.bugY))
            # elif self.level1 == True:
            #     self.window.blit(self.bug, (2000, 2000))


            # level 2
            # if self.level1 == False:
            #     self.window.blit(self.can, (self.canX, self.canY))
            # else:
            #     self.window.blit(self.can, (2000, 2000))
            # # level 3
            # if self.level1 == False:
            #     self.window.blit(self.fish, (self.fishX, self.fishY))
            # else:
            #     self.window.blit(self.fish, (2000, 2000))
            # # level 4
            # if self.level1 == False:
            #     self.window.blit(self.car, (self.carX, self.carY))
            # else:
            #     self.window.blit(self.car, (2000, 2000))
            # # level 5
            # if self.level1 == False:
            #     self.window.blit(self.house, (self.houseX, self.houseY))
            # else:
            #     self.window.blit(self.house, (2000, 2000))
            # # level 6
            # if self.level1 == False:
            #     self.window.blit(self.moon, (self.moonX, self.moonY))
            # else:
            #     self.window.blit(self.moon, (2000, 2000))
            # # level 7
            # if self.level1 == False:
            #     self.window.blit(self.earth, (self.earthX, self.earthY))
            # else:
            #     self.window.blit(self.earth, (2000, 2000))
            # # level 8
            # if self.level1 == False:
            #     self.window.blit(self.sun, (self.sunX, self.sunY))
            # else:
            #     self.window.blit(self.sun, (2000, 2000))

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
            self.cat_rect = pygame.Rect((self.x, self.y), (50, 50))
            self.bug_rect = pygame.Rect((self.bugX, self.bugY), (50, 50))

            if self.cat_rect.colliderect(self.bug_rect):
                self.effect.play()
                self.bugX = 3000
                self.level1 = True














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




