from itertools import combinations

def is_prime(a):

    if a == 0 or a == 1:
        return False
    else:
        for i in range(2, a//2+1):
            if a%i == 0:
                return False
        return True

def solution(nums):

    ans = 0
    cmb = list(combinations(nums, 3))
    for arr in cmb:
        if is_prime(sum(arr)):
            ans += 1

    return ans