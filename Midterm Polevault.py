
# INF360B - Programming in Python
# Josiah Ball
# Midterm 1
#Midterm Pole Vault Game!!!
#I chose making this game because I know there is a lot of complexity involved in this event.
#I thought this might help people understand polevaults complexity and better understad the sport.
#I wanted to incorporate luck but just didn't have enough time to add it in :( so I just left it as a stat for the player.
#I was also wanted to show that height is also a big factor in polevault but didn't have enough time aswell. But anyways i'll explain the 
game...
#the game allows you to select your player. One has better stats then the other. You are competing against yourself. 
#At the start of the game, players are prompted to select one of two characters: Michael or Miguel.
#Each character has unique stats including height, speed, consistency, technique, and luck.
#The player confirms their choice, and the corresponding stats are stored for use in the competition.
#Players must clear various bar heights to progress in the game, but just like the actual event you are able to jump to any height you want.\
#Each bar height has specific speed and technique requirements.
#lowest height available is 6 feet, and the player can choose a higher bar to attempt.
#When the player selects a bar height, the game checks if the player’s speed and technique meet the requirements for that height (just didn't 
have time to add other stat completion).
#If the player meets the requirements, they successfully clear the bar.
#If they do not meet the requirements, they are given two attempts to guess a randomly generated number (1-3) to achieve a "critical step" 
Just like the actual event you get 3 attemps to clear the bar
#I subtracted 1 attempt since they are used their first one saying they missed the height, forcing the player to lock in and guess the right 
number.
#this allows them to clear the height despite not having sufficient stats. There is alot of luck in polevault
#If the player successfully clears a bar, they can choose to attempt a higher jump or end the game.
#If they fail to clear a bar, the game ends, and the player is informed of their failure (just like the actual event you always end in 
failure).
#2nd term fianl make progression available for the character to either go and practice or compete at meets. bothh increase player stats 
(continue on final)
#create dictionary list that allows
 
#for different poles that let you jump higher
 
#for different people that let you have the chance of jumping higher
 
#for different shoes that make you taller
 
#(standards , takeoffs etc...)
import random #random fucntion for assingin random number
import sys #allows exiting game
print('Welcome player!!\n\npress enter to continue') #welcomes user
test_2 = input('> ') #adding space/time instead of throwing all the info at once
players = {'michael':{'height': "5.7", 'speed': "17", 'consistency': '.8', 'technique': "50", 'luck': "11"},
 
'miguel':{'height': "5.10", 'speed': "17", 'consistency': '.8', 'technique': "40", 'luck': "10"}} #data base of players to be called 
later
# stores selected player data in epmty dictionary
player_data = {}
cleared = False #set to false because they haven't cleared any height yet
#prints players dictionary
def menu_look_players(): # make it easer to call for when I do the midterm final
 
print("Players Stats Options:")
 
print("-" * 20) #making it look nicer more like a menu screen
 
for player, value in players.items(): # Loop through players
 
print(player.capitalize() + ": ") #print player name
 
for stat, stat_value in value.items(): #goes through each stat of player
 
print(f" {stat.capitalize():<12}: {stat_value}") #prints stat name and value
 
print("-" * 20)# adding bottem to look nicer
# Call the function to print out the player stats
menu_look_players()
#prompitng a question to be answered
print ('Choose your character: michael or miguel')
#character choice display dictionary stats
def menu_look(): #player stats of the user selected refrenced later
 
print("Player Stats:")
 
print("-" * 20)
 
for stat, value in player_data.items():
 
print(stat.capitalize() + ": " + str(value))
 
print("-" * 20)
while True: #looping so the user can select a character and conformation
 
character_choice = input('> ').lower()
 
if character_choice in players:
 
print(f'You chose {character_choice.capitalize()}. Is that correct? (y/n)')#checking if it was correct input
 
confirmation = input('> ').lower()
 
 
if confirmation == 'y':
 
#store selected player stats in player_data
 
player_data = players[character_choice]
 
print(f"Player {character_choice.capitalize()} selected.")
 
menu_look() # calls player to display stats
 
break
 
 
elif confirmation == 'n':
 
print ('choose again')
 
continue
 

 
else:
 
print("Invalid input. type 'y' or 'n' next time")
 
elif character_choice != players:
 
print("choose 'michael' or 'miguel'")
 
 
else:
 
print("Invalid choice. please choose between 'michael' or 'miguel'.")
 
