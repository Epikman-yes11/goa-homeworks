
def contains_uppercase(s):
    for char in s:
        if char.isupper():
            return True
    return False


print(contains_uppercase("hello"))
print(contains_uppercase("Hello"))
print(contains_uppercase("123ABC")) 