
num = [1,34,554,7756,97574]

def sorter(num):
    return len(str(num))


print(sorted(num, key= sorter, reverse= True))