import sys
import math

print('Enter two an integer real numbers "a" and "b", moreover b does not equal zero')

a = float(input('Input number a: '))
b = float(input('Input number b: '))
x = (math.sqrt(a*b)/(math.exp(a)*b)) + a*math.exp(2*a/b)

if(a>=0 and b>0):
    print('Da result is:',x)
else:
    print('Error')
