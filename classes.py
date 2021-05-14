class Pokemon:
    def __init__(self, name, health, attack, defense, items):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.items = items

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

charizard = Pokemon("Charizard", 100, 50, 25, 0)
squirtle = Pokemon("Squirtle", 100, 50, 25, 0)
bulbasaur = Pokemon("Bulbasaur", 100, 50, 25, 0)
gyarados = Pokemon("Gyrados", 100, 50, 25, 0)
mewtwo = Pokemon("Mewtwo", 100, 50, 25, 0)