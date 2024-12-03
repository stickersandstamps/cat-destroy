from game import Game
from pygame import mixer

g = Game()

while g.running:
    #music code
    mixer.init() 
    mixer.music.load("")
    mixer.music.set_volume(0.7) 
    mixer.music.play()

    g.curr_menu.display_menu()
    g.game_loop()