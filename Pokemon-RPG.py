import random
import pygame
from random import randint
from pokemon_art import bulbasaur_art, charmander_art, pokeball_art, squirtle_art, logo, pokeball_art, goodbye_message, professor_oak, nurse_joy
import os
import time
import sys
from audio import classic_intro

# POKEMON CLASSES ####################################################################

item_inventory = []

class Pokemon:
    typemultiplier = {'Fire': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Psychic': 0.5}, 'Water': {'Fire': 2.0, 'Water': 0.5, 'Grass': 0.5, 'Psychic': 0.5}, 'Grass': {'Fire': 0.5, 'Water': 2.0, 'Grass': 0.5, 'Psychic': 0.5}, 'Psychic': {'Fire': 2.0, 'Water': 2.0, 'Grass': 2.0, 'Psychic': 0.5}}
    def __init__(self, name, health, attack, type, moves):
        self.name = name
        self.health = health
        self.attack = attack
        self.type = type
        self.moves = moves
        self.bounty = 50
        # self.secondary_attack = secondary_attack
        # self.special_attack = special_attack
    
    def alive(self):
        return self.health > 0

class Charmander(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))

class Squirtle(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))

class Bulbasaur(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))
        

class Gyarados(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))
        
class Mewtwo(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))
    def alive(self): 
        return True

def print_inv(self):
    print(len(item_inventory))

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

# Main Menu #########################################################################
def menu_launch():
    os.system('clear')
    logo()
    starter_pokemon = {
    1: Charmander("Charmander", 100, 35, 'Fire', ['Scratch', 'Ember', 'Dragon Breath']),
    2: Squirtle("Squirtle", 100, 35, 'Water', ['Tacke', 'Water Gun', 'Hydro Pump']),
    3: Bulbasaur("Bulbasaur", 100, 35, 'Grass', ['Vine Whip', 'Razor Leaf', 'Solar Beam']),
    }
    
    user_name = input("What is your name young trainer? ")
    time.sleep(2)
    os.system("clear")
    professor_oak()
    delay_print("\nNice to meet you %s! I'm Professor Oak. I'll be helping you \non your quest to become a pokemon trainer. \n \nLet's get you set up with a pokemon.\n \nChoose wisely, this pokemon will become your best friend and \ntrusted ally." % (user_name))
    print("")
    print("\n===============================================================")
    print("")
    delay_print("                Choose your pokemon:")
    time.sleep(.8)
    print("""
                    1. Charmander
                    2. Squirtle
                    3. Bulbasaur
              """)
    
    user_name = None
    player = None
    running = True
    
    while running:
        pokemon_choice = input("Who do you choose? ")
        if pokemon_choice == "1":
            player = starter_pokemon[1]
            charmander_art()
            running = False
        elif pokemon_choice == "2":
            player = starter_pokemon[2]
            squirtle_art()
            running = False
        elif pokemon_choice == "3":
            player = starter_pokemon[3]
            bulbasaur_art()
            running = False
        else:
            print("Please choose a number 1 - 3.")

    time.sleep(2)
    delay_print(str("What an excellent choice!! Take care of %s for us!" % (player.name)))
    time.sleep(3)
    os.system("clear")
    main(player)

# Main #########################################################################
print(logo)
def main(player):
    os.system("clear")
    logo()
    print("""
                    1. Find wild pokemon
                    2. Visit Nurse Joy
                    3. Visit the Poke Mart
                    4. Quit and Go Home
    
          """)
    time.sleep(1)
    main_input = int(input("What do you and %s want to do? " % (player.name)))
    if main_input == 1:  
        time.sleep(3)
        delay_print("\nA wild pokemon appears!")
        time.sleep(2)
        battle(player)
    elif main_input == 2:
        medic(player)
        # medic(player)
    elif main_input == 3:
        shop(player)
    elif main_input == 4:
        pygame.mixer.music.fadeout(4000)
        time.sleep(1)
        os.system("clear")
        goodbye_message()
        pokeball_art()
        time.sleep(4)
        quit()
    else:
        delay_print("Not a valid input. Please select 1-4")
        time.sleep(1)
        main(player)

