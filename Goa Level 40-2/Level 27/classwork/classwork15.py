
#21) დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.

num = [1,3,4,24,67,43,79]

def bigger_than10(nums):
    count = 0
    for num in nums:
        if num > 10:
            count += 1
    return count