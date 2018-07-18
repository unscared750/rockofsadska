smajlik = input("Zadej smajlíka: \n")

odpoved = "Tvůj smajlík je"
# typ smajlíka
typ = ""

if smajlik == ":)":
    typ = "veselý"
elif smajlik == ":-)":
     typ = "veselý"
elif smajlik == ":(":
    typ = "smutný"
elif smajlik == ":*":
    typ = "zamilovaný"
elif smajlik == ":-P":
    typ = "s vyplazeným jazykem"
elif smajlik == ":-(":
    typ = "smutný"
elif smajlik == ":-*":
    typ = "zamilovaný"
elif smajlik == ":P":
    typ = "s vyplazeným jazykem"
else:
    typ = "neznámý"

print(odpoved, typ)
input()

