def solution(chicken):
    
    res = 0

    while chicken >= 10:
        #몫과 나머지 연산
        share = chicken // 10
        remain = chicken % 10
        #몫만 리턴할 결과값에 덧셈
        res += share
        #위에서 연산한 몫과 나머지를 새로 주문 가능한 치킨 수로 저장
        chicken = share + remain

    return res