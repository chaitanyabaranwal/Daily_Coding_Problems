def twoSum(arr, target):

    seen = dict()

    for i in range(len(arr)):
        if (target - arr[i]) in seen:
            return [i, seen[target-arr[i]]]
        else:
            seen[arr[i]] = i

    return []

print(twoSum([10, 15, 3, 7], 17))
