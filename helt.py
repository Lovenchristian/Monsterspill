"""
import Vopen as t

class Spiller(t.Vopen):
    def __init__(self, skade, hit_chance,hp):
        super().__init_(skade,hit_chance)
        self.hp=hp

spiller=Spiller(100)

print(spiller.hp)
"""
class Spiller:
    def __init__(self, hp):
        self.hp=hp

spiller=Spiller(100)