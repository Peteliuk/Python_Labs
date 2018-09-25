import sys
import math

#The size of the door is 0.7x2
h = 2
w = 0.7
print('The size of the door is 0.7x2')

#The size of the box
print('Enter the size of the box (a, b, c) in meters')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

#determination if there is some way to fit the box through the door
if ((a<h and b<h)
or (b<h and c<h)
or (a<h and c<h)

or (a<w and b<w)
or (b<w and c<w)
or (a<w and c<w)):
    print('Congratulation! You are a lifter!')
elif(a<=0 and b<=0 and c<=0):
    print('Blue Death Screen!!')
else:
    print('Very bad')
