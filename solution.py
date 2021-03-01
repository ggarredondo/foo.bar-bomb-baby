

def solution(M, F):
    generations = -1
    iM = int(M)
    iF = int(F)

    while iM > 0 and iF > 0:
        if iM > iF:
            division = iM // iF
            iM %= iF
        else:
            division = iF // iM
            iF %= iM
        generations += division
    invalid = (iM == 0 and iF > 1) or (iM > 1 and iF == 0)

    result = str(generations)
    if invalid:
        result = "impossible"
    return result