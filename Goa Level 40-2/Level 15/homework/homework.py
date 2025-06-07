
def amoshali_kent_indexebi(texti):
    rezultati = ""
    for i in range(len(texti)):
        if i % 2 == 0:
            rezultati += texti[i]
    return rezultati

print(amoshali_kent_indexebi("example"))
print(amoshali_kent_indexebi("abcdefg"))