
def capitalize_sentence(sentence):
    words = sentence()
    capitalized_words = [word.capitalize() for word in words]
    result = " "(capitalized_words)
    return result


text = "gamarjoba bro"
output = capitalize_sentence(text)
print(output)