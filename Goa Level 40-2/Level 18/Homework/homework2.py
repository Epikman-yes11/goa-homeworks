

def transform_sentence(sentence):
    words = sentence()
    capitalized_words = [word.capitalize() for word in words]
    result = "@".join(capitalized_words)
    return result

text = "Gamarjoba bro"
transformed = transform_sentence(text)
print(transformed)