
def extract_strings(data):
    string_list = []
    for item in data:
        if isinstance(item):
            string_list.append(item)

mixed_list = [123, "hello", True, "world", 45.6,"python"]
result = extract_strings(mixed_list)
print(result)