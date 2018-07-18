# Funkce pro šifrování textu
def encrypt(vstup, heslo):
    vystup = ""
    for i, znak in enumerate(vstup):
        # Pokud není znak písmeno, přeskočíme šifrování a ponecháme znak
        if not znak.isalpha():
            vystup += znak
            continue

        posun = ord(heslo[i % len(heslo)].lower()) - (ord("a"))
        if znak.islower():
            vysledek = chr((ord(znak) - ord("a") + posun) % 26 + ord("a"))
        elif znak.isupper():
            vysledek = chr((ord(znak) - ord("A") + posun) % 26 + ord("A"))
        vystup += vysledek
    return vystup


# Funkce pro dešifrování textu
def decrypt(vstup, heslo):
    vystup = ""
    for i, znak in enumerate(vstup):
        # Pokud není znak písmeno, přeskočíme dešifrování a ponecháme znak
        if not znak.isalpha():
            vystup += znak
            continue

        posun = ord(heslo[i % len(heslo)].lower()) - (ord("a"))
        if znak.islower():
            vysledek = chr((ord(znak) - ord("a") - posun) % 26 + ord("a"))
        elif znak.isupper():
            vysledek = chr((ord(znak) - ord("A") - posun) % 26 + ord("A"))
        vystup += vysledek
    return vystup
