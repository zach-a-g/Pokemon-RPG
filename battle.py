import time
import sys
import random
# from Pokemon-RPG import player

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)



def battle_page(player, other_pokemon):
    while (self.health > 0) and (other_pokemon.health > 0):
        print("GO %s ! I CHOOSE YOU!" % self.name)
       # print(print status of pokemon)
        print(" ")
       # print(print status of other pokemon)
        print(" ")
        print("Move List goes here")
        index = int(input('Pick a move: '))
        delay_print("%s uses %s!" % self.name, pokemon.attack)
        time.sleep(2)
        other_pokemon.health -= pokemon.power
        print("%s hits for %d damage!" %  pokemon.name, attack.power)
        print("%s now has %s health." % other_pokemon.name, other_pokemon.health)
       # print(print status of pokemon)
        print(" ")
       # print(print status of other pokemon)
        print(" ")
        time.sleep(1)

       # Other pokemon defeated
        if other_pokemon.health <= 0:
            delay_print("%s has fainted!" % other_pokemon.name)
            delay_print("%s dropped %d coins!" % other_pokemon, random.randrange(20, 100))
            break
        else:
            pass
                
       # Other Pokemon's turn to attack you

        delay_print("% is thinking..." % other_pokemon.name)
        delay_print("%s uses %s !" % other_pokemon.name, other_pokemon.attack)
        time.sleep(1)
        pokemon.health -= other_pokemon.attack
        print("%s hit you for %d damage!" % other_pokemon, other_pokemon.power)
        time.sleep(1)

    # Your pokemon defeated or not
        if pokemon.health <= 0:
            delay_print("Your %s has fainted!" % pokemon.name)
            break
        else: 
            print("%s now has %d health." % pokemon.name, pokemon.health)
            break

range = random.randrage(1,5)
