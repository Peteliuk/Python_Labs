import sys
import math

h = float(input('Enter your height (in meters): '))
w = float(input('Enter your weight (in kilos): '))
BMI = w/math.pow(h,2)

print('Your BMI is:',BMI)
