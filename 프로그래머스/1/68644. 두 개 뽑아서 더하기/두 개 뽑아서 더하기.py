def solution(numbers):
    ans = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] not in ans:
                ans.append(numbers[i]+numbers[j])

    return sorted(ans)