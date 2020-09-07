# def current_beat():
#     maxNum = 100
#     nums = (1, 2, 3, 4)
#     i = 0 
#     result = []
#     while len(result) < maxNum:
#         if i >= len(nums) : i = 0
#         result.append(nums[i])
#         i += 1
#     return result


def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums) : i = 0
        yield nums[i]
        i += 1


print(current_beat())

# for num in current_beat():
#     print(num)

