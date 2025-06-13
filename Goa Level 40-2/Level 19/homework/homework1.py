
def filter_strings(mixed_list):
    return [item for item in mixed_list]


data = [10, "hello", 3.14, True, "world","python"]
strings_only = filter_strings(data)
print(strings_only)