# Battle #########################################################################
def battle(player):
    

    charizard = Pokemon("Charizard", 100, 25, 'Fire', ['Dragon Claw', 'Heat Wave', 'Fire Spin'])
    blastoise = Pokemon("Blastoise",100, 30, 'Water', ['Water Pulse', 'Rain Dance', 'Shell Smash'])
    mewtwo = Pokemon('Mewtwo', 200, 50, 'Psychic', ['Confusion', 'Ancient Power', 'Psystrike'])
    squirtle = Pokemon('Squirtle', 100, 20, 'Water', ['Tackle', 'Water Gun', 'Hydro Pump'])
    charmander = Pokemon("Charmander", 100, 35, 'Fire', ['Scratch', 'Ember', 'Dragon Breath'])
    bulbasaur = Pokemon("Bulbasaur", 100, 35, 'Grass', ['Vine Whip', 'Razor Leaf', 'Solar Beam'])


    opponent_list = [charizard, blastoise, squirtle, mewtwo, bulbasaur, charmander]
    opponent = random.choice(opponent_list)
    battle = True
    fullDMG = player.attack * player.typemultiplier[player.type][opponent.type]
    oppDMG = opponent.attack * opponent.typemultiplier[opponent.type][player.type]
 
# Consider types advantages
    # version = ['Fire', 'Water', 'Grass', 'Psychic']
