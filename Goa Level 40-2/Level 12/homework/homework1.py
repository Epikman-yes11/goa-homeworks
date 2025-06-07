
def int_eligebi(sia):
    result = []
    for elementi in sia:
        if isinstance(elementi):
            result.append(elementi)
    return result


mixed_list = [1, "ტექსტი", 3.14, True, 42, None, -7]

print(int_eligebi(mixed_list))