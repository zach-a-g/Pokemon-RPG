#test classes:

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
        elif pokemon_choice == 2:
            player = starter_pokemon[2]
        elif pokemon_choice == 3:
            player = starter_pokemon[3]
    
        else:
            print("Please choose a number 1 - 3.")
    
        print(player.name)
        
        print("What an excellent choice!! Take care of %s for us!" % (player.name))
        #Tests the selection above - delete later
        print(player.__dict__)
        running = False
        main(player)


def main(player):
    print("What do you and %s want to do? " % (player.name))
    shop(player)

def shop(player):
    print("This is a test %s" % (player.name))

# def attack_sequence(self, player):
#         # While loop that starts the battle
#         if player.health > 0:
#             attack = input("Do you want to attack? Yes or No? ")
#             #If the user wants to attack do:
#             if attack == ('yes','1', 'Yes'):
#                 time.sleep(2)
#                 other_pokemon.health - self.attack
#                 print("%s's health has decreased to %d" % (other_pokemon.name, other_pokemon.health))
#             # If the user does not want to attack:
#             elif attack == ('2', 'No', 'no'):
#                 print("Your turn will be skipped, are you sure?")
#                 skip = input("""1.Yes
#                 2.No""" )
#                 if skip == ('1', 'Yes', 'yes'):
#                     time.sleep(4)
#                     print("""...%s is just sitting around.""" % (self.name))
#                 else:
#                     if skip == '2' or 'No' or 'no':
#                         pass
                
#             else:
#                 print("Please enter a valid option.")

#     def defend_sequence(self, other_pokemon):
#         if self.health > 0:
#             defend = input('Do you want to defend?')
#             #Begin sequence
#             if defend == '1' or 'Yes' or 'yes':
#                 time.sleep(1.5)
#                 self.health - other_pokemon.attack/2
#                 print("""%s defended itself. Damage was reduced to half.""" % (self.name))
#             else:
#                 if defend == ('2', 'No', 'no)':
#                     print('Select another option')


menu_launch()
