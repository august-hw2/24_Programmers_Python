#요소 삭제 후 새 배열 만들기
def new_arr(a, new_s):

    rm_set = set()
    rm_set.add(a)

    tmp = [i for i in new_s if i not in rm_set]

    return tmp

def solution(N, stages):

    fail_arr = []
    for j in range(1, N+1):
        if len(stages) == 0:
            fail_arr.append(0)
        else:
            fail_arr.append(stages.count(j)/len(stages))
            stages = new_arr(j, stages)

    sort_fail_arr = sorted(fail_arr, reverse=True)
    ans = []

    for a in sort_fail_arr:
        idx = fail_arr.index(a)
        ans.append(idx+1)
        fail_arr[idx] = -1

    return ans