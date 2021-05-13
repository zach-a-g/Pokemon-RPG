
import random


# POKE MART ITEMS CLASSES
class Item():
    def __init__ (self):
        self.name = "Item"
        self.price = "price"

    def use_item(self):
        attack_function = "item + attack_power"
        # still thinking on how to make this work
class Crit_Potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Critical Chance Potion"
        self.crit_chance = 0.4
        # something like if random is true, attack+40% of attack is damage dealt
        self.price = 20
class Pokeball(Item):
    def __init__(self):
        super().__init__()
        self.name = "Pokeball"
        self.catch_chance = 0.15
        # we already have a catch chance once under certain HP, so how would we add this on?
        # maybe just start this higher with no "under HP" to just see if it works
        self.price = 25
class Master_Pokeball(Item):
    def __init__(self):
        super().__init__()
        self.name = "Master Pokeball"
        self.catch_chance = 0.5
        self.price = 75
class Health(Item):
    def __init__(self):
        super().__init__()
        self.name = "Health Potion"
        self.healing = 60
        self.price = 40

# POKEMON CLASSES

class Pokemon:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.potions = 3

    def attack_opponent(self, other_pokemon):
        # While loop that starts the battle
        print("A WILD %s APPEARS!" % other_pokemon)
        while self.health > 0 or other_pokemon.health == 0:
            desire_to_attack = input("Choose your attack: List of Commands")
            lower_desire_to_attack = desire_to_attack.lower()
            #If the user wants to attack do:
            if lower_desire_to_attack == "yes":
                other_pokemon.health = other_pokemon.health - (self.attack * 0.1)
                self.attack -= 5
                self.health = self.health - (other_pokemon.attack * 0.1)
                print("%s's health has decreased to %d" % (other_pokemon.name, other_pokemon.health))
                print("-----------")
                print("%s's attack has decreased to %d" % (self.name, self.attack))
                print("%s attacked your pokemon. Your health fell to: %d" % (other_pokemon.name, self.health))
            # If the user does not want to attack:
            elif lower_desire_to_attack == "no":
                print("""
                1. Flee
                2. Take Potion
                    """)
                flee_or_potion = int(input("What do you want to do? Type 1 or 2." ))
                # Option for taking potions
                if flee_or_potion == 2:
                    if self.potions > 0:
                        self.health += 20
                        self.potions -= 1
                        print("Your pokemon's health is now at %d. You have %d potions left" % (self.health, self.potions))
                    else:
                        print("You don't have any more potions.")
                 # Option for fleeing the battle   
                else:
                    print("You have fled the battle.")
                    self.health = 0
            else:
                print("Please enter a valid option.")
                 
    
    def list_stats(self):
        print("""%s's stats:
              Health: %d
              Attack: %d
              Defense: %d
              """ % (self.name, self.health, self.attack, self.defense))
        
running = True

charizard = Pokemon("Charizard", 100, 120, 80)
blastoise = Pokemon("Blastoise",100, 100, 110)

charizard.attack_opponent(blastoise)



# print("Welcome to Pokemon!")

# while running:
#     print("""
#           1. View Pokemon's stats
#           2. Fight another pokemon 
#           3. Exit
#           """)
#     user_input = int(input("What would you like to do? Select a number 1-3"))