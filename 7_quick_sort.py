#!/usr/bin/env python
import random
data = [i for i in range(1, 101)]
print 'origin:', data, '\n'
compute_count = 0

def partion(start, end):
    global compute_count
    if end - start <= 1:
        return -1
    left = start + 1
    right = end - 1
    # randomly pick one element as beacon and exchange it with the first element
    seed = random.randint(start, end - 1)
    tmp = data[start]
    data[start] = data[seed]
    data[seed] = tmp
    beacon = data[start]

    while left < right:
        compute_count += 1
        if data[left] <= beacon:
            left += 1
        if data[right] > beacon:
            right -= 1
        if left < right and data[left] > beacon and data[right] <= beacon:
            tmp = data[left]
            data[left] = data[right]
            data[right] = tmp
    res = left - 1 if data[left] > beacon else left
    # exchange with last smaller number
    tmp = data[start]
    data[start] = data[res]
    data[res] = tmp
    return res


def quick_sort(start, end):
    index = partion(start, end)
    if index != -1:
        quick_sort(start, index)
        quick_sort(index + 1, end)

quick_sort(0, len(data))
print data
print 'data length is', str(len(data)), 'compute count is', str(compute_count)
