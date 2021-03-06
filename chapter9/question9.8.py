from __future__ import print_function

"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5
cents) and pennies (1 cent), write code to calculate the number of ways of
representing n cents.
"""


def make_change(n, changes):
    """
    `changes` is a list of integers
    """
    if not changes:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (make_change(n - changes[-1], changes)
                + make_change(n, changes[:-1]))


def make_change2_aux(n, changes, m, t):
    """Top-Down DP"""
    if m < 0:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    elif t[n][m] != 0:
        return t[n][m]
    else:
        t[n][m] = (make_change2_aux(n - changes[m], changes, m, t)
                   + make_change2_aux(n, changes, m - 1, t))
        return t[n][m]


def make_change2(n, changes):
    t = [[0 for i in changes] for i in range(n + 1)]
    return make_change2_aux(n, changes, len(changes) - 1, t)


def make_change3(n, changes):
    """Bottom-Up DP"""
    # t[i][j] means number of representing ways when using first j + 1 coins
    # (coins[0] through coins[j]) to make i
    t = [[0 for i in changes] for i in range(n + 1)]
    m = len(changes)
    for j in range(m):
        t[0][j] = 1
    for i in range(1, n + 1):
        for j in range(m):
            x = y = 0
            if i - changes[j] >= 0:
                x = t[i - changes[j]][j]
            if j - 1 >= 0:
                y = t[i][j - 1]
            t[i][j] = x + y
    return t[n][m - 1]


def make_change4(n, changes):
    m = len(changes)
    # t[i][j] means number of ways when using first j coins to make i
    t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for j in range(m + 1):
        t[0][j] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = 0
            if i - changes[j - 1] >= 0:
                x = t[i - changes[j - 1]][j]
            t[i][j] = t[i][j - 1] + x
    return t[n][m]


def _test():
    pass


def _print():
    c1 = [1, 5, 10, 25]
    n1 = 500
    r1 = make_change(n1, c1)
    print(r1)
    r2 = make_change2(n1, c1)
    print(r2)
    r3 = make_change3(n1, c1)
    print(r3)
    r4 = make_change4(n1, c1)
    print(r4)


if __name__ == '__main__':
    _test()
    _print()
