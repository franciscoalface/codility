# def solution(a):
#     min_diff = sum(a)
#     for i in range(1, len(a)):
#         x = a[:i]
#         y = a[i:]
#         print(x, y)
#         diff = abs(sum(x) - sum(y))
#         if min_diff > diff:
#             min_diff = diff
#     return min_diff


def solution(a):
    min_diff = len(a)
    i = 1
    while i < len(a):
        x = a[:i]
        y = a[i:]
        print(x, y)
        diff = abs(sum(x) - sum(y))
        if min_diff > diff or min_diff == len(a):
            min_diff = diff
        i += 1
    return min_diff


print(solution([3, 1, 2, 4, 3]))
print(solution([1, 2, 3, 4, 2]))
print(solution([-1000, 1000]))
