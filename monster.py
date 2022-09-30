from random import randrange

names = ["Troll", "Rotte", "Drage"]

class monster:
    def __init__(self, hp, skade, hit_chance, name = names[randrange(len(names))-1]):
        self.name = name
        self.hp = hp
        self.skade = skade
        self.hit_chance = hit_chance
    def angrip(self, motstander):
        if (randrange(100) <= self.hit_chance):
            motstander.hp -= self.skade
            print(self.name, "traff for", self.skade)
        else:
            print(self.name, "bommet")

_monster = monster(100, 10, 75)