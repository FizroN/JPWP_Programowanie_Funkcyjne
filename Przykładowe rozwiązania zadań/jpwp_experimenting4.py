import functools
from functools import reduce

nums=[3, 4, 5, 6]

def myfunc(x, y):
    return x*y

output=functools.reduce(myfunc, nums, 1)
print(output)

output2=sum(nums)
print(output2)

output3=sum(nums)/len(nums)
print(output3)