from __future__ import print_function


def partition1(a, left, right):
    """With nested while loops"""
    pivot = a[left]
    while left <= right:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if left <= right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
    return left


def partition2(a, left, right):
    """Without nested while loops"""
    pivot = a[left]
    while left <= right:
        if a[left] >= pivot and a[right] <= pivot:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        else:
            if a[left] < pivot:
                left += 1
            if a[right] > pivot:
                right -= 1
    return left


def partition3(a, left, right):
    """CLRS variant"""
    pivot = a[right]
    i = left
    for j in range(left, right):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


def quicksort1(a, left, right):
    p = partition1(a, left, right)
    if left < p - 1:
        quicksort1(a, left, p - 1)
    if p < right:
        # Inclusive pivot `p` to the right part
        quicksort1(a, p, right)


def quicksort2(a, left, right):
    p = partition2(a, left, right)
    if left < p - 1:
        quicksort2(a, left, p - 1)
    if p < right:
        # Inclusive pivot `p` to the right part
        quicksort2(a, p, right)


def quicksort3(a, left, right):
    if left < right:
        p = partition3(a, left, right)
        quicksort3(a, left, p - 1)
        quicksort3(a, p + 1, right)


def merge(a, left, mid, right):
    t = a[:]
    left_end = mid
    right_start = mid + 1
    p = left
    while left <= left_end and right_start <= right:
        if t[left] <= t[right_start]:
            a[p] = t[left]
            left += 1
        else:
            a[p] = t[right_start]
            right_start += 1
        p += 1
    # Only copy the remaining elements in the left part
    # Since those in the right part are already there
    while left <= left_end:
        a[p] = t[left]
        p += 1
        left += 1


def mergesort(a, left, right):
    if left < right:
        mid = (left + right) / 2
        mergesort(a, left, mid)
        mergesort(a, mid + 1, right)
        merge(a, left, mid, right)


def _test():
    pass


def _print():
    #a1 = []
    a2 = [1]
    a3 = [1, 2]
    a4 = [2, 1]
    a5 = [1, 3, 2]
    a6 = [3, 4, 1, 2]
    a7 = [5, 4, 3, 2, 1]
    _as = locals()
    for _a in _as:
        #print(_as[_a])
        mergesort(_as[_a], 0, len(_as[_a]) - 1)
        print(_a, _as[_a])


if __name__ == '__main__':
    _test()
    _print()
