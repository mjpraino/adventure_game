# Python Text RPG


import time 
import random

# Definitions
bag = []
scroll = ['FireBlast', 'FrostNova', 'Ignite']
MagicRune = ['Frost Bolt', 'Fire Ball', 'Lightning Bolt']
Dragon = ['Blue Dragon', 'Green Dragon', 'Red Dragon']
Weapon = ['Rusted Sword', 'Long Sword', 'Wand']
Dungeon = []
MagicRune = random.choice(MagicRune)
Dragon = random.choice(Dragon)
scroll = random.choice(scroll)
Weapon = random.choice(Weapon)




##### This will be the intro #####
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            print_pause("You use the " + str(Weapon) +  " against the dragon")
            print_pause("But it is not strong enough "
                        "to defeat the dragon, he uses Fire Breath"
                        " and, luckily you dodge the attack and escape! ")
            dungeon_game()
            break
        elif option2 in response:
            print_pause("Smart Choice! You head back to the main dungeon")
            dungeon_game()
            break
        else:
            print("Sorry, try again")
    return response        

def display_intro():
    print_pause("Welcome to the game, right now you are in the main dungeon.")
    print_pause("In front of you are three passageways")
    print_pause("Choose whether you want to go to the Left Dungeon, \n"
                "the Right Dungeon, or the Middle Dungeon. ")


    
##### 1st Option #####
def left_dungeon():
    print_pause("You walk to the left, there is a door.")
    print_pause("You open the door and find a chest, inside the chest is a scroll.")
    if "scroll" in bag:
        print_pause("You already took the scroll, there is nothing more to do here.")
    else:
        print_pause("You pick up the scroll.")
        bag.append('scroll')
    print_pause("You head back to the main dungeon")
    dungeon_game()
    play_again()
##### 2nd Option #####
def right_dungeon():
    print_pause("You walk to the right dungeon.")
    print_pause("After a few moments, you find yourself "
                "in front of a wizard.")
    if "MagicRune" in bag:
        print_pause("The wizard already gave you the rune.")
        print_pause("You already harness the power of the Magic Rune")
    else:
        print_pause("The wizard walks up to you.")
        if "scroll" in bag:
            print_pause("He looks at your scroll and then gives you the magic rune \n"
                        "you now have increased power from the magical rune.")
            bag.append("MagicRune")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you obtain the scroll.")
    print_pause("You head back to the main dungeon.")
    dungeon_game()
    play_again()
##### 3rd Option #####
def middle_dungeon():
    print_pause("You go to the middle dungeon.")
    print_pause("After a few moments,"
                " you find yourself in front of a " + Dragon + "!")
    print_pause("This is why you need these magical powers.")

    if "MagicRune" in bag:
        print_pause("Luckily the Wizard trained you well, you now obtain "
                    " the power of the " + str(MagicRune) + "!")
        print_pause("You attack the dragon! ")
    if "MagicRune" not in bag:
        print_pause("You do not obtain the necessary magical powers.")
        print_pause("It looks like you need a scroll or more power!.")
        print_pause("You head back to the main dungeon.")   
        dungeon_game()
    ans = ''
    while ans != 'Yes' and ans != 'No':
        ans = input("Do you want to attack the dragon? " " Please say 'yes' or 'no'.\n",
                              "yes", "no")
        if ans == 'Yes':
            dragon_health = 100
            count = 0
            while dragon_health > 0:
                damage_by_player = random.randint(0, 60)
                print_pause(f"You hit the dragon and caused {damage_by_player} damage")
                dragon_health = dragon_health - damage_by_player
                print_pause(f"dragon health is now {dragon_health}")
                count = count + 1

            print_pause(f"You successfully defeated the dragon in {count} attempts, you win!")
            play_again()
        

##### Decisions #####
   
# This is the game
def dungeon_game():
    passage = ''
    if 'started' not in Dungeon:
        display_intro()
        Dungeon.append('started')
        while passage != '1' and passage != '2' and passage != '3':
            passage = input("1. Left\n"
                    "2. Right\n"
                    "3. Middle\n")
            if passage == '1':
                left_dungeon()
            elif passage == '2':
                right_dungeon()
            elif passage == '3':
                middle_dungeon()
                dungeon_game()
    else:
         while passage != '1' and passage != '2' and passage != '3':
            passage = input("1. Left\n"
                    "2. Right\n"
                    "3. Middle\n")
            if passage == '1':
                left_dungeon()
            elif passage == '2':
                right_dungeon()
            elif passage == '3':
                middle_dungeon()
                dungeon_game()
                 
# ask the user to play again
def play_again():
    passage =input("\n ##### Would you like to play again? #####\n "
                   "If YES Enter 1\n "
                   "If NO Enter 2\n ")
    if passage == '1':
        display_intro()
        dungeon_game()
    elif passage == '2':
        print_pause("No worries, see you next time!")
        exit()

dungeon_game()