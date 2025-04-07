input=[3, 6, 8, 12, 15, 18, 21]

enums=list(enumerate(input))

print(enums)

def even_index(x):
    return x[0]%2==0

def div_by_three(x):
    return x[1]%3==0

output=list(filter(even_index,enums))
print(output)
output=list(filter(div_by_three,output))
print(output)