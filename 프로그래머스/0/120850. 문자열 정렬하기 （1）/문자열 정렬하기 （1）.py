def solution(my_string):
    my_string = list(my_string)
    return sorted([int(i) for i in my_string if i.isdigit()])