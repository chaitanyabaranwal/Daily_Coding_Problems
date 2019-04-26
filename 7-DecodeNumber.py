def solution(number):
    result = [0] * len(number)
    result[0] = 1
    for x in range(1, len(number)):
        if number[x] == '0':
            result[x] = result[x-1]
        elif int(number[x-1] + number[x]) > 26:
            result[x] = result[x-1]
        else:
            result[x] = 1 + result[x-1]

    return result[-1]

assert solution('111') == 3
assert solution('251') == 2
assert solution('271') == 1
assert solution('1') == 1
