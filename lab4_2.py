import sys
import math

print('Enter 3 real numbers')

numA = float(input(''))
numB = float(input(''))
numC = float(input(''))

res = (1/numC*math.sqrt(2*math.pi))*math.exp((-1*math.pow((numA-numB),2))/(2*math.pow(numC,2))

print('Result:',res)
