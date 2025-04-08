from sympy import isprime
from time import time
from random import randint

N = 200

def Wypisz(arr):
    for x in arr:
        print(f"{x} ", end="")
    print()


def Sumowanie(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum


def Prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        else:
            d += 1
    return True


def Palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].upper() == s[j].upper:
            return False
        else:
            i += 1
            j -= 1
    return True


def Insert_Sort(arr):
    i = 2
    for i in range(1, 20):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k


arr = range(N)
Wypisz(arr)
print(f"\n\nSuma liczb po użyciu własnej funkcji: {Sumowanie(arr)}")
print(f"Suma liczb po użyciu wbudowanej funkcji: {sum(arr)}\n")
arr = list(filter(Prime, arr))
print("\nZbiór liczb pierwszych w przedziale od 0 do 199 (z użyciem własnej funkcji): ")
Wypisz(arr)
arr = range(N)
print("\nPonowne wypisanie wszystkich liczb od 0 do 199: ")
Wypisz(arr)
arr = list(filter(isprime, arr))
print("\nZbiór liczb pierwszych w przedziale od 0 do 199 (z użyciem wbudowanej funkcji): ")
Wypisz(arr)
tab = [randint(0, N) for i in range(20)]
print("\n\nNieposortowana tablica losowych liczb od 0 do 200:")
Wypisz(tab)
print("\nPosortowana tablica losowych liczb od 0 do 200 (z użyciem własnej funkcji):")
Insert_Sort(tab)
Wypisz(tab)
print("\nPosortowana tablica losowych liczb od 0 do 200 (z użyciem wbudowanej funkcji):")
tab.sort()
Wypisz(tab)
s = input("\n\nTekst: ")
print(f"Czy {s} to palindrom (użycie własnej funkcji) - {"TAK" if Palindrome(s) else "NIE"}")
print(f"Czy {s} to palindrom (bez użycia własnej funckji) - {"TAK" if s == s[::-1] else "NIE"}")
