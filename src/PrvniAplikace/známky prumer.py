#!/usr/bin/env python3

print("Výpočet průměru známek")
print("Zadejte známky oddělené čárkou: ")

vstup = input()

try:
    # Převod vstupu na seznam čísel (int)
    znamky = [int(znamka.strip()) for znamka in vstup.split(",")]

    # Kontrola, zda uživatel zadal alespoň jednu známku
    if len(znamky) == 0:
        print("Nebyla zadána žádná známka. Ukončuji program.")
    else:
        # Výpočet průměru
        prumer = sum(znamky) / len(znamky)
        print(f"Průměr: {prumer:.3f}")
except ValueError:
    # Ošetření chyby převodu na číslo
    print("Vstup obsahuje neplatný znak. Zadávejte pouze čísla oddělená čárkou.")
