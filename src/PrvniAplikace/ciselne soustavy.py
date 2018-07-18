#!/usr/bin/env python3

print("Číslo v desítkové soustavě:")
cislo = input()


def decimal_to_base(number, base):
    digits = "0123456789ABCDEF"
    if number == 0:
        return "0"

    result = ""
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base

    return result


def main():
    while True:
        try:
            number = int(cislo)
            base = int(input("Číselná soustava (2-16): "))
            if 2 <= base <= 16:
                print(f"Číslo ve zvolené soustavě: {decimal_to_base(number, base)}")
                break
            else:
                print("Neplatná soustava. Zadejte číslo mezi 2 a 16.")
        except ValueError:
            print("Neplatný vstup. Zadejte prosím čísla.")


if __name__ == "__main__":
    main()