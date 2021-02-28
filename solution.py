

def solution(M, F):
    counter = 0
    iM = int(M)
    iF = int(F)

    equal = iM == iF and iM > 1
    while (iM > 1 or iF > 1) and not equal:
        if iM > iF:
            iM -= iF
        else:
            iF -= iM
        counter += 1
        equal = iM == iF and iM > 1

    result = "impossible"
    if not equal:
        result = str(counter)
    return result