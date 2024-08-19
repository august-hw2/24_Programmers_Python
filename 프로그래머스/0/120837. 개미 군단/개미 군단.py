def solution(hp):
    res = int(hp/5)
    
    hp -= 5*int(hp/5)
    
    if hp >= 3:
        res += int(hp/3)
        hp -= 3*int(hp/3)
    
    if hp >= 1:
        res += int(hp/1)
        
    return res
        