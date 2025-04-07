def is_greater(x):
    if(x>10):
        return True
    else:
        return False

nums=[1,2,3,4,5]
outputs=list(map(lambda x: x**3-2*x**2+x-2, nums))
print(nums)
print(outputs)

greater_than=list(filter(is_greater, outputs))

print(greater_than)