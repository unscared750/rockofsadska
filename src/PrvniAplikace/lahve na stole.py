for i in range(10, 0, -1):
    if i == 1:
        print(f"{i} zelená láhev stojí na stole a jedna spadne")
    elif i in [2, 3, 4]:
        print(f"{i} zelené láhve stojí na stole a jedna spadne")
    else:
        print(f"{i} zelených láhví stojí na stole a jedna spadne")