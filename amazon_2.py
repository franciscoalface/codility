def solution(S):
    i = 1
    position = 0
    while i < len(S):
        open_b = S[:i].count('(')
        close_b = S[i:].count(')')
        if open_b == close_b:
            position = i
        i += 1
    if position == 0:
        position = len(S)
    return position

# def append_value(d, k):
#     a = list()
#     if k in d.keys():
#         a = d[k]
#     a.append(k)
#     return a
#
# def solution(A):
#     i = 0
#     j = len(A) - 1
#     result = count_left = count_right = 0
#     dict_left = dict_right = dict()
#     while i < len(A):
#         i += 1
#         j -= 1
#         if A[i] == '(':
#             count_left += 1
#         if A[j] == ')':
#             count_right += 1
#
#         if dict_left.keys(i):
#             dict_left[i].
#
#     return result


print(solution('(())'))
print(solution('(())))('))
print(solution('))'))
