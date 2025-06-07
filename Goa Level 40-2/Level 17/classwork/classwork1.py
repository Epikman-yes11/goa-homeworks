
def filter_capitalized(words):
    result = []
    if words[0].upper:
            result.append(words)
    return result


words_list = ["kaxi", "ana", "Aleqsandre", "ia", "Giorgi", "Iamze", "beqa"]
capitalize = filter_capitalized(words_list)

print(capitalize)