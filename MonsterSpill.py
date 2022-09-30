import Vopen as v
import helt as h
import monster as m

print("")
print('Du går inn i en dyp mørk hule. Hulen er fylt med alle mulige skatter og våpen, men innerst i hulen står et monster, et monster som gjør hva som helt for å vokte sin dyrebare skatt.')
print("")
print('Velg et av våpnene dine å angripe monsteret med:')
print("")

def print_hp():
    hp_bar = ""
    for i in range(1,h._spiller.hp):
        hp_bar += "I"
    print("Spiller hp: ", h._spiller.hp, "", hp_bar)
    hp_bar = ""
    for i in range(1,m._monster.hp):
        hp_bar += "I"
    print("Monster hp: ", m._monster.hp, "", hp_bar)

while (h._spiller.hp > 0 and m._monster.hp > 0):
    h._spiller.vleg_vopen(v.alle_vopen)
    h._spiller.angrip(m._monster)
    m._monster.angrip(h._spiller)
    print_hp()
    print("")

if h._spiller.hp <=0:
    print("Du tapte kampen. Monsteret vant")
elif m._monster.hp <=0:
    print("Gratuler du vant!")
elif (h._spiller.hp and m._monster.hp == 0):
    print("Det ble uavgjort, men begge døde")
