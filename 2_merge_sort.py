#!/usr/bin/env python
import sys
orig_data = [8, 6, 5, 9, 12, 14, 4, 7, 0, 13, 12, 5, 99, 33, 23, -1, 8]
print orig_data, '\n'


def merge(data, start, middle, end):
    res = []
    i1, i2 = start, middle
    while i1 < middle and i2 < end:
        if data[i1] < data[i2]:
            res.append(data[i1])
            i1 += 1
        else:
            res.append(data[i2])
            i2 +=1
    if i1 != middle:
        res.extend(data[i1:middle])
    else:
        res.extend(data[i2:end])
    data[start:end] = res

def merge_sort(data, start, end):
    if start + 1 < end:
        middle = (start + end) / 2
        merge_sort(data, start, middle)
        merge_sort(data, middle, end)
        merge(data, start, middle, end)
        print data[start:end]

merge_sort(orig_data, 0, len(orig_data))
