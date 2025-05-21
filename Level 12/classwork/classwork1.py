
user_input = input("enter your string: ")


def count():
    string = string.lower()
    count_a = 0
    for i in string:
        if i == "a":
            count += 1
    return count

print(count(user_input))