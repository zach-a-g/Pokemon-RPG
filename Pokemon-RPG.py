
import random
#from Items import Item, Crit_Potion, Pokeball, Master_Pokeball, Health
from random import randint
from pokemon_art import bulbasaur_art, charmander_art, squirtle_art

# POKEMON CLASSES

#Basic class and subclasses for testing purposes

class Pokemon:
    def __init__(self, name, health, basic_attack, secondary_attack, special_attack):
        self.name = name
        self.health = health
        self.bounty = 0
        self.potions = 1
        self.basic_attack = basic_attack
        self.secondary_attack = secondary_attack
        self.special_attack = special_attack
        

class Charizard(Pokemon):
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


class Pokemon:
    def __init__(self, name, health, basic_attack, secondary_attack, special_attack):
        self.name = name
        self.health = health
        self.bounty = 0
        self.potions = 1
        self.basic_attack = basic_attack
        self.secondary_attack = secondary_attack
        self.special_attack = special_attack
        

class Charmander(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))


class Squirtle(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))

class Bulbasaur(Pokemon):
    def print_status(self):
        print("%s has %d health and %d power" % (self.name, self.health, self.power))



def menu_launch():
    print("""
================================================
  _____   ____  _  ________ __  __  ____  _   _ 
 |  __ \ / __ \| |/ /  ____|  \/  |/ __ \| \ | |
 | |__) | |  | | ' /| |__  | \  / | |  | |  \| |
 |  ___/| |  | |  < |  __| | |\/| | |  | | . ` |
 | |    | |__| | . \| |____| |  | | |__| | |\  |
 |_|     \____/|_|\_\______|_|  |_|\____/|_| \_|
================================================
""")
    
    starter_pokemon = {
    1: Charmander("Charmander", 100, 50, 45, 110),
    2: Squirtle("Squirtle", 100, 40, 60, 110),
    3: Bulbasaur("Bulbasaur", 100, 45, 55, 120),
    }
    
    user_name = input("What is your name young trainer? ")
    print("Nice to meet you %s. I'm Professor Oak. I'll be helping you on your quest to become a pokemon trainer. Let's get you set up with a pokemon. Choose wisely, this pokemon will become your best friend and trusted ally." % (user_name))
    print("")
    print("====================================================================================")
    print("")
    print("Choose your pokemon:")
    print("""
    1. Charmander
    2. Squirtle
    3. Bulbasaur
              """)
    # user_input = int(input(""))
    # print(user_input)
    
    player = None
    running = True
    while running:
        pokemon_choice = int(input("Who do you choose? "))
        if pokemon_choice == 1:
            player = starter_pokemon[1]
            charmander_art()
        elif pokemon_choice == 2:
            player = starter_pokemon[2]
            squirtle_art()
        elif pokemon_choice == 3:
            player = starter_pokemon[3]
            bulbasaur_art()
    
        else:
            print("Please choose a number 1 - 3.")
    
        print("What an excellent choice!! Take care of %s for us!" % (player.name))
        #Tests the selection above - delete later
        #print(player.__dict__)
        running = False
        main(player)



def main(player):
    print("""
          1. Find wild pokemon
          2. Tournament
          3. Visit the Store
    
          """)
    main_input = int(input("What do you and %s want to do? " % (player.name)))
    if main_input == 1:  
        battle(player)
    elif main_input == 3:
        shop(player)
    else:
        print("test")


def battle(player):

    battle = True
    opponent_list = {
        1: Gyarados("Gyarados", 100, 50, 45, 110),
        2: Mewtwo("Mewtwo", 200, 70, 80, 200 ),
    }
    while battle:
        random_number = randint(1, 2)
        opponent = opponent_list[random_number]
        print("A wild %s appears!" % (opponent.name)) 
        print(player.name)
        #Launch into battle sequence here
        battle = False
    

def shop(player):
    print("Welcome to the shop! What can we help you with today?")
    print("""
          1. Purchase Potions 
          2. Purchase attack items
          3. Purchase Pokeballs
          """)
    shop_input = int(input(""))
    if shop_input == 1:
        player.bounty -= 50
        player.potions += 1
        print("Thanks for your purchase!")
    elif shop_input == 2:
        player.bounty -= 25
        player.basic_ttacks += 25
        print("Thanks for your purchase!")
    else:
        print("Thanks for stopping by!")
    main(player)


menu_launch()



