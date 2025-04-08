def add(a, b):
    a = a + b


def insert(arr, num):
    arr.append(num)


x = int(input("x = "))
y = int(input("y = "))
add(x, y)
print(x)
tab = [i for i in range(1, 4)]
print(tab)
n = int(input("Co chcesz dodać do listy: "))
insert(tab, n)
print(tab)
