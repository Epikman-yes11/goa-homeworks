
name = ["Davit", "shota", "demetre", "Mate"]
list = []

for i in name:
    for index in range(len(i)):
        if index % 2 != 0:
            list.append(i[index])

print(sorted(list))
