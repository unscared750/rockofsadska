a = int(input("Zadejte číslo v rozmezí 10-20: "))
if a >= 10 and a <= 20:
    print("Zadal jsi správně")
else:
    print("Zadal jsi špatně")

a = int(input("Zadejte číslo v rozmezí 10-20 nebo 30-40: "))
if (a >= 10 and a <= 20) or (a >= 30 and a <= 40):
    print("Zadal jsi správně")
else:
   print("Zadal jsi špatně")

print("Vítejte v kalkulačce")
a = float(input("Zadejte první číslo: "))
b = float(input("Zadejte druhé číslo: "))
print("Zvolte si operaci: ")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")
operace = int(input())

if (operace == 1):
    vysledek = a + b
elif (operace == 2):
    vysledek = a - b
elif (operace == 3):
    vysledek = a * b
elif (operace == 4):
    if b != 0:
        vysledek = a / b
    else:
        print("Nulou nelze dělit!")
        vysledek = "N/A"
if operace > 0 and operace < 5:
    print(f"Výsledek: {vysledek}")
else:
    print("Neplatná volba")
print("Děkuji za použití kalkulačky.")

print("Vítejte v kalkulačce")
a = float(input("Zadejte první číslo:"))
b = float(input("Zadejte druhé číslo:"))
print("Zvolte si operaci:")
print("1 - sčítání")
print("2 - odčítání")
print("3 - násobení")
print("4 - dělení")
volba = int(input())
vysledek = 0.0
match volba:
    case 1:
        vysledek = a + b
    case 2:
        vysledek = a - b
    case 3:
        vysledek = a * b
    case 4:
        if b != 0:
            vysledek = a / b
        else:
            print("Nulou nelze dělit!")
            vysledek = "N/A"

if volba > 0 and volba < 5:
    print(f"Výsledek: {vysledek}")
else:
    print("Neplatná volba")
print("Děkuji za použití kalkulačky, aplikaci ukončíte libovolnou klávesou.")


x = 10  # Hodnota pro demonstrování

match x:
    case 10:
        print("Začátek bloku pro hodnotu 10.")  # Všimněme si více příkazů v jedné větvi case
        print("x je rovno 10. ")                # v bloku s odsazením
        print("Konec bloku pro hodnotu 10. Zde dojde k opuštění match.")
    case 20:
        print("x je rovno 20.") #
    case 30:
        print("x je rovno 30.")
    case _:
        print("x má jinou hodnotu.")