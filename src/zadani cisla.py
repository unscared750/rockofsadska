a = int(input("Zadej nějaké číslo: "))
if (a > 5):
    print("Zadal jsi číslo větší než 5!")
print("Děkuji za zadání")



a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
    odmocnina = a ** (1 / 2)
    print(f"Odmocnina z čísla {a} je {odmocnina}")
print("Děkuji za zadání")


a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a >= 0):
    print("Zadal jsi nezáporné číslo, to znamená, že ho mohu odmocnit!")
    odmocnina = a ** (1 / 2)
    print(f"Odmocnina z čísla {a} je {odmocnina} ")
if (a < 0):
    print("Odmocnina ze záporného čísla neexistuje v oboru reálných čísel!")
print("Děkuji za zadání")



a = int(input("Zadej nějaké číslo, ze kterého spočítám odmocninu: "))
if (a >= 0):
    print("Zadal jsi nezáporné číslo, to znamená, že ho mohu odmocnit!")
    odmocnina = a ** (1 / 2)
    print(f"Odmocnina z čísla {a} je {odmocnina}")
else:
    print("Odmocnina ze záporného čísla neexistuje v oboru reálných čísel!")
print("Děkuji za zadání")



cislo = 0 # deklarace proměnné s hodnotou 0

if (cislo == 0): # pokud je hodnota proměnné 0, změníme hodnotu na 1
    cislo = 1
if (cislo == 1): # pokud je hodnota proměnné 1, změníme hodnotu na 0
    cislo = 0

print(cislo)

cislo = 0 # deklarace proměnné s hodnotou 0

if (cislo == 0): # pokud je hodnota proměnné 0, změníme hodnotu na 1
    cislo = 1
else: # pokud je hodnota proměnné 1, změníme hodnotu na 0
    cislo = 0

print(cislo)