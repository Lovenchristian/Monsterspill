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

    def vleg_vopen ():
        pass

    def angrip ():
        pass