# def type(type1, type2):
    # Both Pokemon are the same type
    if player.type == 'Fire' and opponent.type == 'Fire':
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts not very effective...'
    
    elif player.type == 'Water' and opponent.type == 'Water':
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts not very effective...'

    elif player.type == 'Grass' and opponent.type == 'Grass':
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts not very effective...'

    elif player.type == 'Psychic' and opponent.type == 'Psychic':
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts not very effective...'

    # # Wild Pokemon is STRONG
    if opponent.type == 'Water' and player.type == 'Fire':
    #     opponent.attack *= 2
    #     player.attack /= 2
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts super effective!'
    
    elif opponent.type == 'Grass' and player.type == 'Water':
    #     type2.attack *= 2
    #     type1.attack /= 2
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts super effective!'

    elif opponent.type == 'Fire' and player.type == 'Grass':
    #     type2.attack *= 2
    #     type1.attack /= 2
        string_1_attack = '\nIts not very effective...'
        string_2_attack = '\nIts super effective!'

    elif opponent.type == 'Psychic' and player.type == 'Fire':
        string_1_attack = '\nMewtwo is OP, you should have fled...'
        string_2_attack = '\nMewtwo is King!'

    elif opponent.type == 'Psychic' and player.type == 'Water':
        string_1_attack = '\nMewtwo is OP, you should have fled...'
        string_2_attack = '\nMewtwo is King!'

    elif opponent.type == 'Psychic' and player.type == 'Grass':
        string_1_attack = '\nMewtwo is OP, you should have fled...'
        string_2_attack = '\nMewtwo is King!'
            
    # Wild Pokemon is WEAK
    if opponent.type == 'Fire' and player.type == 'Water':
    #     type1.attack *= 2
    #     type2.attack /= 2
        string_1_attack = '\nIts super effective!'
        string_2_attack = '\nIts not very effective...'

    if opponent.type == 'Water' and player.type == 'Grass':
    #     type1.attack *= 2
    #     type2.attack /= 2
        string_1_attack = '\nIts super effective!'
        string_2_attack = '\nIts not very effective...'

    elif opponent.type == 'Grass' and player.type == 'Fire':
    #     type1.attack *= 2
    #     type2.attack /= 2
        string_1_attack = '\nIts super effective!'
        string_2_attack = '\nIts not very effective...'    

    # # Mewtwo only
    if type == 'Psychic':
    #     type2.attack *= 2
    #     type1.attack /= 2
        string_1_attack = '\nMewtwo is OP, you should have fled.'
        string_2_attack = '\nMewtwo is King!'    

    while battle:
        # delay_print("\nA wild %s appears!" % opponent.name) 
        time.sleep(3)
        print("")
      # Launch into battle sequence here
        os.system('clear')
        logo()
        print("Go %s!" % (player.name))
        print(str("%s health is at %s" % (player.name, player.health)))
        print(str("Enemy %s health is at %s" % (opponent.name, opponent.health)))
        action = input("""\n                  What would you like to do?
                         1.Attack
                         2.Defend
                         3.Use an item
                         4.Flee
                         """)
        time.sleep(1)
        if action == '1' and player.health > 0:
            time.sleep(1)
            delay_print("%s health is %d." % (player.name, player.health))
            delay_print("\n%s health is %d." % (opponent.name, opponent.health))
            #time.sleep(1)
            for i, x in enumerate(player.moves):
                print(f"\n\n{i+1}.", x)
            index = int(input('\nPick a move: '))
            print("%s used %s!" % (player.name, player.moves[index-1]))
            time.sleep(1)
            print(string_1_attack)
            delay_print("\n%s attacked %s for %s damage." % (player.name, opponent.name, fullDMG))
            time.sleep(1)
            print(' ')
            opponent.health -= fullDMG 
            delay_print(str("\nEnemy %s's health has decreased to %d." % (opponent.name, opponent.health)))
            time.sleep(2)
            #Add statement to make value 0 to avoid negative health
            if opponent.health <= 0:
                delay_print("\n%s has fainted!" % opponent.name)
                # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                time.sleep(3)
                main(player)
            else:
                pass
            
            if opponent.alive():
                print("""\n===============================================================\n""")
                delay_print("It's your enemy's turn to attack.")
                # for n in version[opponent.moves]:
                print("\n %s used %s!" % (opponent.name, opponent.moves[index-1]))
                time.sleep(1)
                print(string_2_attack)
                time.sleep(1)
                player.health -= oppDMG
                delay_print("""\n%s's health is now %d""" % (player.name, player.health))
                time.sleep(2)
                if player.health <= 0:
                    delay_print("\n%s has fainted!" % player.name)
                    # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                    time.sleep(3)
                    main(player)
                else:
                    pass

            else:
                delay_print("\nPlease enter a valid option.")
        
        elif action == '2':
            random.randrange(1, 4)
            if random.random() <= 0.5:
                print("%s defended itself and took no damage." % (player.name))
                time.sleep(1)

            else:
                player.health -= oppDMG
                delay_print("%s defended itself, but it failed." % (player.name)) 
                delay_print("%s's health is: %d" % (player.name, player.health))
                if player.health <= 0:
                    delay_print("\n%s has fainted!" % player.name)
                    # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                    time.sleep(3)
                    main(player)
                else:
                    pass
                time.sleep(2)
        
        elif action == '3':
            print("\nInventory of Items:")
            print(*item_inventory, sep = "\n")
            delay_print("\nWhich item would you like to use? ")
            selection = input("")
            lower_selection = selection.lower()
            if lower_selection == "health":
                player.health += 40
                print("%s health has gone up 40!" % player.name)
                print(player.health)
                time.sleep(2)
            
            elif lower_selection == "crit potion":
                crit_chance = random.randrange(1, 10)
                if crit_chance <= 4:
                    opponent.health -= fullDMG + 20
                    time.sleep(2)
                    delay_print("!!!CRITICAL HIT!!!\n")
                    time.sleep(1)
                    delay_print(str("%s health has decreased to %d" % (opponent.name, opponent.health)))
                    
                    if opponent.name == "Mewtwo":
                        if opponent.health <= 40:
                            opponent.health += 100
                            delay_print("Mewtwo steps back and finds his strength!")
                            delay_print("Mewtwo's health is now at %s." % opponent.health)
                        else:
                            pass
                    else:
                        pass

                    if opponent.health <= 0:
                        delay_print("\n%s has fainted!" % opponent.name)
                    # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                        time.sleep(2)
                        main(player)
                    else:
                        pass
            
                    if opponent.health > 0:
                        print("""\n===============================================================\n""")
                        delay_print("It's your enemy's turn to attack.")
                        time.sleep(1)
                        player.health -= oppDMG
                        delay_print("""\n%s's health is now %d""" % (player.name, player.health))
                        time.sleep(2)
                        if player.health <= 0:
                            delay_print("\n%s has fainted!" % player.name)
                            # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                            time.sleep(3)
                            main(player)
                        else: 
                            pass
                else:
                    time.sleep(2)
                    delay_print("Crit Potion seems uneffective.....")
                    time.sleep(1)
                    opponent.health -= fullDMG 
                    delay_print(str("\n%s's health has decreased to %d." % (opponent.name, opponent.health)))
                    time.sleep(2)
                    if opponent.name == "Mewtwo" and opponent.health <= 40:
                        opponent.health += 100
                        delay_print("Mewtwo steps back and finds his strength!")
                        delay_print("Mewtwo's health is now at %s." % opponent.health)
                    else:
                        pass
                    
                    if opponent.health <= 0:
                        delay_print("\n%s has fainted!" % opponent.name)
                     # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                        time.sleep(2)
                        main(player)
                    else:
                        pass
            
                    if opponent.health > 0:
                        print("""\n===============================================================\n""")
                        delay_print("It's your enemy's turn to attack.")
                        time.sleep(1)
                        player.health -= oppDMG
                        delay_print("""\n%s's health is now %d""" % (player.name, player.health))
                        time.sleep(2)
                        if player.health <= 0:
                            delay_print("\n%s has fainted!" % player.name)
                            # print("%s dropped %d coins!" % opponent.name, random.randrange(20, 100))
                            time.sleep(3)
                            main(player)
                        else:
                            pass
                    
            elif lower_selection == "pokeball":
                catch_chance = random.randrange(1, 10)
                if catch_chance <= 3:
                    time.sleep(3)
                    pokeball_art
                    delay_print("!!!POKEBALL WAS SUCCESSFULL!!!")
                    time.sleep(1)
                    delay_print("You caught a %s!" % opponent.name)
                    time.sleep(3)
                    main(player)
                else:
                    time.sleep(2)
                    delay_print("Pokeball seems uneffective.....")
                    time.sleep(1)
                    
            elif lower_selection == "master pokeball":
                catch_chance = random.randrange(1, 10)
                if catch_chance <= 7:
                    time.sleep(3)
                    pokeball_art()
                    delay_print("!!!MASTER POKEBALL WAS SUCCESSFULL!!!\n")
                    time.sleep(1)
                    delay_print("You caught a %s!" % opponent.name)
                    time.sleep(3)
                    main(player)
                else:
                    time.sleep(2)
                    delay_print("Master Pokeball seems uneffective.....")
                    time.sleep(1)
            else:
                print("Item not found.")

        elif action == '4':
            delay_print("You have fled the battle!")
            time.sleep(2)
            main(player)
        
        else:
            delay_print("Please type in a number 1 - 4")

