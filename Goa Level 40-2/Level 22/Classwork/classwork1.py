

num = int(input("Enter a random number here: "))

def number_list(num):
    New_list = []
    while num >= 10:
        New_list.append(num)
        num = int(input("Enter a random number here: "))
    
    return New_list