

def even_numbers_at_even_indices(numbers):
    filtered = []
    for index, num in numbers:
        if index % 2 == 0 and num % 2 == 0:
            filtered.append(num)
    
    if filtered:
        average = sum(filtered) / len(filtered)
        return average
    else:
        return None

nums = [2, 5, 4, 8, 6, 9, 10]
result = even_numbers_at_even_indices(nums)
print(result)