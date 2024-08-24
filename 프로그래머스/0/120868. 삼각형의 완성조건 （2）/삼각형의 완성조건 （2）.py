def solution(sides):
    return 2*min(sides)-1
    '''
    sides에서 a > b일 때
    
    1) a+b > c 
       a+b > c > a 여야 한다.
       정리하면, 
       b-1 > c > 0 이므로 (b-1)개
    
    2) b+c > a
       b+c > a > c 여야 한다.
       정리하면, 
       b-1 > a > 0 이므로 (b-1)개
    
    3) a = c
       3번의 경우는 1개
       
       => (b-1) + (b-1) + 1 = (2b-1)개
    
    '''