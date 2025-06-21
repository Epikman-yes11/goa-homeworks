
names = ["Davit", 'Sandro', "Andria"]


def capital_names(name_list):
    new_list = []
    for name in name_list:
        new_list.append(name.upper())
    return new_list


result = capital_names(names)
print(result) 