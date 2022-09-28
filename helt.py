"""
import Vopen as t

class Spiller(t.Vopen):
    def __init__(self, skade, hit_chance,hp):
        super().__init_(skade,hit_chance)
        self.hp=hp

_spiller=Spiller(100)

print(spiller.hp)
"""
class Spiller:
    def __init__(self, skade, hit_chance, hp=100):
        self.hp=hp
        self.skade=skade
        self.hit_chance=hit_chance

    def vleg_vopen (liste):
        for i in range(0, liste):
            print(f"Våpen: {liste[i].navn} har {liste[i].skade} skade og {liste[i].hit_chance} treff sansynelighet")

    def angrip ():
        pass

