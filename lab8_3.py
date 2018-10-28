#!/usr/bin/env python3
import sys
import statistics

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

def ser(lst):
    a = (sum(lst))/(len(lst))
    return a

lst = [1,2,3,6,10,3]
print('list is [1,2,3,6,10,3]')
print('Da median of it is: ', median(lst) )
print('Da serednje value is: ',ser(lst))
