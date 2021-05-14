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

