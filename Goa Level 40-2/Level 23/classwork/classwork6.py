

def func(list):
    new_list = []
    for i in range(len(list)):
        if i % 2 != 0:
            new_list.append(list[i])
    return new_list

print(func([1,2,3,4,5,6,7]))