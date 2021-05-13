# class Pokemon:
#     def __init__(self, name, health, attack, defense, items):
#         self.name = name
#         self.health = health
#         self.attack = attack
#         self.defense = defense
#         self.items = items

# Updated class
class Pokemon:
    def __init__(self, name, health, basic_attack, secondary_attack, special):
        self.name = name
        self.healh = health
        self.basic_attack = basic_attack
        self.secondary_attack = secondary_attack
        self.special = special



class Charizard(Pokemon):
    pass

class Squirtle(Pokemon):
    pass

class Bulbasaur(Pokemon):
    pass

class Gyarados(Pokemon):
    pass

class Mewtwo(Pokemon):
    pass

# charizard = Pokemon("Charizard", 100, 50, 25, 0)
# squirtle = Pokemon("Squirtle", 100, 50, 25, 0)
# bulbasaur = Pokemon("Bulbasaur", 100, 50, 25, 0)
# gyarados = Pokemon("Gyrados", 100, 50, 25, 0)
# mewtwo = Pokemon("Mewtwo", 100, 50, 25, 0)



charizard = Pokemon("Charizard", 100, 50, 150, 110)
squirtle = Pokemon("Squirtle", 100, 40, 60, 110)
bulbasaur = Pokemon("Bulbasaur", 100, 45, 55, 120)
gyarados = Pokemon("Gyarados", 100, 40, 90, 140)
mewtwo = Pokemon("Mewtwo", 150, 60, 100, 120)