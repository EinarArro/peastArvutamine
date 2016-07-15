import random
import time

manguPikkus = 30
punktideCounter = 0

print("{:*^70}".format(" PEAST ARVUTAMISE MÄNG "))
print("***** Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha".format('centered'))
print("***** Mäng lõppeb, kui oled kokku kogunud {0} punkti".format(manguPikkus))
print("{:*^70}".format("*"))


def arvutaRaskusaste(param):
    if param == 1:
        raskusaste = 10
    elif param == 2:
        raskusaste = 20
    elif param == 3:
        raskusaste = 30
    elif param == 4:
        raskusaste = 40
    return raskusaste

def oigeVoiVale(param1, param2):
    global punktideCounter
    
    if param1 != param2:
        punktideCounter -= 2
        print("VALE VASTUS")
        print()
    else:
        punktideCounter += 1
        print()
        #print(punktideCounter)

def vastus(oigeVastus):
    vastus = int(input())
    oigeVoiVale(oigeVastus, vastus) 

def liitmine():
    liidetav = random.randint(1, raskusaste)
    liitja = random.randint(1, raskusaste)
    print("{0} + {1} = ".format(liidetav, liitja))
    oigeVastus = liidetav + liitja
    vastus(oigeVastus)

def lahutamine():
    lahutatav = random.randint(2, raskusaste)
    lahutaja = random.randint(1, lahutatav)
    print("{0} - {1} = ".format(lahutatav, lahutaja))
    oigeVastus = lahutatav - lahutaja
    vastus(oigeVastus)

def tehteValik(tehe):
    if tehe == 1:
        liitmine()
    else:
        lahutamine()

def prindiAeg(start, end):
    print("Aeg: {0:.0f} sekundit".format(end-start))
        
print()
print("Vali raskusaste:     1: kuni 10     2: kuni 20     3: kuni 30     4: kuni 40")
raskusaste_in = int(input())
raskusaste = arvutaRaskusaste(raskusaste_in)
    
print("Vali tehe:     1: liitmine     2: lahutamine     3: liitmine ja lahutamine")
tehe = int(input())

start = time.time()

while (punktideCounter < manguPikkus):
    if tehe == 3:
        tehteValik(random.randint(1,2))
    else:
        tehteValik(tehe)

end = time.time()
time = end-start
print("Mängu läbimiseks kulus {0:.0f} minutit ja {1:.0f} sekundit".format((time // 60), (time % 60)))
a = input("Väljumiseks vajuta Enter")
