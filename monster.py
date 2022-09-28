from random import randrange

names = ["a", "b", "c", "d"]

class monster:
    def __init__(self, hp, skade, hit_chance, name = names[randrange(4)]):
        self.name = name
        self.hp = hp
        self.skade = skade
        self.hit_chance = hit_chance
    def angrip(self, motstander):
        if (randrange(100) <= self.hit_chance):
            motstander.hp -= self.skade
            print("Mosteret traff for", self.skade)

_monster = monster(100, 10, 75)