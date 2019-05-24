# coding=utf-8
"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
    A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
    |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution(a):
    def calculate_difference(lst, slice_int, min_diff):
        if slice_int == len(lst):
            return min_diff

        diff = abs(sum(lst[:slice_int]) - sum(lst[slice_int:]))
        if min_diff > diff or min_diff == 0:
            min_diff = diff
        return calculate_difference(lst, slice_int + 1, min_diff)

    return calculate_difference(a, 1, 0)


def solution2(a):
    i = 1

    def calculate(lst, iterator, result):
        if iterator == len(lst):
            return min(result)

        result.append(abs(sum(lst) - sum(lst[:iterator]) * 2))
        return calculate(lst, iterator + 1, result)

    return calculate(a, i, [])


def solution3(a):
    total_sum = sum(a)
    i = 1
    first = True
    min_counter = 0
    while i < len(a):
        b = sum(a[:i])
        current_min = abs(total_sum - (b + b))
        if current_min < min_counter or first:
            first = False
            min_counter = current_min
        i += 1
    return min_counter


def solution4(a):
    head = a[0]
    tail = sum(a[1:])
    min_diff = abs(head - tail)
    i = 1

    while i < len(a) - 1:
        head += a[i]
        tail -= a[i]
        if abs(head - tail) < min_diff:
            min_diff = abs(head - tail)
        i += 1
    return min_diff


print(solution([3, 1, 2, 4, 3]))
print(solution([-1000, 1000]))
print(solution4([3, 1, 2, 4, 3]))
print(solution4([-1000, 1000]))
