def recursive_solution(arr):
    if (arr == []):
        return 0
    return max(arr[0] + recursive_solution(arr[2:]), recursive_solution(arr[1:]))

def iterative_solution(arr):
    index = 0
    answer = 0
    while (index + 1) < len(arr):
        if arr[index] >= arr[index+1]:
            answer += arr[index]
            index += 2
        else:
            answer += arr[index+1]
            index += 3
    return answer
        

assert recursive_solution([2, 4, 6, 2, 5]) == 13
assert recursive_solution([5, 1, 1, 5]) == 10