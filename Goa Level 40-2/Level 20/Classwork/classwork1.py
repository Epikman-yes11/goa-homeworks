


def get_uppercase_name(name):
    uppercase_name = []
    for name in names_list:
        if name.isupper():
            uppercase_name.append(name)
    return uppercase_name



names_list = ["David", "LEVAN", "ANDRIA", "Shota"]
result = get_uppercase_name(names_list)
print(result)