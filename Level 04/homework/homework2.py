

text = input("შეიყვანე სიტყვა: ")
number = int(input("შეიყვანე რიცხვი: "))

result = ''.join([char * number for char in text])

print("შედეგი:", result)