import random
from random import randint

#Basic class and subclasses for testing purposes

# class Pokemon:
    

# class Charizard(Pokemon):

def pokemon_selector():
   # Change the class names accordingly
    pokemon_list = {
        #Character name, health, basic attack, seconday attack, special:
        #Possibly add another for coins/loot to give?
        1 : Charizard("Charizard", 100, 50, 140 ,110),
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
    while True:
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
            print(pokemon_checker)
        
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
        return player, opponent
    
pokemon_selector()