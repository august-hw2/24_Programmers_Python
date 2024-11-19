def solution(phone_book):

    # 해시 맵 만들기
    hash_map = {}
    for phone_num in phone_book:
        hash_map[phone_num] = 1

    # 접두어 추가해가며 확인 (단, 본인 스스로 비교는 제외)
    for phone_num in phone_book:
        t = ""
        for num in phone_num:
            t += num
            if t in hash_map and t != phone_num:
                return False

    return True