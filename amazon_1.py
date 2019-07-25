def solution(A):
    result = 0
    for x in A:
        if 9 < abs(x) < 100:
            result += x
    return result


print(solution([1, 1000, 80, -91]))
print(solution([47, 1900, 1, 90, 45]))
print(solution([-13, 1900, 1, 100, 45]))
