import os

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
print(logo)



if user_input == '1':   
    print(battle_page)
    user_input = input()
    os.system('clear')
    print("""%s id a great choice! Get ready for battle""" % (pokemon)) 
    
elif user_input == '2':
    print(store_page)
    user_input = input()
    os.system('clear')

elif user_input == '3':
    print(medic_page)
    user_input = input('Yes or No: ')
    os.system('clear')
    if user_input == 'Yes' or 'yes':
        print('%s is all healed. Feel free to drop by anytime' % (pokemon))    
    else:
        if user_input == 'No' or 'no':
            print("""%s looks tired. :( Are you sure?.""" % (pokemon))
    