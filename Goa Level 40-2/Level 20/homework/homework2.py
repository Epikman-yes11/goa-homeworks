
user_input = int(input("შეიყვანეთ მთელი რიცხვი: "))

even_sum = 0
odd_count = 0

for num in range(1, user_input + 1):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_count += 1


average = (even_sum + odd_count) / 2


print(even_sum)
print(odd_count)
print(average)