def solution(my_string):
    return sum(int(my_string[i]) for i in range(len(list(my_string))) if my_string[i].isdigit())