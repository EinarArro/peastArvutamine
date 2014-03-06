__author__ = 'einar'

import random

game_length = 30
points_counter = 0
last_calculation = ""


print("{:*^75}".format(" PEAST ARVUTAMISE MÄNG "))
print("** Iga õige vastus annab ühe punkti. Iga vale vastus võtab kaks punkti maha")
print("** Mäng lõppeb, kui oled kokku kogunud {0} punkti".format(game_length))
print("{:*^75}".format("*"))


def exit_on_error():
    error_message = input("Sinu sisestatud andmed ei ole korrektsed. Väljumiseks vajuta Enter ja taaskäivita mäng")
    raise SystemExit


def right_or_wrong_answer(right_answer, answer):
    global points_counter

    try:
        if right_answer != answer:
            points_counter -= 2
            print("VALE VASTUS")
            print()
        else:
            points_counter += 1
            print()
    except (AttributeError, TypeError):
        raise AssertionError("Õige ja vale vastus ei ole õiget tüüpi")


def addition():
    global last_calculation

    while True:
        addend = random.randint(1, biggest_number)
        adder = random.randint(1, biggest_number)
        question = "{0} + {1} = ".format(addend, adder)
        if (question != last_calculation) or (addend == 1 and adder == 1):
            #kui ühtedega võrdlemist sisse ei too, siis saab süsteemi lolliks ajada
            break

    while True:
        try:
            answer = int(input(question))
            break

        except (AttributeError, TypeError, ValueError):
            print("Sa ei sisestanud täisarvu. Proovi uuesti.")
    last_calculation = question
    right_answer = addend + adder
    right_or_wrong_answer(right_answer, answer)


def subtraction():
    global last_calculation

    while True:
        subtractive = random.randint(2, biggest_number)
        subtracter = random.randint(1, subtractive)
        question = "{0} - {1} = ".format(subtractive, subtracter)
        if question != last_calculation:
            break

    while True:
        try:
            answer = int(input(question))
            break

        except (AttributeError, TypeError, ValueError):
            print("Sa ei sisestanud täisarvu. Proovi uuesti.")
    last_calculation = question
    right_answer = subtractive - subtracter
    right_or_wrong_answer(right_answer, answer)


def multiplication():
    global last_calculation

    while True:
        multiplier = random.randint(1, 10)
        multiplicand = random.randint(1, biggest_number)
        question = "{0} * {1} = ".format(multiplicand, multiplier)
        if question != last_calculation:
            break

    while True:
        try:
            answer = int(input(question))
            break

        except (AttributeError, TypeError, ValueError):
            print("Sa ei sisestanud täisarvu. Proovi uuesti.")

    last_calculation = question
    right_answer = multiplicand * multiplier
    right_or_wrong_answer(right_answer, answer)


def choose_calculation_type(calculation_type_in):
    try:
        if calculation_type_in == 1:
            addition()
        elif calculation_type_in == 2:
            subtraction()
        elif calculation_type_in == 4:
            multiplication()
        else:
            exit_on_error()
    except (AttributeError, TypeError, ValueError):
        raise AssertionError("Tehte valik peab olema int tüüpi")

#### Let user choose calculation type ###
print()
print("""Vali tehe:
            1: liitmine
            2: lahutamine
            3: liitmine ja lahutamine
            4: korrutamine""")
while True:
    try:
        calculation_type = int(input())
        if calculation_type < 5:
            break
        else:
            print("Tehte valimiseks sisesta number, mis on tehte ees. Näiteks: 3")
            print("Proovi uuesti:")
    except ValueError:
        print("Tehte valimiseks sisesta number, mis on tehte ees. Näiteks: 3")
        print("Proovi uuesti:")

if calculation_type == 1:
    calculation_type_in_string_with_grammatics = "liitmist"
elif calculation_type == 2:
    calculation_type_in_string_with_grammatics = "lahutamist"
elif calculation_type == 3:
    calculation_type_in_string_with_grammatics = "liitmist ja lahutamist"
elif calculation_type == 4:
    calculation_type_in_string_with_grammatics = "korrutamist"
else:
    calculation_type_in_string_with_grammatics = ""
    exit_on_error()

#### Let user choose biggest number ###
print()
print("Sisesta suurim positiivne täisarv, mille piires {0} harjutada: ".format(calculation_type_in_string_with_grammatics))
while True:
    try:
        biggest_number = int(input())
        if biggest_number > 0:
            break
        else:
            print("Nullist väiksemate arvudega harjutamine ei ole veel toetatud")
            print("Proovi uuesti:")
    except ValueError:
        print("Sisesta korrektne täisarv. Näiteks: 10")
        print("Proovi uuesti:")


#### mängu käivitus ###
while points_counter < game_length:
    if calculation_type == 3:
        choose_calculation_type(random.randint(1, 2))
    else:
        choose_calculation_type(calculation_type)

v = input("Väljumiseks vajuta Enter")
