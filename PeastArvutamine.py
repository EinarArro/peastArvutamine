__author__ = 'einar'

import random
import time

manguPikkus = 30
punktideCounter = 0

print("{:*^75}".format(" PEAST ARVUTAMISE MÄNG "))
print("** Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha")
print("** Mäng lõppeb, kui oled kokku kogunud {0} punkti".format(manguPikkus))
print("{:*^75}".format("*"))


def arvutaRaskusaste(param):
    try:
        raskusaste = 0
        if param == 1:
            raskusaste = 10
        elif param == 2:
            raskusaste = 20
        elif param == 3:
            raskusaste = 30
        elif param == 4:
            raskusaste = 40
        else:
            v = input("Sinu sisestatud raskusaste ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
            raise SystemExit
        return raskusaste
    except (AttributeError, TypeError):
        raise AssertionError("Raskusaste peab olema int tüüpi")


def oigeVoiVale(param1, param2):
    global punktideCounter

    try:
        if param1 != param2:
            punktideCounter -= 2
            print("VALE VASTUS")
            print()
        else:
            punktideCounter += 1
            print()
            #print(punktideCounter)
    except (AttributeError, TypeError):
        raise AssertionError("Õige ja vale vastus ei ole õiget tüüpi")


def liitmine():
    liidetav = random.randint(1, raskusaste)
    liitja = random.randint(1, raskusaste)
    try:
        vastus = int(input("{0} + {1} = ".format(liidetav, liitja)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oigeVastus = liidetav + liitja
    oigeVoiVale(oigeVastus, vastus)


def lahutamine():
    lahutatav = random.randint(2, raskusaste)
    lahutaja = random.randint(1, lahutatav)
    try:
        vastus = int(input("{0} - {1} = ".format(lahutatav, lahutaja)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oigeVastus = lahutatav - lahutaja
    oigeVoiVale(oigeVastus, vastus)


def tehteValik(tehe):
    try:
        if tehe == 1:
            liitmine()
        elif tehe == 2:
            lahutamine()
        else:
            v = input("Sinu sisestatud tehtevalik ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
            raise SystemExit
    except (AttributeError, TypeError):
        raise AssertionError("Tehte valik peab olema int tüüpi")


def prindiAeg(start, end):
    print("Aeg: {0:.0f} sekundit".format(end - start))


print()
print("Vali raskusaste:     1: kuni 10     2: kuni 20     3: kuni 30     4: kuni 40")

try:
    raskusaste_in = int(input())
except (ValueError):
    v = input("Sinu sisestatud raskusaste ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
    raise SystemExit

raskusaste = arvutaRaskusaste(raskusaste_in)

print("Vali tehe:     1: liitmine     2: lahutamine     3: liitmine ja lahutamine")

try:
    tehe = int(input())
except (ValueError):
    v = input("Sinu sisestatud tehtevalik ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
    raise SystemExit

start = time.time()

while (punktideCounter < manguPikkus):
    if tehe == 3:
        tehteValik(random.randint(1, 2))
    else:
        tehteValik(tehe)

end = time.time()
diff = end - start
print("Mängu läbimiseks kulus {0:.0f} minutit ja {1:.0f} sekundit".format((diff // 60), (diff % 60)))
a = input("Väljumiseks vajuta Enter")
