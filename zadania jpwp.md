# 1. Mając daną funkcję x^3 - 2x^2 + x - 2, użyj w Pythonie map() i lambdy aby obliczyć wartości tej funkcji dla argumentów [1, 2, 3, 4, 5]. Potem, użyj filter() aby zwrócić wartości większe od 10.

Przydatna dokumentacja: https://docs.python.org/3/howto/functional.html

Oczekiwany output: [34, 78]


# 2. Mając do dyspozycji listę liczb: [3, 6, 8, 12, 15, 18, 21] oraz funkcje enumerate() i filter(), uzyskaj takie wartości liczb, których indeks jest parzysty a jednocześnie sama liczba jest podzielna przez 3.

Oczekiwany output: [(0, 3), (4, 15), (6, 21)] (wersja bez krotek też jest uznawana: (3, 15, 21))


# 3. Napisz funkcję, która rekurencyjne oblicza silnię z podanej liczby całkowitej. Potem użyj tej funkcji oraz list liczb od 1 do 5 włącznie, aby stworzyć słownik, który jako klucz przechowuje argument, a jako wartość przechowuje wynik działania funkcji.

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Oczekiwany output: {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}


# 4. Używając funkcji reduce() z biblioteki functools oblicz iloczyn liczb z listy [3, 4, 5, 6]. Potem, oblicz sumę i średnią tych liczb używając sum() i len() i wyświetl wynik działania wszystkich trzech operacji.

Oczekiwany output:
Iloczyn: 360
Suma: 18
Średnia: 4.5


# 5. Napisz dwie funkcje, gdzie pierwsza funkcja f dodaje do inputu 5 i dzieli przez 2, a druga funkcja g jest wielomianem z zadania 1. Następnie, złóż dwie funkcje ze sobą, tak, że f zwraca wynik swojego działania do g. Używając tak złożonej funkcji, użyj map(), aby obliczyć wartości tej funkcji złożonej dla wartości [1, 2, 3, 4, 5].

Oczekiwany output: [10.0,  19.875,  34.0,  53.125,  78.0]
