retezec = "Bum! "
print(retezec * 7)
jazyk = "Python"
zprava = "je nejlepší!"
print(jazyk + zprava)
print(len("a"))
print(len("Python"))
print("Tento řetězec \npokračuje na novém řádku, odskočí \to jeden tabulátor, vypíše zpětné lomítko: \\ a jednoduchou uvozovku: \'. Pak skončí.")
prazdny_retezec = ""
jazyk = "Python"

print(bool(prazdny_retezec))
print(bool(jazyk))
zprava = "Toto je víceřádkový řetězec vytvořený\npoužitím dvojitých uvozovek a znaku pro nový řádek."
viceradkova_zprava = '''Toto je také víceřádkový
řetězec, ale je vytvořený pomocí
trojitých uvozovek.'''
print(zprava)
print(viceradkova_zprava)

vstup = "krokrohnoshroch"
print(vstup.startswith("krok"))
print(vstup.endswith("hroch"))
print("roh" in vstup)
print("nos" in vstup)


nastaveni = "Fullscreen shaDows autosave"
nastaveni = nastaveni.lower()

print("Poběží hra ve fullscreenu?")
print("fullscreen" in nastaveni)

print("Budou zapnuté stíny?")
print("shadows" in nastaveni)

print("Přeje si hráč vypnout zvuk?")
print("nosound" in nastaveni)

print("Přeje si hráč hru automaticky ukládat?")
print("autosave" in nastaveni)

print("Zadejte číslo:")
vstup = input()
print("Zadal jste text: " + vstup)
print("Text po funkci strip: " + vstup.strip())

cislo = int(vstup.strip())
print("Převedl jsem zadaný text na číslo parsováním, zadal jste: " + str(cislo))

veta = "C# je nejlepší!"
veta = veta.replace("C#", "Python")
print(veta)


if (4 > 5):
    print("Pravda")
print("Program zde pokračuje dál")

s1 = "Tohle je původní text"
s2 = s1
s1 = "Tohle je nový text"
print(s1)
print(s2)

float_num = 3.9
int_num = int(float_num)
print(int_num)

from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
soucet = a + b
print(soucet)  # vrátí přesně 0.3