# Medic #########################################################################

def medic(player):
    os.system("clear")
    nurse_joy()
    print("%s's health is at %s/100." % (player.name, player.health))
    print("\nHello, and welcome to the Pokemon Center!\nWe restore your tired Pokemon to full health.\nDo you want to heal %s? \n(yes/no)" % (player.name))

    medic_input = input("")
    lower_medic_input = medic_input.lower()
    medic_running = True
    while medic_running:
        if lower_medic_input == "yes":
            player.health = 100
            time.sleep(2)
            print("%s is at full health." % (player.name))
            medic_running = False
            
        elif lower_medic_input == "no":
            print("%s looks tired. :( Are you sure? " % (player.name))
            second_chance = input("")
            second_chance_lower = second_chance.lower()
            if second_chance_lower == "yes":
                medic_running = False
            elif second_chance_lower == "no":
                player.health = 100
                print("%s is at full health." % (player.name))
                medic_running = False
            
            else:
                print("Please type yes or no.")
                time.sleep(2)
                os.system("clear")
                medic(player)
        else:
            print("Please type yes or no.")
            time.sleep(2)
            os.system("clear")
            medic(player)
            
    time.sleep(2)
    os.system("clear")
    logo()
    main(player)
        
# Shop #########################################################################

def shop(player):
    os.system("clear")
    logo()
    delay_print("\n  Welcome to the Poke Mart! What can we help you with today?")
    print("""\n
               1. Health Potion 
               2. Crit Potion
               3. Pokeball
               4. Master Pokeball
               5. Exit the Poke Mart
          """)
    shop_input = int(input(""))
    if shop_input == 1:
        os.system("clear")
        logo()
        print("""\n Health Potion:
\nThis potion can be used to heal your pokemon by 40 health.
\nWould you like to purchase this item?
Yes or No:
""")
        shop_input = input("")
        lower_shop_input = shop_input.lower()
        if lower_shop_input == "yes":
            item_inventory.append("Health")
            print("\nHealth Potion has been added to your items.")
            time.sleep(2)
        elif lower_shop_input == "no":
            print("Ok! What else would you like to look at?")
            time.sleep(2)
        else:
            print("I do not quite understand. Did you say yes or no?")
        shop(player)
    
    if shop_input == 2:
        os.system("clear")
        logo()
        print("""\n Crit Potion:
\nThis potion gives you a 30% chance to land a critical hit on\nyour next attack.
\nWould you like to purchase this item?
Yes or No:
""")
        shop_input = input("")
        lower_shop_input = shop_input.lower()
        if lower_shop_input == "yes":
            item_inventory.append("Crit Potion")
            print("Crit Potion has been added to your items.")
            time.sleep(2)
        elif lower_shop_input == "no":
            print("Ok! What else would you like to look at?")
            time.sleep(2)
        else:
            print("I do not understand. Did you say yes or no?")    
        shop(player)
    
    if shop_input == 3:
        os.system("clear")
        logo()
        print("""\n Pokeball:
\nPokeballs give you a 20% chance to catch pokemon once they \nare weak enough.
\nWould you like to purchase this item?
Yes or No:
""")
        shop_input = input("")
        lower_shop_input = shop_input.lower()
        if lower_shop_input == "yes":
            item_inventory.append("Pokeball")
            print(" Pokeball has been added to your items.")
            time.sleep(2)
        elif lower_shop_input == "no":
            print("Ok! What else would you like to look at?")
            time.sleep(2)
        else:
            print(input("I do not understand. Did you say yes or no?"))
        shop(player)

    if shop_input == 4:
        os.system("clear")
        logo()
        print("""\n Master Pokeball:
\nMaster Pokeballs give you a 70% chance to catch pokemon once \nthey are weak enough.
\nWould you like to purchase this item?
Yes or No:
""")
        shop_input = input("")
        lower_shop_input = shop_input.lower()
        if lower_shop_input == "yes":
            item_inventory.append("Master_Pokeball")
            print("Master Pokeball has been added to your items.")
            time.sleep(2)
        elif lower_shop_input == "no":
            print("Ok! What else would you like to look at?")
            time.sleep(2)
        else:
            print("I do not understand. Did you say yes or no?")
        shop(player)

    if shop_input == 5:
        os.system("clear")
        logo()
        print("\nThank you for stopping by!")
        time.sleep(2)
        main(player)

menu_launch()