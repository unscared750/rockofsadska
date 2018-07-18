def nacti_cislo(text_zadani, text_chyba):
    cislo_nezadano = True
    while cislo_nezadano:
        try:
            cislo = float(input(text_zadani))
            cislo_nezadano = False
        except ValueError:
            print(text_chyba)

    return cislo

def dalsi_priklad():
    odpoved_nevalidni = True
    while odpoved_nevalidni:
        odpoved = input("\nPřejete si zadat další příklad? ano / ne: ").lower()
        if odpoved == "ano" or odpoved == "ne":
            odpoved_nevalidni = False
        else:
            print("Prosím, odpovězte 'ano' nebo 'ne'.")

    return odpoved == "ano"  #  Když bude v proměnné odpoved uložen řetězec "ano", funkce vrátí hodnotu True. Jinak vrátí False.

def proved_operaci(a, b):
    operace = 0
    while operace not in [1, 2, 3, 4]:
        print("1 - sčítání")
        print("2 - odčítání")
        print("3 - násobení")
        print("4 - dělení")

        # Abychom nemuseli znovu při vybírání operace ošetřovat uživatelský vstup, využijeme zde naši již vytvořenou funkci
        # Její výstup (typu float) přetypujeme na int
        operace = int(nacti_cislo("Zadejte číslo pro vybranou operaci: ", "Neplatný vstup. Zadejte prosím číslo."))

        if operace == 4 and b == 0:
            print("Nulou nelze dělit! Zkuste jinou operaci.")
            operace = 0  # Reset operace kvůli dělení nulou

        elif operace < 1 or operace > 4:
            print("Neplatná volba. Zadejte číslo odpovídající vybrané operaci.")  # Ošetření neplatného vstupu

    match operace:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b

print("Kalkulačka\n")
pokracovat = True

while pokracovat:
    prvni_cislo = nacti_cislo("Zadej číslo: ", "Neplatné číslo!\n")
    druhe_cislo = nacti_cislo("Zadej číslo: ", "Neplatné číslo!\n")
    vysledek_vypoctu = proved_operaci(prvni_cislo, druhe_cislo)
    print(f"Výsledek: {vysledek_vypoctu}")
    pokracovat = dalsi_priklad()

print("Děkuji za použití kalkulačky, aplikaci ukončíte klávesou Enter.")
input()