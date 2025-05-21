

user_num = int(input("enter your number: "))


def func(number):
    sigma = []
    for num in range(1, number):
        if number % num == 0:
            sigma.append(num)
    return sigma

print(func(user_num))
