import random
from random import randint

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


def pokemon_selector():
   # Change the class names accordingly
    pokemon_list = {
        #Character name, health, basic attack, seconday attack, special:
        #Possibly add another for coins/loot to give?
        1 : Charizard("Charizard", 100, 50, 140, 110),
        2: Squirtle("Squirtle", 100, 40, 60, 110),
        3: Bulbasaur("Bulbasaur", 100, 45, 55, 120),
        4: Gyarados("Gyarados", 100, 40, 90, 140),
        5: Mewtwo("Mewtwo", 150, 60, 100, 120),
    }
    
    #Edit this later to include more exciting text
    print("""
          Choose your pokemon!
          1. Charizard
          2. Squirtle
          3. Bulbasaur
          4. Gyarados
          5. Mewtwo
          """)
    #Future: add the images of the pokemon you select here. 
    opponent = None
    running = True
    while running:
        pokemon_choice = int(input("Who do you choose? "))
        if pokemon_choice == 1:
            player = pokemon_list[1]
        elif pokemon_choice == 2:
            player = pokemon_list[2]
        elif pokemon_choice == 3:
            player = pokemon_list[3]
        elif pokemon_choice == 4:
            player = pokemon_list[4]
        elif pokemon_choice == 5:
            player = pokemon_list[5]
        else:
            print("Please choose a number 1 - 5.")

        for pokemon in pokemon_list:
            pokemon_checker = pokemon_list[pokemon].name
            #Checks to make sure the selector is working correctly
        
        while opponent is None:
            if player.name != pokemon_checker:
                #Assigns random opponent from pokemon dictionary.
                random_number = randint(1, 5)
                #Takes the random number above and uses it to assign opponent the corresponding key from the dictionary
                opponent = pokemon_list[random_number]
                #Test that it's working correctly
                print("**********")
                print(opponent.name)
                
        #Future: print the opponent's image here(?)
                
        print("A wild %s has appeared!" % (opponent.name))
        #Checks player selection:
        #print(player.__dict__)
        #
        print("""%s is ready! Your pokemon's stats are:
              
              Health: %d
              Basic attack: %d
              Seconday Attack: %d
              Special Attack: %d
              
              """
              % (player.name, player.health, player.basic_attack, player.secondary_attack, player.special_attack))
        running = False
        main(player, opponent)
        #return player, opponent

#pokemon_selector()


def main(player, opponent):
    testing = True
    while testing:
        print("What do you want to do? ")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = int(input(""))
        if user_input == 1:
            print (player.name)
            print (opponent.name)
            testing = False
        else:
            testing = False
    testing = False


pokemon_selector()
            
