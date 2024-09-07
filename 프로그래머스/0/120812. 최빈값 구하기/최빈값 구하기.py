def solution(array):
    
    tmp = set(array) #중복 제거한 집합
    max = 0
    
    for i in tmp:
        
        cnt = array.count(i) #각 원소의 개수 구하기
        
        if max < cnt: #가장 많은 개수의 원소 저장
            
            max = cnt
            ans = i
            
        elif max == cnt: #
            ans = -1
            
    return ans