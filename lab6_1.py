#!/usr/bin/env python3
import sys
import math

"""def figure(a):
    a = a.split()
    for i in range(len(a)):
        a[i] = float(a[i])
   # if a[i] <= 0:
   #     print("The value of triangle sizes must be more then 0")
   #         break
    if len(a) == 3:
        p = (a[0]+a[1]+a[2])/2
        square = math.sqrt(p * (p-a[0]) * (p-a[1]) * (p-a[2]))
        print("Triangle's square is:  ", square)
    else:
        print("Enter three numbers!") 
param = input("Enter sides of da triangle by spaces: ")
figure(param)
"""


def input(a):
    a = a.split()
    for i in range(len(a)):
        a[i] = float(a[i])


def logic(p, s):
    if len(a) == 3:
        p = (a[0]+a[1]+a[2])/2
        s = math.sqrt(p * (p-a[0]) * (p-a[1]) * (p-a[2]))
        return True
    else:
        return False

def output(s):
    if logic == True:
        print("Triangle's square is:  ", s)
    else:
        print("Enter three numbers!") 

param = input("Enter sides of da triangle by spaces: ")
input(param)
output()
