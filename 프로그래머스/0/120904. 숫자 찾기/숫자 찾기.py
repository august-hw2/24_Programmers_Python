def solution(num, k):
    num = str(num)
    k = str(k)
    
    return num.find(k)+1 if num.find(k) != -1 else -1