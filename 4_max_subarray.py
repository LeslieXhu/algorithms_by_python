#!/usr/bin/env python
"""Find a sub array which has the max sum"""
orig_data = [13, -3, -25, 20, -3, -16, -23, 18, 20, -71, 12, -5, -22, 15, -4, 7, 39]
print orig_data, '\n'

def find_max_subarray(start, end):
    # if the target array length is 1, return itself.
    if start + 1 == end:
        return start, end, orig_data[start]
    # split array into 2 parts, and process them recursively.
    mid = (start + end) / 2
    left_start, left_end, left_max = find_max_subarray(start, mid)
    right_start, right_end, right_max = find_max_subarray(mid, end)

    # the max subarray may crossing the middle
    # so we seek max subarray start from middle to left and right
    # then the sum of both sides is the max subarray acrossing middle
    mid_left_cur = orig_data[mid - 1]
    mid_left_max = mid_left_cur
    mid_start = mid - 1;
    for index in range(mid - 2, start - 1, -1):
        mid_left_cur += orig_data[index]
        if mid_left_cur > mid_left_max:
            mid_left_max = mid_left_cur
            mid_start = index

    mid_right_cur = orig_data[mid]
    mid_right_max = mid_right_cur
    mid_end = mid
    for index in range(mid + 1, end):
        mid_right_cur += orig_data[index]
        if mid_right_cur > mid_right_max:
            mid_right_max = mid_right_cur
            mid_end = index
    mid_end += 1 # move to next as end
    mid_max = mid_right_max + mid_left_max

    # compare 3 results and choose the max one.
    res_max = 0
    res_start = 0
    res_end = 0
    if left_max > mid_max and left_max > right_max:
        res_start, res_end, res_max = left_start, left_end, left_max
    if mid_max > left_max and mid_max > right_max:
        res_start, res_end, res_max = mid_start, mid_end, mid_max
    if right_max > mid_max and right_max > left_max:
        res_start, res_end, res_max = right_start, right_end, right_max
    print orig_data[start:end]
    print 'max subarray:', str(res_start), str(res_end), str(res_max)
    return res_start, res_end, res_max

find_max_subarray(0, len(orig_data))
