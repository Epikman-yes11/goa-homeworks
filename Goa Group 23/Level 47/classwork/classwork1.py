

fruits = ["apple","banana","cherry"]

try:
   print(fruits[10])


except IndexError:
   print("there arent 10 fruits")


finally:
   print("3 fruits")