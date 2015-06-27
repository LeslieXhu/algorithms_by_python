#!/usr/bin/env python
data = [8, 6, 5, 9, 12, 14, 4, 7, 0, 13, 12, 5, 99, 33, 23, -1, 8]
print data, '\n'

for i in range(1, len(data)):
    key = data[i]
    for j in range(i, 0, -1):
        if data[j - 1] > key:
            data[j] = data[j - 1]
            if j == 1: j = 0
        else:
            break
    data[j] = key
    print data
