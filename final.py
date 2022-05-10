#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@#Created: April 29. 2022
@Author: Alpha Group: Jamil Ali, Rebecca Holm, Jalen Lloyd, Alanna Murray
@Course: LIS 6050 - Introduction to Computer Programming
@University: Wayne State University
@Assignment: Group Assignment
@Purpose: Choose Your Own Adventure RPG Game
@Python version: 3.9x
@Description: Basic Text Choose Your Own Adventure/RPG game
Idea of the game is for a player to traverse through multiple zones, 
completing puzzles, or having encounters through each zone. 
Objective of the game is to complete as many encounters as you can 
while leaving unscathed. Algorithim utilizies APIs, Dicionaries, Loops, and 
Object Oriented Programming Player is subjective to fail; however, idea of 
the game is to display the multiple different cases which utilize the 
aforementioned functionalities 
"""

#### Import Modules ####

import sys
import os
import random
import time
import requests

#### Global Variables ####
secretWord = ("lumberjack")
medkit = False

#def tarot deck dictionary for 
deck = {}
#variable for fortune teller 
read = ""
#json file for fortune teller
response = requests.get("https://rws-cards-api.herokuapp.com/api/v1/cards/random")
#to call the deck
deck = response.json()

#### Player Setup ####

class player:
    def __init__(self):
        self.name = " "
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "a1"
        self.gameOver = False
        self.job = ""
        self.solves = 0 # helps with puzzle
        
myPlayer = player()

#### Title Screen #####        
def title_screen_options():
	#Allows the player to select the menu options, case-insensitive.
    done = False
    while done == False:
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("quit"):
            print("Thanks for playing!")
            sys.exit()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower != "play" or "help" or "quit":
            try:
                option = int(option)
            except: 
                print("That is not a valid option")
                sys.exit()
        else:
            print("#" * 50)
            print("# Welcome to text-based puzzle RPG for #")
            print("#" * 50)
            print("                 .: Play :.                  ")
            print("                 .: Help :.                  ")
            print("                 .: Quit :.                  ")

    #option = input("> ")
'''if option.lower() == ("play"):
		start_game()
	elif option.lower() == ("quit"):
		sys.exit()
	elif option.lower() == ("help"):
		help_menu()		
	while option.lower() not in ["play", "help", "quit"]:
		print("Invalid command, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			start_game()
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == ("help"):
			help_menu()'''

  
def title_screen():
	#Clears terminal of prior code for title screen
	#os.system("clear")
	#Prints # 50 times.
	print("#" * 50)
	print("# Welcome to text-based puzzle RPG for LIS 6050 #")
	print("#" * 50)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()
    
    
#############
# Help Menu #
#############

# After help menu is displayed, 
# it calls the title screen option function again
def help_menu():
	print("")
	print("#" * 50)
	print("~" * 50)
	print("Use up, down, left, right to move character")
	print("to nagivate through the fantasy world.\n")
	print("Inputs such as 'look' or 'examine' will")
	print("let you interact with puzzles in world.\n")
	print("Puzzles will require various input and ")
	print("possibly answers from outside knowledge.\n")
	print("Type your commands in lowercase to get through the game.\n")
	print("#" * 50)
	print("\n")
	print("#" * 50)
	print("    Please select an option to continue.     ")
	print("#" * 50)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()   

# second help screen
# helps players with traversing through the game if they are stuck
def help_menu2():
    print("")
    print("#" * 50)
    print("~" * 50)
    print("Use up, down, left, right to move character'")
    print("to nagivate through the fantasy world.\n")
    print("Inputs such as 'look' or 'examine' will")
    print("let you interact with puzzles in world.\n")
    print("Puzzles will require various input and ")
    print("possibly answers from outside knowledge.\n")
    print("Type your commands in lowercase to get through the game.\n")
    print("Objective is to complete each zone or solve 5 puzzles.")

 ### constant variables ###
ZONENAME = ""
DESCRIPTION = "description"
INFO = "info"
PUZZLE = "puzzle"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

def entry(): #Adding Health Boost Option
    global health
    global medkit
      
    time.sleep(1)#Time delay to help with reading 
    medkit = random.choice([True,False])
    if medkit == True:
        medkit == True
        print("")#Intro/Instructions for medkit
        print("\nYou go to walk and kick something with your foot.")
        print("\n\nYou found a health potion!\n")
        print("When you are injured you may use it to heal up to 25 hp.")
    print("\nHealth> " + str(myPlayer.hp))#Sends out their current health
    return DeerEncounter()
    
def DeerEncounter():#Starting the Encounter function
    global health #Importing the variables needed
    global medkit
    time.sleep(1)#Creates delay in print so that it is easier to read
    print("")#Intro to Deer
    print("\nYou approach and see a deer with smoke rising from it's head.\n")
    print("At second glance you notice, what you thought was the head \
is actually a skull dripping with black ooze.\n")
    print("Do you wish to proceed?. Y/N")
    combat = input("> ")
    if combat.lower() == "y":
        #Gives player the health before so they can see the drop after the attack
        print("\nHealth> " + str(myPlayer.hp))
        deerAttack = random.choice([True,False])
        #Random function makes the deer's action more guess work than a sure thing
        #And allows for different endings depending on the choice
        if deerAttack == True:#Deer attacks and injures player
            print("A thing pretending to be a deer charged at you \
and attacked you. You are tackled to the ground.")
            #Generates the attack hit points at random
            myPlayer.hp -= random.randint(1,120)
            #calculate the damage to the player and then give them that info
            print("You're new health is " + str(myPlayer.hp))
            print("The Deer gives a huff and walks back into the forest.")
            myPlayer.solves += 1
            print("\nPuzzles solved: " + str(myPlayer.solves))
            if myPlayer.hp <= 0: #Possible death of character
                print("You are dead!")
                print("You're adventure has ended, better luck next time.")
                sys.exit()
        elif deerAttack == False:
            #Deer Does not attack but you get injured by tree
            #Basically the same thing only less damage
            print("The deer lets out ground-shaking roar at you.")
            print("You run in the opposite direction and in your haste \
crashed into a tree.")
            myPlayer.hp -= random.randint(1,25)
            print("You're new health is " + str(myPlayer.hp))
            print("The Deer gives a huff and walks back into the forest.")
            myPlayer.solves += 1
            print("\nPuzzles solved: " + str(myPlayer.solves))
    elif combat.lower() == "n":
        # If they don't want to play it will let them move on
        prompt()   
    while medkit == True: #Healing option 
        action = input("Would you like to use your health potion? Y/N \n> ")
        if action.lower()  == "y":
            medkit = False #Gets rid of their health kit so they won't use it again
            print("You used your health potion")
            health += random.randint(1,25)
            myPlayer.hp = health #Again updating the player with their new health
            print("You're new health is " + str(myPlayer.hp))
            break
        elif action.lower() == "n": 
            #Or if they do not want to use it then they can move on
            break
        
#function for quit
def Quit(userExit):
    if userExit.capitalize() == "Quit":
        print("\nThank you for playing!")
	#player types "quit" or "Quit" and game ends completely.
        sys.exit()
    else:
        return userExit
    
#function for fortune teller    
def fortuneRead():  
    #greeting player by name	
    print("Hello, " + myPlayer.name)
    #calling player's job; option for fortune
    read = input(myPlayer.job + ", Would you like to have your \
fortune told? (Y/N): ")
	#this option reads the json file
    if read.capitalize() == "Y":
	#gives the name of the card in json generated using a randomized api
        print(deck["cards"][0]["name"] + "!")
	#prints the meaning of the card for the player to interpert
        print("Very interesting... it can mean: " + deck["cards"][0]["meaning_up"])
        myPlayer.solves += 1
        print("\nPuzzles solved: " + str(myPlayer.solves))
     #this option let's the player avoid the fortune	
    elif read.capitalize() == "N":
        print("Then you best get on your way.") 
     #allows player to quit	
    elif read.capitalize() == "Quit":
        sys.exit()
    else:
        return read


def intro():
    
    print("\n----- Welcome to the Cave of Wonders!-----")
    print("\nHello player, my name is Socrates...you might've heard of me. \
I want to test your riddle skills.")
    
    time.sleep(3)
    #While loop lets the NPC keep asking the question 
    while True:    
            #asks the user if they want to proceed with the game
            user_choice = input("Do you accept the riddle challenge? Y/N ").upper()
            #Checks answers
            if user_choice == "N":
                print("\n\nWell.... that's too bad, you will try to solve the riddle anyway!")
                return riddle_game() #starts riddle game
            elif user_choice == "Y":
                print("\n\nThank you for humoring me!")
                return riddle_game() #starts riddle game
            else:
                print("\nSocrates does not like that answer....try again")


def riddle_game():

    
    while True:
        
        time.sleep(3)
        
        print("\n\n")
        print("\nI have cities, but no houses. I have mountains, but no trees.\
 I have water, but no fish. What am I?")
        print("\n\nType your guess, or type 'Help1', 'Help2' below: ")
        
        answer = input()
            

        if answer == "Help1".lower(): #input for hint to riddle
            print("\n\nA modern version of this came out 500 years ago.")
        elif answer == "Help2".lower(): #input for hint to riddle
            print("\n\nMakers of this item use fake places to catch forgers.")
        elif answer != "map": #continues loop if answer is not map
            print("Wrong....Try Again!")
            continue
        else:
           checkpuzzle(answer) #checks answer within zonemap
           break


def intro_2():
    print("\n----- You see a stranger lit by candlelight!-----")
    print("\nHello player, my name is Aristotle...you might've heard of me. \
I want to test your riddle skills as well.")
    
    time.sleep(3)
    
    while True:    
            
            user_choice = input("Do you accept the riddle challenge? Y/N ").upper()
    
            if user_choice == "N":
                print("\n\nWell.... that's too bad, you will try \
to solve the riddle anyway!")
                return riddle_game_2() #starts riddle game 2
            elif user_choice == "Y":
                print("\n\nSo you think you are quite an intellect!")
                return riddle_game_2() #starts riddle game 2
            else:
                print("\nAristotle does not like that answer....try again")


def riddle_game_2():
   
    
    while True:
        
        time.sleep(3)
        
        print("\n\n")
        print("\nWhat they couldn't catch, they kept; what they caught, \
they got rid of.")
        print("\n\nType your guess, or type 'Help1', 'Help2' below: ")
        
        answer = input()

            

        if answer == "Help1".lower(): #input for hint to riddle
            print("\nThese are infamous for transmitting the Black Death plaque")
            
        elif answer == "Help2".lower(): #input for hint to riddle
            print("\nThey are tiny vampires!")
            
        elif answer != "fleas": #continues loop if answer is fleas
            print("Wrong....Try Again!")
            continue
        else:
           checkpuzzle(answer) #checks answer within zonemap
           break
		
#function for secret word game
def play():
    #secret word defined/Python Easter Egg/variables for game
    secretWord = ("lumberjack")	
    #Creates a line for the length of the word 
    #which people can then see their correct answers on
    wordCompletion = "_" * len(secretWord)
    guessed = False
    guessedLetters = []
    guessedWord = []
    #Sets how many incorrect guesses they get
    #And how many times the loop goes through
    turns = 10
    #Welcome to game that explains rules and calls player's name
    print("Hello, " + myPlayer.name + ". I am Bevis. It is time to play \
a secret word game!\nYou must guess letters in a secret word in order \
to continue on your journey. There are 10 letters in the word, \
and 10 wrong guesses are allowed.")
    print()
    #wait for 1 second 
    time.sleep(1) 
    print("Start guessing...")
    time.sleep(0.5) 
    #Prints out the lines which will be filled with the guesses
    print(wordCompletion)
    print()
	#loop for guesses begins, setting wrong turns counter at 0
    while not guessed and turns > 0:
        guess = input("Guess a letter or the word: ").lower()
	#Checking to make sure they only put 1 letter 
	#checks if letter is in alphabet
        if len(guess) == 1 and guess.isalpha():
		#statement for a letter already guessed
            if guess in guessedLetters:
                print("You've already guessed that letter.")
		#guessed letter not in word
            elif guess not in secretWord:
                print(guess, "is not in the word.")
                turns -=1 #Counting down the turns and letting the player know
		#sends guess to the list of letters guessed
                guessedLetters.append(guess)
                print("You have ", turns , " turns left.")
		#correct letter guess statement
            else:
                print("Great job, ", guess, "is in the word!")
                guessedLetters.append(guess)
		#Updating the word completion by turning into a list 
                wordList = list(wordCompletion)
		#Looks for the letter in the guess word and replaces it with i
                #by iterating through the indicies with emunerate to seperate the letters
                indices = [i for i, letter in enumerate(secretWord) if letter == guess]
                for index in indices:
                    wordList[index] = guess
		#Sends the guess to to the word completion line 
                #for it to show the player where it is in the word
                #Also converts the wordCompletion back into a string
                wordCompletion = "".join(wordList)
		#If the guess finishes the guess word get out of the loop
                if "_" not in wordCompletion:
                    guessed = True
                sys.exit() 
	#Statement for word guess; checks the word and adds wrong guesses to a list	
        elif len(guess) == len(secretWord) and guess.isalpha():
            if guess in guessedWord:
                print("That word has already been guessed.")
            elif guess != secretWord:
                print(guess, "is not the word.")
		#Only take away turns when they guess wrong
                #and saving it to the guess word list
                turns -= 1
                guessedWord.append(guess)
                print("You have ", turns , " turns left.")
            else:
                guessed = True
                wordCompletion = secretWord
	#if the player enters anything other than a letter from the alphabet	
        else:
            print("Not a valid guess.")
	#print the words on the line provided in wordcompletion as player guess them
        print(wordCompletion)
        print()
    #correct guess statement	
    if guessed:#Win prompt w/easter egg monty python skit
        print("Congratulations! You guessed the secret word!")
        myPlayer.solves += 1
	#Adding player score when completed
        print("You have solved the puzzle. Onwards!")
        print("\nPuzzles solved: " + str(myPlayer.solves))
        speech1 = "\nYou have unlocked the Lumberjack."
        speech2 ="\nYou hear footsteps behind you and see a man in a \
plaid shirt and overalls walks through the forest.\n\nYou hear the end \
of his last phrase as he screams 'We'd sing, SING, SING! I'm a \
lumberjack and I'm okay I sleep all night and I work all day.'\n\nA chorus \
next to him repeats his line joyously.\n\nThey seem fun but you keep moving \
on and as you walk further you see a group of nicely dressed older women \
around a fire that have a well dressed man staked on a spit over a fire. \
They smile and wave to you as you go by.\n"
        #Creates the typewriter effect for the lines of speech
        for character in speech1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        for character in speech2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    #Did not guess correctly
    else:
        print("Sorry, you are out of turns. The word was " + secretWord + ".")
    
def home():
    print("You notice someone at your doorsteps?")  
    helper = input("We need you to follow us into the cave! Can you help? Y/N: ") 
    if helper == 'Y':
        myPlayer.solves += 1
	#Adding player score when completed
        print("You have solved the puzzle. Onwards!")
        print("\nPuzzles solved: " + str(myPlayer.solves))
        
    


#### MAP OF GAME ####
"""
player will navigate through each zone,
eventually reaching the end 
"""
    ###########
   # -----------
   # | | | | |  player goes from zoneA_1 to zoneA_3 
   # -----------
   # | | | | |  zoneB_1 to zoneB_3
   # -----------


# we use this to coincide with the examine function
# once a zone is updated to True,
# user can no longer examine area
solved_places = {"a1":False, "a2":False, "a3":False, 
                 "b1":False, "b2":False, "b3":False, 
                              
                 }
#map zones 
zone_map = {
     "a1":{
         
         ZONENAME:"Home",
         DESCRIPTION:"You find yourself back home... everything seems normal",
         INFO:"info",
         PUZZLE: home,
         SOLVED: "Y",
         UP:"a1",
         DOWN:"b1",
         LEFT:"a1",
         RIGHT: "a2"

         
         
         },
     "a2":{
         
         ZONENAME:"Cave of Wonders",
         DESCRIPTION:"Oh hello... did not see you there, can you solve this?",
         INFO:"You encounter a strange man, and unaware of what he is saying",
         PUZZLE: intro,
         SOLVED: "map",
         UP:"a2",
         DOWN:"b2",
         LEFT:"a1",
         RIGHT: "a3"
     
    },
     "a3":{
         
         ZONENAME:"Deeper in Cave",
         DESCRIPTION:"You move further into the cave",
         INFO: "As you move further in, you notice a man in a hat" ,
         PUZZLE: intro_2,
         SOLVED: "fleas",
         UP:"a3",
         DOWN:"b3",
         LEFT:"a2",
         RIGHT: "b1"
     
    },
     "b1":{
         
         ZONENAME:"Forest",
         DESCRIPTION:"You reach the end of the cave and enter a dense forest \
notice a dark figure approaching.",
         INFO:"info",
         PUZZLE: entry,
         SOLVED: False,
         UP:"a1",
         DOWN:"b1",
         LEFT:"a3",
         RIGHT: "b2"
     
    },
     "b2":{
         
         ZONENAME:"Further in the forest...",
         DESCRIPTION: "You come upon a woman at a crossroads. She looks like \
she is waiting for someone.",
         INFO:"info",
         PUZZLE:fortuneRead,
         SOLVED: False,
         UP:"a2",
         DOWN:"b2",
         LEFT:"b1",
         RIGHT: "b3"
     
    },
     "b3":{
         
         ZONENAME:"A clearing...",
         DESCRIPTION:"You come out of the forest...",
         INFO:"info",
         PUZZLE:play,
         SOLVED: False,
         UP:"a3",
         DOWN:"down",
         LEFT:"b2",
         RIGHT: "a1"
     
    },
}



### GAME INTERACTIVITY ###


# prints location
def print_location():
    if len(zone_map[myPlayer.location][ZONENAME]) <= 10:
    	# Shows User where they exactly are at the moment
        print("\n" + ("#" * (7 +len(myPlayer.location))))
        print("# " + (zone_map[myPlayer.location][ZONENAME]) + " #")
        print("#" * (7 +len(myPlayer.location)))
        print("\n" + (zone_map[myPlayer.location][DESCRIPTION]))
    else:
        print("\n" + ("#" * (15 +len(myPlayer.location))))
        print("# " + (zone_map[myPlayer.location][ZONENAME]) + " #")
        print("#" * (15 +len(myPlayer.location)))
        print("\n" + (zone_map[myPlayer.location][DESCRIPTION]))
        

# prompts user to how they should traverse through zones
def prompt():
    
    # Asks User what they want to do
    print("\nAcceptable Actions: " + "[move, go, travel, walk, quit, " +
          "inspect, examine, look, search, help]")
    print("\nWhat would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "inspect", \
                          "examine", "look", "search","help"]
        #Forces the player to write an acceptable sign
        #as this is essential to solving a puzzle later.
    while action.lower() not in acceptable_actions:
    	print("Unknown action command, please try again.\n" +
           str(acceptable_actions) + "\nWhat would you like to do?")
    	action = input("> ")
    if action.lower() == "quit":
    	sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        move(action.lower()) # calls function move
    elif action.lower() in ["inspect", "examine", "look", "search"]:
    	examine() # calls function examine
    elif action.lower() == "help":
        help_menu2()
    

### asks user where they would like to move###
### if user acceptable action, their place in the zone 
### becomes updated. ###
### Movement handler updates players location  

### If user says they want to move north, we call
### function movement handler, and it updates the movement

### We start at myPlayer.location = a1, and if we choose to move right,
### we will move to zone a2, and our myPlayer.location wll be updated.

def move(playerMove):
    
    print("Acceptable Actions: " + "[left, right, up, down]")
    ask = "Where would you like to " + playerMove + " to \n"
    destination = input(ask)
    if destination in ["up","north", "UP","Up","North","NORTH"]:
        move_dest = zone_map[myPlayer.location][UP]
        movement_handler(move_dest) # calls function movement handler
    elif destination in ["down", "south","DOWN","Down","SOUTH","South"]:
        move_dest = zone_map[myPlayer.location][DOWN]
        movement_handler(move_dest)
    
    elif destination in ["right","east","Right","East","EAST","RIGHT"]:
        move_dest = zone_map[myPlayer.location][RIGHT]
        movement_handler(move_dest)
    
    elif destination in ["left","west","LEFT","WEST","West","Left"]:
        move_dest = zone_map[myPlayer.location][LEFT]
        movement_handler(move_dest)
    else:
        move(playerMove)



# takes the class attribute of location, and updates
# the location of user depending on where they decided to
# go from the move function
def movement_handler(move_dest):
    print("\n" + "You have moved to zone " + move_dest + ".")
    myPlayer.location = move_dest # updates location
    print_location()
    

# examine function enables for different outputs to happen
# depending on the location of which the user is in
# if the user has already completed a zone/ solved a puzzle
# the solved_places dictionary is updated and the
# user is no longer prompted the same scene
def examine():
    #from Riddle import intro
    if solved_places[myPlayer.location] == True:
        print("There is nothing new to see here")
    elif myPlayer.location == "a1":
        home()
    elif myPlayer.location == "a2":
        intro()
    elif myPlayer.location == "a3":
        intro_2()
    elif myPlayer.location == "b1":
        entry()
    elif myPlayer.location == "b2":
        fortuneRead()
    elif myPlayer.location == "b3":
        play()
    else:
        print("\n" + (zone_map[myPlayer.location][INFO]))
        print((zone_map[myPlayer.location][PUZZLE]))
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)


# function checks to see if user's answer
# matches the answer in the SOLVED value in the DICTIONARY
def checkpuzzle(puzzle_answer):
    if myPlayer.solves >= 5:
        print("Congratulations")
        sys.exit()
    else:
        if puzzle_answer == (zone_map[myPlayer.location][SOLVED]):
            solved_places[myPlayer.location] = True
            myPlayer.solves += 1
            print("You have solved the puzzle. Onwards!")
            print("\nPuzzles solved: " + str(myPlayer.solves))
        else:
            print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            examine()
    
    
# start of main game loop, ends when user solves 5 puzzles
def main_game_loop():
    while myPlayer.solves != 5:
        prompt()
        if myPlayer.solves == 5:
            print("You have won the game!")
            os.system("cls")
            sys.exit()



### STARTING GAME ###
################
def start_game():
	#Clears the terminal for the game to start.
    os.system("cls")

	#QUESTION NAME: Obtains the player's name.
    question1 = "\nHello there, what is your name?\n"
    for character in question1:
        #this allows a type writer effect, nice and slow texts form and show
        # gives video game effect 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name = input("> ")
    myPlayer.name = player_name.capitalize()

    question4 = "\nHow old are you?\n"
    for character in question4:
        #this allows a type writer effect, nice and slow texts form and show
        # gives video game effect 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_age = input("> ")
    try:
        player_age == int(player_age)
    except:
        print("That is not a valid age. Please try again.")
        sys.exit()

	#QUESTION ROLE: Obtains Player's Role

    
    question2 = "My dear friend " + myPlayer.name + ", choose your role.\n"
    question3 = "(You can play as a Mage, Priest, Warrior, Prisoner)\n"
    
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ["mage","priest","warrior","prisoner"]
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job.lower()
        print("You are now a " + " " + myPlayer.job)
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job.lower()
            print("You are now a" + " " + myPlayer.job)
     
    ### Player Stats ###
    if myPlayer.job == "warrior":
        myPlayer.hp = 120
        myPlayer.mp = 30
    elif myPlayer.job == "prisoner":
        myPlayer.hp = 110
        myPlayer.mp = 40
    elif myPlayer.job == "priest":
        myPlayer.hp = 75
        myPlayer.mp = 75
    else:
        myPlayer.hp = 100
        myPlayer.mp = 50
    
    
    ###INTRODUCTION###
	#Leads the player into the game 
    speech1 = "Ah, " + myPlayer.job + ", how interesting. Well then.\n" 
    speech2 = "It is a beautiful day outside. You just turned " + player_age \
+". The sun is shining and you decide to take a walk in \
the park, " + myPlayer.name + ".\n"   
    speech3 = "You take a path into a garden that you have never \
seen before. It is lush with greenery and flowers and in the very center \
there is an ornately carved fountain. It’s beautiful, and you decide to take \
a closer look. You've never seen anything like it, and your gaze follows the \
water has it cascades into a pool...\n\n"  
    speech4 = "Looking into the pool you are astonished to see a face looking \
back at you. It is not clear, but it is distinctly not yours.\n\n"
    speech5 = "You lean in closer. Hands reach out, grabbing your shoulders \
and pulling you into the fountain.\n\n"
    speech6 = "You black out. When you awaken you are sitting beside the \
fountain, your clothes aren't wet, and the sky is stormy. You look down and \
see that you are dressed as a " + myPlayer.job + " and the... \n\nGame... \
\n\nOffically... \n\nBegins...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
        

    os.system("cls")
    main_game_loop()


title_screen()
