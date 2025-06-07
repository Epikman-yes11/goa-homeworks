
def martvis_mowmoba(saxeli, asaki):
    chemi_saxeli = "გიორგი"
    if asaki > 18 and saxeli == chemi_saxeli:
        return "თქვენ წარმატებით აიღეთ მართვის მოწმობა"
    else:
        return "თქვენ ჩაიჭერით"
    
print(martvis_mowmoba(20))
print(martvis_mowmoba(22)) 