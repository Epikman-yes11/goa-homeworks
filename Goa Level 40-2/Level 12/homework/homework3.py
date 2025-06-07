

def shebrunebuli_tirebit(teqsti):
    shebrunebuli = ""
    for aso in teqsti:
        shebrunebuli = aso + shebrunebuli
    return "-".join(shebrunebuli)

print(shebrunebuli_tirebit("hello"))