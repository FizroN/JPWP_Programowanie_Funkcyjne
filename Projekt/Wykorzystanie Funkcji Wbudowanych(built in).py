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
    while i <= j:
        if s[i] != s[j]:
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


if __name__ == "__main__":
    arr = range(N)
    Wypisz(arr)
    stime = time()
    print(f"\n\nSuma liczb po użyciu własnej funkcji: {Sumowanie(arr)}")
    print(f"Czas wykonania: {time() - stime}")
    stime = time()
    print(f"Suma liczb po użyciu wbudowanej funkcji: {sum(arr)}")
    print(f"Czas wykonania: {time() - stime}\n\n")
    print("Zbiór liczb pierwszych w przedziale od 0 do 199 (z użyciem własnej funkcji): ")
    stime = time()
    arr = list(filter(Prime, arr))
    Wypisz(arr)
    print(f"Czas wykonania: {time() - stime}")
    arr = range(N)
    print("\nPonowne wypisanie wszystkich liczb od 0 do 199: ")
    Wypisz(arr)
    print("\nZbiór liczb pierwszych w przedziale od 0 do 199 (z użyciem wbudowanej funkcji): ")
    stime = time()
    arr = list(filter(isprime, arr))
    Wypisz(arr)
    print(f"Czas wykonania: {time() - stime}")
    tab = [randint(0, N) for i in range(20)]
    print("\n\nNieposortowana tablica losowych liczb od 0 do 200:")
    Wypisz(tab)
    A = tab[::]
    print("\nPosortowana tablica losowych liczb od 0 do 200 (z użyciem własnej funkcji):")
    stime = time()
    Insert_Sort(A)
    Wypisz(A)
    print(f"Czas wykonania: {time() - stime}")
    A = tab[::]
    print("\nPosortowana tablica losowych liczb od 0 do 200 (z użyciem wbudowanej funkcji):")
    stime = time()
    A.sort()
    Wypisz(A)
    print(f"Czas wykonania: {time() - stime}")
    s = input("\n\nTekst: ")
    stime = time()
    print(f"Czy {s} to palindrom (użycie własnej funkcji) - {"TAK" if Palindrome(s.upper()) else "NIE"}")
    print(f"Czas wykonania: {time() - stime}")
    stime = time()
    print(f"\nCzy {s} to palindrom (bez użycia własnej funckji) - {"TAK" if s.upper() == s[::-1].upper() else "NIE"}")
    print(f"Czas wykonania: {time() - stime}")
