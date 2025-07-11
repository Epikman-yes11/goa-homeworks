

#4)შექმენით სია სადაც შეიყვანთ განსხვავებული მონაცემთთა ტიპის ელემენტებს,თქვენი
#დავალებაა ინტეჯერები ჩაამატო ერთ ახალ სიაშ და სტრინგები ჩაამატო სხვა ახალ სიაში

list = ["hello", 12, "World", 24, "Hi", 64]


def func():
    integer = []
    string = []
    for i in list:
        if i != str:
            integer.append(i)
    else:
        if i != int:
           string.append(i)

print(func)