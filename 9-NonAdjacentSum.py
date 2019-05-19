def recursive_solution(arr):
    if (arr == []):
        return 0
    return max(arr[0] + recursive_solution(arr[2:]), recursive_solution(arr[1:]))

def iterative_solution(arr):
    if not arr or arr == []:
        return 0
    elif len(arr) <= 2:
        return max(arr)
    result = [arr[0], arr[1], arr[2] + arr[0]]
    for i in range(3, len(arr)):
        result.append(arr[i] + max(result[i-2], result[i-3]))
    return max(result[-1], result[-2])


assert recursive_solution([2, 4, 6, 2, 5]) == 13
assert recursive_solution([5, 1, 1, 5]) == 10
