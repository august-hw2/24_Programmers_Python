import re

def solution(babbling):
    
    res = []

    for i in range(len(babbling)):
        res.append(re.split("aya|ye|woo|ma", babbling[i]))

    for j in range(len(res)):
        res[j] = ''.join(res[j]).split()

    return res.count([])