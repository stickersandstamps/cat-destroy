import cowsay
import pygame
from game import Game


def main():

    catSpeak1()
    catSpeak2()
    catSpeak3()

    g = Game()

    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()


def catSpeak1():
    cowsay.kitty('Most of my code is in my files menu.py & game.py! :D')


def catSpeak2():
    cowsay.kitty('I used project.py mainly to just run the game. :P')


def catSpeak3():
    cowsay.kitty(':)')


if __name__ == "__main__":
    main()