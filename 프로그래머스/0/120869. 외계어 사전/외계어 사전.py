def solution(spell, dic):
    for i in dic:
        if set(spell).issubset(i):
            return 1
        
    return 2