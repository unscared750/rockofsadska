x = 0
while True:
    x += 1
    if x >= 50:
        print(f"hodnota x je {x}")
        break

print("Program úspěšně skončil.")

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for cislo in cisla:
    if cislo == 6:
        print("Číslo 6 bylo nalezeno!")
        break
else:
    print("Číslo 6 v seznamu není.")

chyba = ""
if not jmeno:
    chyba = "Jméno je povinný údaj!"
elif " " in jmeno:
    chyba = "Zadej jen křestní jméno!"
elif len(jmeno) < 3:
    chyba = "Jméno je příliš krátké, zadej alespoň 3 znaky!"
elif len(jmeno) > 16:
    chyba = "Jméno je příliš dlouhé, zadej max 16 znaků!"

if not chyba:
    print("Nyní zadej svůj věk")
    # ...
else:
    print("Nevalidní hodnota")
    print("Chyba: " + chyba)
    input()