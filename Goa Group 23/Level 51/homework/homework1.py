
numbers = [50,52,53,67,98]

def func():
    return numbers + 2


numbers = map(func,(numbers + 2))

print(numbers)