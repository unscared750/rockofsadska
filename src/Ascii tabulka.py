print("ASCII tabulka")
print("=============")
for kod in range(256):
    print(f"{kod} : {chr(kod)}", end=" ")


print("ASCII tabulka")
print("=============")
for i in range(256):
    print(str(i) + ' : ' + str(chr(i)) + '\t', end='')
input()