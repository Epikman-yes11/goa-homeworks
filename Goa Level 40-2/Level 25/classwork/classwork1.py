


def count_G(user_word):
    return user_word.count('G')

user_list = ["Goa", "Gamer", "Brigade"]

print(sorted(user_list, key=count_G))