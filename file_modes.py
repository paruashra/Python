with open('hello.txt', 'r+') as file:
    file.seek(36)
    file.write('lolo')
    file.seek(0)
    print(file.read())

