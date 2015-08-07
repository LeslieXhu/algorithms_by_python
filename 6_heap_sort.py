#!/usr/bin/env python
data = [8, 6, 5, 9, 12, 14, 4, 7, 0, 13, 12, 5, 99, 33, 23, -1, 8]
length = len(data)
print 'origin:', data, '\n'

def heapify(i):
    """max heapify array, always assume chile level has been heapified."""
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    if left < length and data[left] > data[largest]:
        largest = left
    if right < length and data[right] > data[largest]:
        largest = right
    if not largest == i:
        tmp = data[i]
        data[i] = data[largest]
        data[largest] = tmp
        heapify(largest)
# build the whole max heapified array
# after that the first element must be largest one
for index in range(length / 2 - 1, -1, -1):
    heapify(index)
print data, '\n'
# exchange the first element with the last one
# reduce the origin array length
# then heapify again to make sure the first one is the largest one
indexs = range(length - 1, 0, -1)
for index in indexs:
    tmp = data[index]
    data[index] = data[0]
    data[0] = tmp
    length -= 1
    heapify(0)
    print data, '\n'

