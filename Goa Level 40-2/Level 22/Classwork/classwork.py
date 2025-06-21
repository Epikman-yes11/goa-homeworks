

def vowels(name):
    res = []
    vowel = "aeiou"
    for i in name:
        if i in vowel:
            res.append(i)
    return res, len(res)
print(vowels("Davit"))