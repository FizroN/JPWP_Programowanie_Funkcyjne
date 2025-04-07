def factorial(x):
    if(x==0):
        return 1
    else:
        return x*factorial(x-1)

input=[1, 2, 3, 4, 5]

factorials=map(factorial, input)
output=dict(zip(input, factorials))
print(output)