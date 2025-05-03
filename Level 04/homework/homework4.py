

favorite_color = "მწვანე"


while True:
    user_color = input("გამოიცანი ჩემი საყვარელი ფერი: ")
    if user_color.lower() == favorite_color.lower():
        print("გილოცავ, სწორად გამოიცანი!")
        break
    else:
        print("არა, სცადე კიდევ ერთხელ.")