
my_list = [10, 20, 30, 40, 50, 60, 70]

number = int(input("შეიყვანე რიცხვი: "))

if 0 <= number < len(my_list):
    print(my_list[number:])
else:
    print("რიცხვი არასწორია!")