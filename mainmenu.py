import os
class Pokemon:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_sequence(self, other_pokemon):
        # While loop that starts the battle
        if self.health > 0:
            attack = input("Do you want to attack? Yes or No? ")
            #If the user wants to attack do:
            if attack == ('yes','1', 'Yes'):
                time.sleep(2)
                other_pokemon.health - self.attack
                print("%s's health has decreased to %d" % (other_pokemon.name, other_pokemon.health))
            # If the user does not want to attack:
            elif attack == ('2', 'No', 'no'):
                print("Your turn will be skipped, are you sure?")
                skip = input("""1.Yes
                2.No""" )
                if skip == ('1', 'Yes', 'yes'):
                    time.sleep(4)
                    print("""...%s is just sitting around.""" % (self.name))
                else:
                    if skip == '2' or 'No' or 'no':
                        pass
                
            else:
                print("Please enter a valid option.")

    def defend_sequence(self, other_pokemon):
        if self.health > 0:
            defend = input('Do you want to defend?')
            #Begin sequence
            if defend == '1' or 'Yes' or 'yes':
                time.sleep(1.5)
                self.health - other_pokemon.attack/2
                print("""%s defended itself. Damage was reduced to half.""" % (self.name))
            else:
                if defend == ('2', 'No', 'no)':
                    print('Select another option')
    def 



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

main_menu = ("""WELCOME TO POKEMON!! 
1. Battle Arena 
2.Visit Store.
3. Medic """)


battle_page = ("""Welcome to the arena. Please select a Pokemon to begin!
1.Charizard
2.Gyarados
3.Bulbasaur
4.Mewtwo
5.Squirtle """)

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

pokemon = "charchar"

print(logo)
print(main_menu)
user_input = input()
os.system('clear')



if user_input == '1': 
    print(logo)  
    print(battle_page)
    user_input = input()
    os.system('clear')
    print("""%s id a great choice! Get ready for battle""" % (pokemon)) 
    
elif user_input == '2':
    print(logo)
    print(store_page)
    user_input = input()
    os.system('clear')

elif user_input == '3':
    print(logo)
    print(medic_page)
    user_input = input('Yes or No: ')
    os.system('clear')
    if user_input == 'Yes' or 'yes':
        print('%s is all healed. Feel free to drop by anytime' % (pokemon))    
    else:
        if user_input == 'No' or 'no':
            print("""%s looks tired. :( Are you sure?.""" % (pokemon))
else:
    print(logo)
    print('Invalid Input. Choose from the on screen selection.')    