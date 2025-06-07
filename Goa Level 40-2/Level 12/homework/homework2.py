

def fesvis_amogeba(ricxvi):
    if ricxvi < 0:
        return "უარყოფითი რიცხვიდან ფესვი არ ამოდის"
    else:
        return "ამოდის ფესვი"
    
print(fesvis_amogeba(25))
print(fesvis_amogeba(-9))