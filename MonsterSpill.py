import Vopen as v
import helt as h
import monster as m

print(h._spiller.hp)
print(m._monster.hp)

def print_hp():
    print("Spiller hp: ", h._spiller.hp)
    print("Monster hp: ", m._monster.hp)

while (h._spiller.hp > 0 and m._monster.hp > 0):
    h._spiller.vleg_vopen(v.alle_vopen)
    h._spiller.angrip(m._monster)
    m._monster.(h._spiller)
    print_hp()