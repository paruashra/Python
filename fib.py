def fib_list(max1):
    nums = []
    a, b = 0, 1
    while len(nums) < max1:
        a, b = b, a + b
        nums.append(a)
    return nums

    
print(fib_list(10))


def fib_gen(max1):
    a, b = 0, 1
    i = 0
    while i < max1:
        a, b = b, a + b
        yield a
        i += 1


gen = fib_gen(10)

for num in gen:
    print(num)
