import sys
import math

# Листинг 8
n = int(input("n="))
a = range(n+1)
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in xrange(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)
