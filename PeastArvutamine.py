__author__ = 'einar'

import random

mangu_pikkus = 30
punktide_counter = 0
viimane_tehe = ""


print("{:*^75}".format(" PEAST ARVUTAMISE MÄNG "))
print("** Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha")
print("** Mäng lõppeb, kui oled kokku kogunud {0} punkti".format(mangu_pikkus))
print("{:*^75}".format("*"))


def exit_on_error():
    v = input("Sinu sisestatud andmed ei ole korrektsed. Väljumiseks vajuta Enter ja taaskäivita mäng")
    raise SystemExit


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
    global viimane_tehe

    while True:
        liidetav = random.randint(1, suurim_number)
        liitja = random.randint(1, suurim_number)
        kysimus = "{0} + {1} = ".format(liidetav, liitja)
        if (kysimus != viimane_tehe) or (liidetav == 1 and liitja == 1):
            #kui ühtedega võrdlemist sisse ei too, siis saab süsteemi lolliks ajada
            break

    while True:
        try:
            vastus = int(input(kysimus))
            break

        except (AttributeError, TypeError, ValueError):
            print("Sa ei sisestanud täisarvu. Proovi uuesti.")
    viimane_tehe = kysimus
    oige_vastus = liidetav + liitja
    oige_voi_vale(oige_vastus, vastus)


def lahutamine():
    global viimane_tehe

    while True:
        lahutatav = random.randint(2, suurim_number)
        lahutaja = random.randint(1, lahutatav)
        kysimus = "{0} - {1} = ".format(lahutatav, lahutaja)
        if kysimus != viimane_tehe:
            break

    while True:
        try:
            vastus = int(input(kysimus))
            break

        except (AttributeError, TypeError, ValueError):
            print("Sa ei sisestanud täisarvu. Proovi uuesti.")
    viimane_tehe = kysimus
    oige_vastus = lahutatav - lahutaja
    oige_voi_vale(oige_vastus, vastus)


def korrutamine():
    global viimane_tehe

    while True:
        korrutaja = random.randint(1, 10)
        korrutatav = random.randint(1, suurim_number)
        kysimus = "{0} * {1} = ".format(korrutatav, korrutaja)
        if kysimus != viimane_tehe:
            break

    while True:
        try:
            vastus = int(input(kysimus))
            break

        except (AttributeError, TypeError, ValueError):
            print("Sa ei sisestanud täisarvu. Proovi uuesti.")

    viimane_tehe = kysimus
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
    except (AttributeError, TypeError):
        raise AssertionError("Tehte valik peab olema int tüüpi")

#### tehte valik ###
print()
print("""Vali tehe:
            1: liitmine
            2: lahutamine
            3: liitmine ja lahutamine
            4: korrutamine""")
while True:
    try:
        tehe = int(input())
        if tehe < 5:
            break
        else:
            print("Tehte valimiseks sisesta number, mis on tehte ees. Näiteks: 3")
            print("Proovi uuesti:")
    except (ValueError):
        print("Tehte valimiseks sisesta number, mis on tehte ees. Näiteks: 3")
        print("Proovi uuesti:")

if tehe == 1:
    tehe_sonadega = "liitmist"
elif tehe == 2:
    tehe_sonadega = "lahutamist"
elif tehe == 3:
    tehe_sonadega = "liitmist ja lahutamist"
elif tehe == 4:
    tehe_sonadega = "korrutamist"
else:
    tehe_sonadega = ""
    exit_on_error()

#### raskusastme valik ###
print()
print("Sisesta suurim positiivne täisarv, mille piires {0} harjutada: ".format(tehe_sonadega))
while True:
    try:
        suurim_number = int(input())
        if suurim_number > 0:
            break
        else:
            print("Nullist väiksemate arvudega harjutamine ei ole veel toetatud")
            print("Proovi uuesti:")
    except ValueError:
        print("Sisesta korrektne täisarv. Näiteks: 10")
        print("Proovi uuesti:")


#### mängu käivitus ###
while punktide_counter < mangu_pikkus:
    if tehe == 3:
        tehte_valik(random.randint(1, 2))
    else:
        tehte_valik(tehe)

v = input("Väljumiseks vajuta Enter")
