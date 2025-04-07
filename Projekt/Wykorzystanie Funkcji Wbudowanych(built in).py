N = 200

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

arr = range(N)
arr = list(filter(Prime, arr))
for n in arr:
    print(f"{n} ", end="")
