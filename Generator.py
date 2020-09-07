def count_up_to(maxi):
    count = 1
    while count < maxi:
        yield count
        count += 1

    
counter = count_up_to(10)

print(next(counter))

for num in counter:
    print(num)

