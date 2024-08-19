import re

def solution(my_string):
    my_string = re.sub("(a|e|i|o|u)", "", my_string)
    return my_string