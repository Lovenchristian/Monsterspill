from random import randrange

class Spiller:
    def __init__(self, skade, hit_chance, hp=100):
        self.hp=hp
        self.skade=skade
        self.hit_chance=hit_chance

    def vleg_vopen (self, liste):
        for i in range(0, len(liste)):
            print(f"{i+1}     Våpen: {liste[i].navn} har {liste[i].skade} skade og {liste[i].hit_chance}% treff sansynelighet")
        _input = int(input("velg våpen:"))
        self.skade = liste[_input-1].skade
        self.hit_chance = liste[_input-1].hit_chance

    def angrip(self, motstander):
        if (randrange(100) <= self.hit_chance):
            motstander.hp -= self.skade

_spiller = Spiller(0, 0, 100)