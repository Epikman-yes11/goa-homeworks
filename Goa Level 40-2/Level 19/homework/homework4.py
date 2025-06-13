
def even_index_letters(word):
    result = ""
    for i in range(0, len(word), 2):
        result += word[i]
    return result


user_input = input("შეიყვანეთ სიტყვა: ")
output = even_index_letters(user_input)
print(output)