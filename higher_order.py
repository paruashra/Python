def sumofSquare(number, fun):
    total = 0
    for num in range(1, number + 1):
        total += fun(num)
    
    return total


def square(num): return num * num


def cube(num): return num ** 3


print(sumofSquare(3, square))
print(sumofSquare(3, cube))
  
