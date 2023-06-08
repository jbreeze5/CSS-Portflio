# Jade Watson
# Jade Watson
# This is the main file that controls the whole game.
# It imports the main character and section files and starts the game by calling the first section.

import main_character
import section_1



print("Hello there!")
print("Welcome to my game Lost in the Jungle")
input()

#1. Start the game
#.2. Quit the game
Choice = int(input("Choose 1 to 'start' and begin or 2 to 'quit' the journey: "))
mode = "begin our jounrney"
elif (Choice == 2):
    mode = ("quit, Goodbye.")
    quit("You choose to quit, Goodbye.")
    print("You choose to", mode)

# Welcome the player
name = input('Enter your name: ')
print( "hello, name, "Lets begin our journey!" )

#And do/say anything else to get your game started
       print("Lets Go!")
            

#Then call your first section.
section_1.start()
       
#Create the player character
print( "Your name is?",main_character.mc.name)
#This code will let your user name the character
 #This is how you'll use the attributes in your main character file in the rest
 # of the sections
  main_character.mc.name = input("what do you want to name your character?")
       print( "welcome " + main_character.mc.name + "!")
       print( "Level 1 is our first jounrney")

 #And do/say anything else to get your game started.
  #For example, inttro narration, setting other player charcter values,
 #   Establishing NPC, etc.

   section_1.start(main_character.mc)    
