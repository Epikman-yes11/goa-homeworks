

my_name = "დავით"
my_age = 25

user_name = input("შეიყვანე შენი სახელი: ")
user_age = int(input("შეიყვანე შენი ასაკი: "))

if user_age > 18:
    if user_name.lower() == my_name.lower():
        print("we have same names and we are adults")
    else:
        print("we do not have same names but we are adults")

elif user_age < 18:
    print("we do not have same names and we are not adults")
else:
    print("შენ ხარ ზუსტად 18 წლის")