def je_deljivo_s_katerim_od(n, seznam):
    if seznam == []:
        return False
    if n % seznam[0] == 0:
        return True
    if not(n % seznam[0] == 0):
        return je_deljivo_s_katerim_od(n, seznam[1:])
    else:
        return False

def prastevila_do(n):
    if n < 2:
        return []
    else:
        manjsa_prastevila = prastevila_do(n - 1)
        if je_deljivo_s_katerim_od(n, manjsa_prastevila):
            return(manjsa_prastevila)
        else:
            return manjsa_prastevila + [n]