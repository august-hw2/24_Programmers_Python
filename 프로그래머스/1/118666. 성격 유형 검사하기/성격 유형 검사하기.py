def solution(survey, choices):
    answer = ''
    dict_rcja = {'R': 0, 'C': 0, 'J': 0, 'A': 0}
    dict_tfmn = {'T': 0, 'F': 0, 'M': 0, 'N': 0}
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3} #choices에 따른 값

    # survey 요소 개수만큼 반복
    i = 0
    while i < len(survey):
        question = survey[i]
        if choices[i] in [1, 2, 3]: # 질문이 첫번째 문자에 속하는 경우
            if question[0] in dict_rcja:
                dict_rcja[question[0]] += score[choices[i]]
            elif question[0] in dict_tfmn:
                dict_tfmn[question[0]] += score[choices[i]]

        elif choices[i] in [5, 6, 7]: # 질문이 두번째 문자에 속하는 경우
            if question[1] in dict_rcja:
                dict_rcja[question[1]] += score[choices[i]]
            elif question[1] in dict_tfmn:
                dict_tfmn[question[1]] += score[choices[i]]
        else:
            pass
        i += 1

    list_rcja = list(dict_rcja.values())
    list_tfmn = list(dict_tfmn.values())

    # 값 비교 후 문자열 더하기
    for i in range(4):
        if list_rcja[i] > list_tfmn[i]:
            answer += list(dict_rcja.keys())[i]
        elif list_rcja[i] < list_tfmn[i]:
            answer += list(dict_tfmn.keys())[i]
        else: # 값이 동일한 경우, 사전순으로 비교 후 더하기
            tmp = [list(dict_rcja.keys())[i], list(dict_tfmn.keys())[i]]
            tmp = sorted(tmp)
            answer += tmp[0]

    return answer