

def faktoriali(n):
    if n < 0:
        return "ფაქტორიალ"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    


print(faktoriali(5))
print(faktoriali(0))
print(faktoriali(-3)) 