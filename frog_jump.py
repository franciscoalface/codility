def solution(x, y, d):
    result = (y - x) / d
    if result > int(result):
        return int(result) + 1
    return int(result)


print(solution(10, 85, 30))
print(solution(10, 10, 30))
print(solution(10, 20, 1))
print(solution(2, 11, 3))
print(solution(3, 50, 8))

