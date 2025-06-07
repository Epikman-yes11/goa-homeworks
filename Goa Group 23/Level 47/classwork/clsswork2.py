

car={
    "brand1":"ford",
    "brand2":"toyota",
    "brand3":"mercedes"
}



try:
    x = car.values(4)

except ValueError:
    print("no numbers in values")

finally:
    x = car.values()

print(x)