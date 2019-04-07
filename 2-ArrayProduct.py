def solution(arr):
    n = len(arr)
    answer = [1] * n
    left_multiplier = arr[0]
    for i in range(1, n):
        answer[i] = left_multiplier * answer[i]
        left_multiplier = left_multiplier * arr[i]
    right_multiplier = arr[-1]
    for i in range(n-2, -1, -1):
        answer[i] = right_multiplier * answer[i]
        right_multiplier = right_multiplier * arr[i]
    return answer

assert solution([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution([3, 2, 1]) == [2, 3, 6]
