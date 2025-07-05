
word = ["Luka", "kula", "kekqsi", "kalatburti", "kvercxi", "hello"]
def count(word):
    word.count("K")

print(sorted(word, key= count, reverse= False))