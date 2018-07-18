#!/usr/bin/env python3

#!/usr/bin/env python3

for i in range(8):  # Pevná velikost šachovnice 8x8
    for j in range(8):
        if (i + j) % 2 == 0:
            print(" ", end="")  # Světlé pole
        else:
            print("█", end="")  # Tmavé pole
    print()  # Nový řádek po každé řadě

