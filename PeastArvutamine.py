__author__ = 'einar'

import random

manguPikkus = 30
punktideCounter = 0

print("{:*^75}".format(" PEAST ARVUTAMISE MÄNG "))
print("** Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha")
print("** Mäng lõppeb, kui oled kokku kogunud {0} punkti".format(manguPikkus))
print("{:*^75}".format("*"))


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
    except (AttributeError, TypeError):
        raise AssertionError("Õige ja vale vastus ei ole õiget tüüpi")


def liitmine():
    liidetav = random.randint(1, suurim_number)
    liitja = random.randint(1, suurim_number)
    try:
        vastus = int(input("{0} + {1} = ".format(liidetav, liitja)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oigeVastus = liidetav + liitja
    oigeVoiVale(oigeVastus, vastus)


def lahutamine():
    lahutatav = random.randint(2, suurim_number)
    lahutaja = random.randint(1, lahutatav)
    try:
        vastus = int(input("{0} - {1} = ".format(lahutatav, lahutaja)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oigeVastus = lahutatav - lahutaja
    oigeVoiVale(oigeVastus, vastus)

def korrutamine():
    korrutatav = random.randint(1, 10)
    korrutaja = random.randint(1, suurim_number)
    try:
        vastus = int(input("{0} * {1} = ".format(korrutaja, korrutatav)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oigeVastus = korrutatav * korrutaja
    oigeVoiVale(oigeVastus, vastus)


def tehteValik(tehe):
    try:
        if tehe == 1:
            liitmine()
        elif tehe == 2:
            lahutamine()
        elif tehe == 4:
            korrutamine()
        else:
            v = input("Sinu sisestatud tehtevalik ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
            raise SystemExit
    except (AttributeError, TypeError):
        raise AssertionError("Tehte valik peab olema int tüüpi")

#### tehte valik ###
print()
print("Vali tehe:     1: liitmine     2: lahutamine     3: liitmine ja lahutamine     4: korrutamine")
try:
    tehe = int(input())
except (ValueError):
    v = input("Sinu sisestatud tehtevalik ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
    raise SystemExit

if tehe == 1:
    teheSonadega = "liitmist"
elif tehe == 2:
    teheSonadega = "lahutamist"
elif tehe == 3:
    teheSonadega = "liitmist ja lahutamist"
elif tehe == 4:
    teheSonadega = "korrutamist"

#### raskusastme valik ###
print()
print("Sisesta suurim number, mille piires {0} harjutada: ".format(teheSonadega))
try:
    suurim_number = int(input())
except (ValueError):
    v = input("Sinu sisestatud raskusaste ei ole lubatud. Väljumiseks vajuta Enter ja taaskäivita mäng")
    raise SystemExit

#### mängu käivitus ###
while (punktideCounter < manguPikkus):
    if tehe == 3:
        tehteValik(random.randint(1, 2))
    else:
        tehteValik(tehe)


v = input("Väljumiseks vajuta Enter")
