
def shemotanili_sityvebi():
    sityvebi = []
    while True:
        sityva = input("შემოიტანე სიტყვა (ან შეიყვანე 'საკმარისია' დასასრულებლად): ")
        if sityva == "საკმარისია":
            break
        sityvebi.append(sityva)
    return sityvebi

shemotani = shemotanili_sityvebi()
print(shemotani)