from random import randrange

names = ["a", "b", "c", "d"]

class monster:
    def __init__(self, hp, dmg, hit_chance, name = names[randrange(5)]):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.hit_chance = hit_chance

_monster = monster(1, 1, 0.1)

def monsterAngrep(self, helt):
    if (randrange(11) < self.hit_chance):
        helt.hp -= self.dmg

