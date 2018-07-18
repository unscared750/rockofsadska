print("Zadejte zprávu k zakódování: ")

# Vstup od uživatele
puvodni_zprava = input().lower()
zasifrovana_zprava = ""

# vzorová pole
abeceda = "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                  "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
                  ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

# Přeložení jednotlivých znaků
for znak in puvodni_zprava:
    pozice = abeceda.find(znak)  # 'find()' je ekvivalentní Java 'indexOf()'
    if pozice >= 0:
        zasifrovana_zprava += morseovy_znaky[pozice] + " "

# Výpis
print(f"Zakódovaná zpráva: {zasifrovana_zprava}")

retezec = "Nabuchonodozor"
print(retezec[::2])

retezec = "Mississippi"
print(retezec.count("s"))
print(retezec.count("s", 1, 4))