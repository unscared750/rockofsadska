
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(cisla[0])
cisla[5] = 50
print(cisla[5])
(print())  #mezera mezi radky

cisla = list(range(1,11))
for cislo in cisla:
    print(cislo, end=" ")

(print())

simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
for i, prvek in enumerate(simpsons):
    print(f"{i}: {prvek}")

cisla = range(10)
print(list(cisla))
print(list(cisla[0:5]))
print(list(cisla[2:8]))
print(list(cisla[1:7:2]))
print(list(cisla[2:9:2]))
print(list(cisla[6:]))

cisla = [5, 10, 15, 20, 25]

nejmensi = min(cisla)
print(f"Nejmenší číslo v seznamu je: {nejmensi}")

nejvetsi = max(cisla)
print(f"Největší číslo v seznamu je: {nejvetsi}")

soucet = sum(cisla)
print(f"Součet všech čísel v seznamu je: {soucet}")


(print())

cisla = [2, 8, 1, 5, 3]
setridena_cisla = sorted(cisla)
print(f"Neuspořádaná čísla: {cisla}")
print(f"Setříděná čísla: {setridena_cisla}")

cisla = range(10)

print(list(cisla[1:7:2]))

for i in range(1, 11, 2):
    print(i, end = ' ')