def dodajIPodziel(x):
    return (x+5)/2

def wielomian(x):
    return x**3-2*x**2+x-2

def zlozona(x):
    return wielomian(dodajIPodziel(x))

nums=[1,2,3,4,5]
test=list(map(dodajIPodziel,nums))
print(test)
outputs=list(map(zlozona,nums))
print(outputs)