
def sum_odd_squares(n):
    total = 0
    for num in range(1, n + 1):
        if num % 2 != 0: 
            total += num ** 2
    return total


user_input = input("შეიყვანე რიცხვი: ")
result = sum_odd_squares(user_input)

print(result)