#!/usr/bin/env python3
import statistics

def selection_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)): 		#Позначимо найменший елемент
        idxMin = i
        for j in range(i+1, len(a)):	#лишайєм 1 елемент і йдем на 2
            if a[j] < a[idxMin]:	#знаходим менший за новий 1
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

ary = [0,3,5,1,2,3,5,4,2,34,43,24]
print('Da list is:',ary)
print('Da sorted list is:',selection_sort(ary))
