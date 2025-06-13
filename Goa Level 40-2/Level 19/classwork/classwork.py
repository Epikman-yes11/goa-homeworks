

def average_even_up_to(n):
    if n < 2:
        return None

    sum_even = 0
    count = 0

    for num in range(2, 1, 2):
        sum_even += num
        count += 1

    return sum_even / count

user_input = int(input("შეიყვანეთ რიცხვი: "))
result = average_even_up_to(user_input)
print(result)