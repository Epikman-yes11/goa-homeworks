
def amoshali_kenti_ricxvebi(sia):
    kenti_ricxvebi = []
    for i in range(1, len(sia), 2):
        elementi = sia[i]
        if isinstance(elementi, int) and elementi % 2 != 0:
            kenti_ricxvebi.append(elementi)
    return kenti_ricxvebi


s = [10, 3, 22, 7, 5, 8, 11, 9]
print(amoshali_kenti_ricxvebi(s)) 