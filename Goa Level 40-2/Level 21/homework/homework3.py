
def has_uppercase(s):
    for char in s:
        if char.isupper():
            return True
    return False


print(has_uppercase("hello"))
print(has_uppercase("Hello"))
print(has_uppercase("123!@#"))
print(has_uppercase("abcD"))