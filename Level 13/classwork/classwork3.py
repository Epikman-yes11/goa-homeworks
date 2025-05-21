

def sum_numbers_in_list(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
    return total