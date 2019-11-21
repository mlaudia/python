from math import gcd

def reduction(frac):
    div = gcd(frac[0], frac[1])
    if(div != 0):
        frac[0] = frac[0]/div
        frac[1] = frac[1]/div
    return frac

def add_frac(frac1, frac2): # frac1 + frac2
    if(frac1[1] == 0 or frac2[1] == 0):
        return("Denominator can't be equal to 0")
    x = [frac1[0]*frac2[1] + frac2[0]*frac1[1], frac1[1]*frac2[1]]
    return reduction(x)
    

def sub_frac(frac1, frac2):        # frac1 - frac2
    if(frac1[1] == 0 or frac2[1] == 0):
        return("Denominator can't be equal to 0")
    x =  [frac1[0]*frac2[1] - frac2[0]*frac1[1], frac1[1]*frac2[1]]
    return reduction(x)

def mul_frac(frac1, frac2):        # frac1 * frac2
    if(frac1[1] == 0 or frac2[1] == 0):
        return("Denominator can't be equal to 0")
    x = [frac1[0]*frac2[0], frac1[1]*frac2[1]]
    return reduction(x)

def div_frac(frac1, frac2):        # frac1 / frac2
    if(frac1[1] == 0 or frac2[1] == 0):
        return("Denominator can't be equal to 0")
    x = [frac1[0]*frac2[1], frac1[1]*frac2[0]]
    return reduction(x)

def is_positive(frac):             # bool, czy dodatni
    if(frac[1] == 0):
        return("Denominator can't be equal to 0")
    return ((frac[0] >= 0 and frac[1] >= 0) or (frac[0] < 0 and frac[1] < 0))

def is_zero(frac):                 # bool, typu [0, x]
    if(frac[1] == 0):
        return("Denominator can't be equal to 0")
    return (frac[0] == 0)

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    frac1 = reduction(frac1)
    frac2 = reduction(frac2)
    if(frac1[1] == 0 or frac2[1] == 0):
        return("Denominator can't be equal to 0")
    if(frac2float(frac1) < frac2float(frac2)):
        return -1
    elif(frac2float(frac1) > frac2float(frac2)):
        return 1
    else:
        return 0


def frac2float(frac):              # konwersja do float
    if(frac[1] == 0):
        return("Denominator can't be equal to 0")
    return(frac[0]/frac[1])