from game import Game
from pygame import mixer

g = Game()

while g.running:
    #music code
    mixer.init() 
    mixer.music.load("game_music.mp3")
    mixer.music.set_volume(1) 
    mixer.music.play()

    g.curr_menu.display_menu()
    g.game_loop()