from game import Game
from pygame import mixer

g = Game()

while g.running:
    
    g.curr_menu.display_menu()
    g.game_loop()