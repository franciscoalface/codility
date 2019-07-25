def solution(a):
    i = 1
    pos = 0
    b = set(a)
    while i <= len(a) + 1:
        if i not in b:
            return i
        i += 1
        pos += 1


print(solution([2, 3, 1, 5]))
