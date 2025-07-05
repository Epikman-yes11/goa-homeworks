
name = input("enter your name: ")

def func():
    xmovan = ""
    for i in name:
        if i not in "aeiou":
            xmovan += i
    return(xmovan)


print(func(name))