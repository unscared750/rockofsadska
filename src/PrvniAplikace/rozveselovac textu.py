print("Zadej text k rozveselení: ")

# Vstup od uživatele
text = input()

# Pomocná pole
interpunkce = "!?."
smajlici = [":)", ":D", ":P"]

# Čtení věty
pozice = 0
smajlik = 0

while pozice < len(text):
    # narazilo se na interpunkci
    if text[pozice] in interpunkce:
        # Odstranění tečky
        if text[pozice] == '.':
            text = text[:pozice] + text[pozice + 1:]
            pozice -= 1

        # Vložení smajlíku
        text = text[:pozice + 1] + " " + smajlici[smajlik] + text[pozice + 1:]

        # Úprava pozice příštího smajlíku
        smajlik += 1
        if smajlik > len(smajlici) - 1:
            smajlik = 0
    pozice += 1

# Výpis
print(f"Rozveselený text: {text}")