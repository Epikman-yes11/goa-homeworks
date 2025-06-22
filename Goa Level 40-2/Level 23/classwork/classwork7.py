
def process_strings(string_list):
    odd_letters = []
    even_uppercase = []

    for s in string_list:
        if len(s) % 2 == 1:
            odd_letters.append(s)
        else:
            even_uppercase.append(s.upper())

    return odd_letters, even_uppercase


words = ["cat", "moon", "sun", "sky", "code", "hello"]
odd, even = process_strings(words)

print("კენტი:", odd)
print("ლუწი (დიდი ასოებით):", even)