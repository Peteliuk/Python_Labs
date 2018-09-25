import sys
import math

print('Enter sides of a triangle (a, b, c)')

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

#Test of triangle existing
if((c>a and c>b and a+b>c)
or(b>a and b>c and a+c>b)
or(a>b and a>c and b+c>a)):
    print('Triangle has been exist')

elif(a==0 and b==0 and c==0):
    print('Triangle has not been exist')

else:
    print('Triangle has not been exist')
