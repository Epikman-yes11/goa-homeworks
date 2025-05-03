
my_name = "დავით"


full_name = input("შეიყვანე სახელი და გვარი: ")

user_name = full_name.split()[0]

if user_name.lower() == my_name.lower():
    print("we have same name")
else:
    print("we do not have same names")