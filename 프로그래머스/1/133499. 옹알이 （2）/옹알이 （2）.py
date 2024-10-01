def solution(babbling):
    ans = 0
    init = {"aya", "ye", "woo", "ma"}

    for word in babbling:
        com = ""  #비교할 단어
        tmp = ""  #임시 저장할 단어

        for char in word:
            com += char

            #연속해서 같은 단어가 나왔을 때 반복문 탈출
            if com == tmp:
                break

            #4가지 단어가 포함 돼있을 때 현재 단어 임시 저장 후 비교단어 초기화
            if com in init:
                tmp = com
                com = ""

        #비교할 단어가 존재 하지 않을때 카운트
        if com == "":
            ans += 1

    return ans