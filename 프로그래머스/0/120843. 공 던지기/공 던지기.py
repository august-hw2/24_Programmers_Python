def solution(numbers, k):
    even = []
    odd = []

    if len(numbers)%2: #홀수일 때
        for i in range(0, len(numbers), 2):
            even.append(numbers[i])
        for i in range(1, len(numbers), 2):
            even.append(numbers[i])
        return even[k % len(even) - 1]

    else: #짝수일 때
        for i in numbers:
            if i%2:
                odd.append(i)

        return odd[k%len(odd)-1]