
def amoshali_khmovnebi(texti):
    khmovnebi = "აეიოუ"
    rezultati = ""
    for simvoli in texti:
        if simvoli.lower() not in khmovnebi.lower():
            rezultati += simvoli
    return rezultati


print(amoshali_khmovnebi("hidroeleqtrosadguri"))