import random

liczba = random.randint(1, 50)
proba = 0
mojaliczba = 0

print("Zgadnij liczbę od 1 do 50")
print("Masz 5 prób")

while mojaliczba != liczba and proba < 5:
    mojaliczba = int(input("Jaka to liczba?\n"))

    if mojaliczba < liczba:
        print("Za mało!")

    elif mojaliczba > liczba:
        print("Za dużo!")
    proba += 1

if mojaliczba == liczba:
    print("Es, zgadłeś")

else:
    print("Nie tym razem\nMagiczna liczba to:", liczba)
