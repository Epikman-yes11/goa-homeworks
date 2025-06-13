
def get_uppercase_names(names_list):
    uppercase_names = []
    for name in names_list:
        if name.isupper():
            uppercase_names.append(name)
    return uppercase_names

names = ["Giorgi", "NINO", "dato", "MAKA", "luka"]
result = get_uppercase_names(names)
print(result)  # ['NINO', 'MAKA']