
#22) შექმენით ფუნქცია რომელიც აბრუნებს სტრინგში ხმოვნების რაოდენობას

word = "hello"

def func():
    count = 0
    xmovan = "aeiou"
    for i in word:
        if i == xmovan:
            count += 1
    return count


print(func)