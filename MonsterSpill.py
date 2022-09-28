import Vopen as v
import helt as h
import monster as m

print(h.Sverd.skade)

while (h._spiller.hp <= 0 or m._monster.hp <= 0):
    #velg våpen
    h._spiller.velgVopen()