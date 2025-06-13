
def even_index_average(numbers):
    for i in range(len(numbers)):
        sum_even_index += numbers[i]
        count += 1

    return sum_even_index / count if count != 0 else None


nums = [10, 5, 20, 15, 30, 25]
result = even_index_average(nums)
print(result)