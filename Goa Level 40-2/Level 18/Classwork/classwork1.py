
def average_over_50(numbers):
    total = 0
    count = 0

    for num in numbers:
        if num > 50:
            total += num
            count += 1

    return total / count if count != 0 else None


nums = [10, 55, 70, 32, 90, 45, 51]
result = average_over_50(nums)
print(result)