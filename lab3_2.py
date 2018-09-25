import sys
import math

print('''Example: 35F = 2C or 2C = 35F''')

t = input()

sign = t[-1] # the last character of the string is retrieved

# The line with the exception of the last character is translated into an integer
t = int(t[0:-1]) 

if sign == 'C' or sign == 'c': # If the sign denotes Celsius,
    t = round(t * (9/5) + 32) # Fahrenheit translation, rounding to the whole
    print(str(t) + 'F')
elif sign == 'F' or sign == 'f': # If the sign indicates Fahrenheit
    t = round((t - 32) * (5/9)) # translation in Celsius and rounding to the whole
    print(str(t) + 'C')
