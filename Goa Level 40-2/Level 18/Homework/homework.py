

def find_min_max(numbers):

    min_num = max_num = numbers[0]

    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num


nums = [8, 3, 15, 6, 1, 22, 4]
min_val, max_val = find_min_max(nums)
print(min_val)
print(max_val)