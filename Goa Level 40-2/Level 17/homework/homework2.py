

def find_max(numbers):
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    return max_number


nums = [3, 11, 7, 2, 25, 10]
print(find_max(nums))