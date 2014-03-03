__author__ = 'einar'

import random

mangu_pikkus = 30
punktide_counter = 0

print("{:*^75}".format(" PEAST ARVUTAMISE MÄNG "))
print("** Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha")
print("** Mäng lõppeb, kui oled kokku kogunud {0} punkti".format(mangu_pikkus))
print("{:*^75}".format("*"))


def exit_on_error():
    v = input("Sinu sisestatud andmed ei ole korrektsed. Väljumiseks vajuta Enter ja taaskäivita mäng")

def oige_voi_vale(param1, param2):
    global punktide_counter

    try:
        if param1 != param2:
            punktide_counter -= 2
            print("VALE VASTUS")
            print()
        else:
            punktide_counter += 1
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
    oige_vastus = liidetav + liitja
    oige_voi_vale(oige_vastus, vastus)

def lahutamine():
    lahutatav = random.randint(2, suurim_number)
    lahutaja = random.randint(1, lahutatav)
    try:
        vastus = int(input("{0} - {1} = ".format(lahutatav, lahutaja)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oige_vastus = lahutatav - lahutaja
    oige_voi_vale(oige_vastus, vastus)

def korrutamine():
    korrutaja = random.randint(1, 10)
    korrutatav = random.randint(1, suurim_number)
    try:
        vastus = int(input("{0} * {1} = ".format(korrutatav, korrutaja)))
    except (AttributeError, TypeError):
        raise AssertionError("Sa ei sisestanud täisarvu")
    oige_vastus = korrutatav * korrutaja
    oige_voi_vale(oige_vastus, vastus)

def tehte_valik(tehe):
    try:
        if tehe == 1:
            liitmine()
        elif tehe == 2:
            lahutamine()
        elif tehe == 4:
            korrutamine()
        else:
            exit_on_error()
            raise SystemExit
    except (AttributeError, TypeError):
        raise AssertionError("Tehte valik peab olema int tüüpi")

#### tehte valik ###
print()
print("""Vali tehe:   
	1: liitmine   
	2: lahutamine   
	3: liitmine ja lahutamine   
	4: korrutamine""")
try:
    tehe = int(input())
except (ValueError):
    exit_on_error()
    raise SystemExit

if tehe == 1:
    tehe_sonadega = "liitmist"
elif tehe == 2:
    tehe_sonadega = "lahutamist"
elif tehe == 3:
    tehe_sonadega = "liitmist ja lahutamist"
elif tehe == 4:
    tehe_sonadega = "korrutamist"
else:
    exit_on_error()

#### raskusastme valik ###
print()
print("Sisesta suurim number, mille piires {0} harjutada: ".format(tehe_sonadega))
try:
    suurim_number = int(input())
except (ValueError):
    exit_on_error()
    raise SystemExit

#### mängu käivitus ###
while (punktide_counter < mangu_pikkus):
    if tehe == 3:
        tehte_valik(random.randint(1, 2))
    else:
        tehte_valik(tehe)

v = input("Väljumiseks vajuta Enter")
