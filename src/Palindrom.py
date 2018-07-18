slovo = input("Zadej palindrom: \n")
if slovo == slovo[::-1]:  # Kontrola, zda je slovo shodné se svou opačnou verzí
    print("Ano, je to palindrom")
else:  # Tento blok musí být správně zarovnaný
    print("Ne, není to palindrom")

