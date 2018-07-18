import math
# Načtení koeficientů od uživatele
a = float(input("Zadej koeficient a: "))
b = float(input("Zadej koeficient b: "))
c = float(input("Zadej koeficient c: "))

# Výpočet diskriminantu
D = b**2 - 4*a*c

# Výpočet a výpis řešení
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Rovnice má dva reálné kořeny: x₁ = {x1}, x₂ = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Rovnice má jeden dvojnásobný reálný kořen: x = {x}")
else:
    print("Rovnice nemá reálné kořeny.")