print('press enter to continue')
time = input('> ')
print(" 
BAR HEIGHT REQUIREMENT")
random_number = random.randint(1,3)
# Requirement of stats to jump each bar height. Able to refrence when pulling certain stats and check if they are less or match users code
bars = {'6ft':{'speed': '6', 'technique': "10"},
 
'6.5ft':{'speed': '6.5', 'technique': "12"},
 
'7ft':{'speed': '7', 'technique': "15"},
 
'7.5ft':{'speed': '7.6', 'technique': "18"},
 
'8ft':{'speed': '8.3', 'technique': "22"},
 
'8.5ft':{'speed': '9', 'technique': "24"},
 
'9ft':{'speed': '9.8', 'technique': "26"},
 
'9.5ft':{'speed': '10.4', 'technique': "28"},
 
'10ft':{'speed': '11', 'technique': "31"},
 
'10.5ft':{'speed': '11.8', 'technique': "33"},
 
'11ft':{'speed': '12', 'technique': "36"},
 
'11.5ft':{'speed': '12.4', 'technique': "38"},
 
'12ft':{'speed': '13', 'technique': "40"},
 
'12.5ft':{'speed': '13.7', 'technique': "42"},
 
'13ft':{'speed': '14', 'technique': "46"},
 
'14ft':{'speed': '15', 'technique': "49"},
 
'14.5ft':{'speed': '16', 'technique': "54"},
 
'15ft':{'speed': '17', 'technique': "60"},
 
'15.5ft':{'speed': '18', 'technique': "67"},
 
'16ft':{'speed': '19', 'technique': "71"}
 
}# bar height
#printing bar stats requirements
for k, v in bars.items():
 
print (k,v)
print("Now choose what height you want to skip to. I would suggest starting at ""[8ft]""\nOpenning height is 6ft (Only Input Numbers, No 
Letters)")
bar_data = {}
#function for height and checks if it meets requirements
def height_option():
 
while True: # Give option for player
 
height_choice = input('-> ') + ('ft')
 
if height_choice in bars:
 
print('Good choice')
 
return height_choice
 
else:
 
print("Choose a height, it can't be greater than (16.5) or a whole number with a decimal ending in '.5'")
height_choice = height_option()
# Speed and height check with attempts
def speed_height(bar):
 
attempts = 2 # Number of attempts given to player with the first already used
 
random_number = random.randint(1, 3)
 
for k, v in bars.items():
 
if k == bar:
 
if float(player_data['speed']) >= float(v['speed']) and float(player_data['technique']) >= float(v['technique']): #float allows 
whole or decimal numbers. But they compare and make sure they are both true
 
print(f"Player can jump over {bar}!") #refrenceing bar 
 
print('Congratulations! You cleared the bar.')
 
return True # making it easier to tell if user cleared the bar
 
else:
 
print(f"Player needs more speed to jump over {bar}.")
 
print('Unfortunately, you did not clear the bar.\nGuess the correct number to clear the height (1-3)')
 
while attempts > 0: #made it like a guess the number so it feels more like a game
 
player_guess = int(input('> '))
 
if player_guess == random_number: #if they are = it will go to this line of code if no it will say input was incorrect and 
subtract 1 from attempts
 
print('Critical step!! Press enter to continue')
input('> ')
print('You got a critical step...')
return True
 
else:
 
attempts -= 1
 
print(f"The correct number was {random_number}. You have {attempts} attempt(s) left.")
 
if attempts > 0:
 
random_number = random.randint(1, 3) # Generates new random number for next guess

 
print(f"Sorry, you used all your attempts and failed to clear {bar}.")
 
return False
# Calling speed_height function and assign its return value to be cleared
cleared = speed_height(height_choice)#if they clear it put cleard as true
# Main game loop for height attempts
while True:
 
if cleared:
 
print(f"{character_choice.capitalize()} cleared the bar at {height_choice}")
 
print("You can try to jump higher if you want, limit 16ft. (y for yes, n for no)")
 
more_jumps = input('> ')
 
if more_jumps == 'n':
 
print('Thanks for playing!')
 
sys.exit()
 
elif more_jumps == 'y':
 
print('Select a new height')
 
height_choice = height_option() # Prompt for a new height choice
 
cleared = speed_height(height_choice) # Try again with the new height
 
else:
 
print('Invalid input.')
 
else:
 
print(f"{character_choice.capitalize()} failed to clear the bar at {height_choice}")
 
print("Unfortunately, you did not clear the height\n(Game Over!!!)")
 
sys.exit()
