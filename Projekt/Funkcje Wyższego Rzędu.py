from math import sin, pi

if __name__ == "__main__":
    f = lambda x: x**3 - 3*x**2 + 4*x + 2
    print("f(x) = x³ + 3x² + 4x + 2\n")
    h = 1
    while h >= 1e-12:
        df = lambda x: (f(x + h) - f(x)) / h
        print(f"f'({1}) = {df(1)}")
        h /= 10


    compose = lambda f, g: lambda x: f(g(x))
    f = lambda x: x**2
    print("\n\nf(x) = x²")
    g = lambda x: x + 1
    print("g(x) = x + 1")
    h = compose(f, g)
    print("(f ∘ g)(x) = (x + 1)²\n")
    for i in range(5):
        print(f"(f ∘ g)({i}) = {h(i)}")


    print("\n\nf(x) = sin(x)/x")
    f = lambda x : sin(x) / x
    lim = lambda x: "Granica nie istnieje" if abs(x) == float("inf") else f"lim(x->{x})f(x) = {f(x)}" if x != 0  else f"lim(x->0)f(x) = 1"
    print(lim(1))
    print(lim(pi / 6))
    print(lim(pi / 2))
    print(lim(0))
    print(lim(float("inf")))
    print(lim(-float("inf")))
