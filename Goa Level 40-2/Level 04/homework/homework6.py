


correct_password = "1234"

# მაქსიმუმ 3 ცდა
attempts = 3

while attempts > 0:
    user_input = input("შეიყვანე პაროლი: ")
    if user_input == correct_password:
        print("პაროლი სწორია. წვდომა მიღებულია!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("პაროლი არასწორია. დაგრჩა რამოდენიმე ცდა.")
        else:
            print("ცდების ლიმიტი ამოიწურა. წვდომა აკრძალულია.")