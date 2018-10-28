#!/usr/bin/env python3
import statistics

n = 10
k = 3

res = 0

for i in range(1, n+1):
    res = (res + k) % i

print(res + 1)
