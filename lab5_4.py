import sys
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

print('Your equal is:',a,'x^2 +',b,'x +',c,'= 0')

#if a=0, then ax^2 + bx + c = 0 become bx + c = 0
if(a==0):
    xa = -c/b
    print('The root of an equal is',xa)

#if b and c  or a and c are zero, then ax^2 + bx + c = 0 become ax^2 = 0 or bx = 0
elif((b==0 and c==0)
or (a==0 and c==0)):
    print('The root of an equal is 0')

#if b=0, then ax^2 + bx + c = 0 become ax^2 + c = 0
elif(b==0):
    xb = math.sqrt(-c/b)
    if(xb>0):
        print('The roots of an equal:',xb,-xb)
    elif(xb==0):
        print('The root of an equal is 0')
    else:
        print('The complex roots of an equal:',xb,-xb)

#if c=0, then ax^2 + bx + c = 0 become ax^2 + bx = 0
elif(c==0):
    xc_1 == 0
    xc_2 = -b/a
    print('The roots of an equal:',xc_1,xc_2)

#if b and c  or a and c are zero, then ax^2 + bx + c = 0 become ax^2 = 0 or bx = 0
elif((b==0 and c==0) or (a==0 and c==0)):
    print('The root of an equal is 0')

#if D>0
elif(math.pow(b,2) - 4*a*c >0):
    x_1 = (-b - math.sqrt(math.pow(b,2) - 4*a*c))/(2*a)
    x_2 = (-b + math.sqrt(math.pow(b,2) - 4*a*c))/(2*a)
    print('The roots of an equal:', x_1, x_2)

#if D=0
elif(math.pow(b,2) - 4*a*c==0):
    x = -b/(2*a)
    print('The root of an equal is',x)

#if D<0
elif(math.pow(b,2) - 4*a*c<0):
    #x_1 = (-b - math.sqrt(math.pow(b,2) - 4*a*c))/(2*a)
    #x_2 = (-b + math.sqrt(math.pow(b,2) - 4*a*c))/(2*a)
    print('The complex roots of an equal:', x_1, x_2)

#if a and b, or all constants are zero
else:
    print("What it is? Don't joke with me, because I'll call Steve Austin")
