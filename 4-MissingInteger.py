def solution(arr):

    # Segregate the positive and non-positive numbers
    index = 0
    for i in range(len(arr)):
        if arr[i] < 1:
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
            index += 1

    # Find missing integer
    for x in range(len(arr)):
        if arr[x] <= 0:
            arr[x] = 0

    # Convert all existing number's indexes to negative
    for x in range(len(arr)):
        if arr[x] < len(arr):
            index = abs(arr[x])
            arr[index] = -arr[index]

    # Find first positive index and that's the answer
    index = 0
    while(index < len(arr)):
        if arr[index] > 0:
            return index
        index += 1

    return index

print(solution([3, 4, 1, -1]))
print(solution([1, 2, 0]))
