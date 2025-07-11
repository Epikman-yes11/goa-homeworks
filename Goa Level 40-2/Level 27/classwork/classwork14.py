
#19)შექმენი ცვლადი სადაც შეინახავ შენ პაროლს,შემდეგ 
# მომხმარებელს შემოატანინე პაროლკსანამ მომხმარებელი სწორად არშემოიყვანს
#  პაროლს იქამდე გაუმეორე რომ შემოიყვანოს თავიდან პაროლი

password = input("enter password: ")

correct_password = "beraia"

while True:
    if password == correct_password:
        print("your password is right")
        break
    else:
        print("your password is wrong")
