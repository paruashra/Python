# file = open("open_read.txt")
# file.seek(0)
# print(file.closed)
# file.close()
# print(file.closed)
# print(file.readlines())
# print(file.read())

# for line in file:
#     print(line)

with open('open_read.txt') as file:
    print(file.read())

# print(file.__enter__)
# print(file.__exit__)
print(file.closed)

print()
