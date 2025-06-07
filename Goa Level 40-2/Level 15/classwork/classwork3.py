

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


nums = list(range(1, 21))
evens = filter_even_numbers(nums)
print(evens)