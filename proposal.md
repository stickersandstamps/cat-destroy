# Title
Cat-Destroy

## Repository
<https://github.com/stickersandstamps/cat-destroy.git>

## Description
My final project will be a short game where you play as an all-powerful cat who destroys all the objects it comes into contact with. This is relevant to media and digital arts because video games are a huge part of digital arts, and many people (including myself) are in this course in order to learn more about how to make games.  

## Features
- Main Menu
	- I will create a main menu so the player isn't immediately thrown into the game. It will give the player three choices, play, options, and quit. This will be done using seperate functions for a main menu screen, options screen, and game screen. I will add clickable buttons so the player can chose between the options.
- Player Movement 
	- The player will be in control of a cat sprite which can move around the screen using the WASD keys. I will do this by tracking which keys have been pushed down on, and making the sprite move its x & y positions accordingly. 
- Destruction on Contact
	- When the player's cat sprite comes into contact with an obect in the game, the object will disappear from the screen. This will be done by tracking whether the dimensions of the player sprite intrude upon the dimensions of the target objects.  
- Randomly Spawned Objects
    - When the player's cat spirte destroys all the items on screen, a new set of items will spawn in random positions. This will be done by checking if a player has destroyed all the current items using a bool value of True or False. The random positioning will need to employ Python's random class. 
- Music & Sound Effects
	- A song will be added to the main menu of the game using Pygame's mixer. The song will change to a different one for the main gameplay, and there will be in-game sound effects for the destruction of objects.

## Challenges
- I will need to research how to create an effective main menu that is informative but not overwhelming, and how to properly construct said main menu.
- I will need to research how to make a moveable sprite which moves at an appropriate speed that is not too slow or too fast for maximum player enjoyment. 
- I will need to research how to add sound effects into the game, so that when an object disappears there is a noise. 

## Outcomes
Ideal Outcome:
- The ideal outcome for my project is a game where there is a functioning menu screen with three functioning buttons (play, options, and quit), a playable game where the player moves around a cat sprite and runs into randomly spawned objects to destroy them. These objects will progressively get bigger and bigger, going from items like simple mouse toys to entire planets. 

Minimal Viable Outcome:
- The bare essential outcome for my project is a game where the player can move around as an all-powerful cat, and all the objects that come into contact with said cat disappear from the screen. 

## Milestones

- Week 1
  1. Create Screens
    - Create seperate screens for the menu, game, and options.
  2. Create Main Menu buttons
    - Create play, options, and quit buttons.
    - Allow the player to quit before starting the game by pressing escape or the quit button. 
  3. Add Main Menu Music
    - Use copyright-free music found online.
    - Employ Pygame's mixer to add the music to the main menu screen.
    - Make sure the main menu music only plays during the main menu sequence. 

- Week 2
  1. Create Game Variables
    - Create necessary game variables in order to track movement and spawn in objects. 
  2. Create Movement Mechanics
    - Track which WASD keys are being pressed down on and move the sprite accordingly. 
  3. Add Randomly Spawned Items
    - Find images for items and add code to randomize their placement. Utilize the random class.

- Week 3 (Final)
  1. Add waves of Randomly Spawned Items
    - After one set of items is destroyed, another set should appear immediately after until there are no objects left to destroy. 
  2. Add Game Music & Sound Effects
    - Add the main game's music using the Pygame mixer, and add soundeffects for when an object is destroyed. 
  3. Test Game Mechanics
    - Make sure that the main menu & game are working properly, and that there are no glaring issues. 