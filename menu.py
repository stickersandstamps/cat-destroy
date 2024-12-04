import pygame
from pygame import mixer 

class Menu():
    def __init__(self, game):

        #background menu image
        self.menu_back = pygame.image.load("main_menu_back.png")
        self.game_back = pygame.image.load("game_back.png")


        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2

        self.mid_w -= 300
        self.mid_h += 150


        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):

    #MENU MUSIC
        mixer.init()
        mixer.music.load("main_menu_music.mp3")
        mixer.music.set_volume(0.9)
        mixer.music.play()

        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 80
        self.quitx, self.quity = self.mid_w, self.mid_h + 130
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)

            #background image
            self.game.display.blit(self.menu_back, (0, 0))


            #self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start", 50, self.startx, self.starty)
            self.game.draw_text("Options", 50, self.optionsx, self.optionsy)
            self.game.draw_text("Quit", 50, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.quit
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40 + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:

    
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))

            #options background
            self.game.display.blit(self.game_back, (0, 0))

            self.game.draw_text('Options', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)

            #options
            self.game.draw_text("Press 'M' to mute music.", 50, self.volx, self.voly)
            self.game.draw_text("Press 'U' to unmute music", 50, self.controlsx, self.controlsy)

            self.draw_cursor()
            self.blit_screen()

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_m]:
                # mute audio
                 mixer.music.set_volume(0)

            if keys[pygame.K_u]:
                # activate audio
                mixer.music.set_volume(0.9)
            





    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            pass

class QuitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            pygame.quit() 







