import random
import time
from collections import deque


manguPikkus = 5  # muuda seda numbrit, kui tahad mängu pikkust muuta
punktideCounter = 0
queue = deque(maxlen=5)


def taida_que_randomiga():
    for i in range(0, 5):
        random_string= "XYZ{0}".format(i)
        queue.append(random_string)


def print_mangu_kirjeldus():
    print('{:*^80}'.format(' PEAST ARVUTAMISE MÄNG '))
    print('{:*^80}'.format(' Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha '))
    print('{:*^80}'.format("*** Mäng lõppeb, kui oled kokku kogunud {0} punkti ***".format(manguPikkus)))


def kysi_raskusaste():
    raskus = int(input("Sisesta suurim number, mille piires soovid arvutada: "))
    return raskus


def kysi_tehe():
    print()
    tehe = int(input(
        """Vali tehe:
             1: liitmine
             2: lahutamine
             3: liitmine ja lahutamine

             Valik: """
    ))
    return tehe


def oige_voi_vale(param1, param2):
    global punktideCounter

    if param1 != param2:
        punktideCounter -= 2
        print("VALE VASTUS")
        print()
    else:
        punktideCounter += 1
        print()


def kontrolli_vastus(oigeVastus):
    try:
        vastus = int(input())
        oige_voi_vale(oigeVastus, vastus)
    except:
        print()
        print("Lubatud on ainult numbrid. Ole hoolikam!")
        print()


def kontrolli_unikaalsust(tehe):
    if tehe in queue:
        return False
    else:
        return True


def arvuta_liitmise_tehe():
    unikaalne = False
    while True:
        liidetav = random.randint(1, raskusaste)
        liitja = random.randint(1, raskusaste)
        oige_vastus = liidetav + liitja
        tehe = "{0} + {1} = ".format(liidetav, liitja)
        unikaalne = kontrolli_unikaalsust(tehe)
        if unikaalne == True:
            queue.append(tehe)
            return (tehe, oige_vastus)
            break


def liitmine():
    tehe, oigeVastus = arvuta_liitmise_tehe()
    print(tehe)
    kontrolli_vastus(oigeVastus)


def arvuta_lahutamise_tehe():
    unikaalne = False
    while True:
        lahutatav = random.randint(2, raskusaste)
        lahutaja = random.randint(1, lahutatav)
        oige_vastus = lahutatav - lahutaja
        tehe = "{0} - {1} = ".format(lahutatav, lahutaja)
        unikaalne = kontrolli_unikaalsust(tehe)
        if unikaalne == True:
            queue.append(tehe)
            return (tehe, oige_vastus)
            break


def lahutamine():
    tehe, oigeVastus = arvuta_lahutamise_tehe()

    print(tehe)
    kontrolli_vastus(oigeVastus)


def tehte_valik(tehe):
    if tehe == 1:
        liitmine()
    else:
        lahutamine()


### Mägu käivitamine ###


print_mangu_kirjeldus()
print()
raskusaste = kysi_raskusaste()
tehe = kysi_tehe()
taida_que_randomiga()
start = time.time()

while punktideCounter < manguPikkus:
    if tehe == 3:
        tehte_valik(random.randint(1, 2))
    else:
        tehte_valik(tehe)

end = time.time()
time = end - start
print("Mängu läbimiseks kulus {0:.0f} minutit ja {1:.0f} sekundit".format((time // 60), (time % 60)))
a = input("Väljumiseks vajuta Enter")
