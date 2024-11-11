# 전체 면적 = y개수 + b개수 = 가로 * 세로
    # y개수 = (가로-2)*(세로-2)
    # b개수 = 전체 면적 - y개수

def solution(brown, yellow):
    
    s = brown + yellow

    #전체 면적에서 가로, 세로 길이 경우의 수로 반복문 진행
    for width in range(s-1, 0, -1):
        if s%width == 0:
            height = s/width
            y = (width-2)*(height-2)
            b = s-y
            
            if y == yellow and b == brown:
                return [width, height]