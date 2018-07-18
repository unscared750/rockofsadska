#!/usr/bin/env python3

cisla = input("Zadej čísla pro seřazení (oddělená čárkou):")


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def parse_input(user_input):
    try:
        numbers = [int(num.strip()) for num in user_input.split(',') if num.strip()]
        return numbers
    except ValueError:
        print("Neplatný vstup. Zadejte pouze celá čísla oddělená čárkou.")
        return None


def main():
    numbers = parse_input(cisla)

    if numbers is not None:
        selection_sort(numbers)
        print("Seřazená čísla:")
        print(", ".join(map(str, numbers)))


if __name__ == "__main__":
    main()
