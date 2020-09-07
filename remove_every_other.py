def remove_every_other(lst):
    return [lst[num] for num in range(0, len(lst), 2)]


print(remove_every_other([1, 2, 3, 4, 5]))
