import os
import time
import random

logo = ("""
================================================
  _____   ____  _  ________ __  __  ____  _   _ 
 |  __ \ / __ \| |/ /  ____|  \/  |/ __ \| \ | |
 | |__) | |  | | ' /| |__  | \  / | |  | |  \| |
 |  ___/| |  | |  < |  __| | |\/| | |  | | . ` |
 | |    | |__| | . \| |____| |  | | |__| | |\  |
 |_|     \____/|_|\_\______|_|  |_|\____/|_| \_|
================================================
""")

def battle_menu():
    print("""WELCOME TO POKEMON!! 
1. Battle Arena 
2. Visit Store.
3. Medic """)


battle_page = ("""Welcome to the arena. Please select a Pokemon to begin!
1.Charizard
2.Blastoise
3.Mewtwo
4.Squirtle """)

store_page = ("""Welcome to the store. Feel free to look around. :)
1.Crit Potions - increases chance to double damage
2.Pokeball - gives 20 percent chance to catch pokemon
3.Master Pokeball - gives 40% to catch
4.Health Potion - heals 30 HP
5.Leave
""")

medic_page = ("""Welcome to the infirmary.
Here we nurse your pokemon back to full health.
Would you like to use our services today? """)

class Pokemon:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_sequence(self, other_pokemon):
        if self.health > 0:
            print("%s attacked %s." % (poke_choice.name, other_pokemon.name))
            print(' ')
            other_pokemon.health -= poke_choice.attack 
            print("%s's health has decreased to %d." % (other_pokemon.name, other_pokemon.health))
        # While loop that starts the battle
        # if self.health > 0:
        #     attack = input("Do you want to attack? Yes or No? ")
        #     #If the user wants to attack do:
        #     if attack == ('yes','1', 'Yes'):
        #         time.sleep(2)
        #         other_pokemon.health -= self.attack
        #         print("%s's health has decreased to %d" % (other_pokemon.name, other_pokemon.health))
        #     # If the user does not want to attack:
        #     elif attack == ('2', 'No', 'no'):
        #         print("Your turn will be skipped, are you sure?")
        #         skip = input("""1.Yes
        #         2.No""" )
        #         if skip == ('1', 'Yes', 'yes'):
        #             time.sleep(4)
        #             print("""...%s is just sitting around.""" % (self.name))
        #         else:
        #             if skip == '2' or 'No' or 'no':
        #                 print('null')
                
        else:
            print("Please enter a valid option.")

    def defend_sequence(self, other_pokemon):
        if self.health > 0:
            defend = input('Do you want to defend?')
            #Begin sequence
            if defend == '1' or 'Yes' or 'yes':
                self.health - other_pokemon.attack/2
                print("""%s defended itself. Damage was reduced to half.""" % (self.name))
            else:
                if defend == ('2', 'No', 'no'):
                    print('Select another option')


charizard = Pokemon("Charizard", 100, 20, 25)
blastoise = Pokemon("Blastoise",100, 20, 25)
mewtwo = Pokemon('Mewtwo', 100, 25, 25)
squirtle = Pokemon('Squirtle', 100, 25, 25)

characters = [" ", charizard, blastoise, mewtwo, squirtle]

opps = [charizard, blastoise, mewtwo, squirtle]
poke = charizard

#active = True
#while active == True:
def start_battle():
    print(logo)
    battle_menu()
    user_input = input()
    os.system('clear')



    if user_input == '1':
        running =True 
        print(logo)  
        print(battle_page)
        poke_choice = characters[int(input())]
        os.system('clear')
        print(logo)
        print("""%s is a great choice! Get ready for battle""" % (poke_choice.name))
        time.sleep(1)
        os.system('clear')
        print(logo)
        print("""Welcome trainer. Here in the arena, the bond between
        you and %s will be put to the test. Lets go!""" % (poke_choice.name))
        time.sleep(2)
        opponent = random.choice(opps)
        print("Your opponent is %s." % (opponent.name))
        print(" ")
        while running == True:
            os.system('clear')
            print(logo)
            action = input("""What would you like to do?
            1.Attack
            2.Defend
            3.Use an item
            4.Flee
            """)
            if action == '1' and poke_choice.health > 0:
                time.sleep(1)
                print("%s attacked %s." % (poke_choice.name, opponent.name))
                time.sleep(2)
                print(' ')
                opponent.health -= poke_choice.attack 
                print("%s's health has decreased to %d." % (opponent.name, opponent.health))
                time.sleep(2)
            if opponent.health > 0:
                print("""============================================================""")
                print("It's your enemy's turn to attack.")
                time.sleep(1)
                poke_choice.health -= opponent.attack
                print("""%s's health is now %d""" % (poke_choice.name, poke_choice.health))
                time.sleep(1)
            
            else:
                print("Please enter a valid option.")