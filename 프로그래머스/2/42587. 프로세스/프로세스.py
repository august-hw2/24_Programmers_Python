def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    #큐 구현 ([0] - 인덱스값, [1] - 우선순위값)
    
    answer = 0
    
    while True:
        
        cur = queue.pop(0)
        
        if any(cur[1] < q[1] for q in queue): 
            #현재 큐보다 남은 대기 큐 중에 더 큰 우선순위 값을 가진 큐가 있으면
            queue.append(cur)
        else:
            answer += 1
            
            if cur[0] == location: 
                #현재 큐의 인덱스 값 == 기존 위치 값 (실행 큐로 넘어온 순간)
                return answer