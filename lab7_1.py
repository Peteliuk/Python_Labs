#/usr/bin/env python3
import sys

s = raw_input('Enter da string: ')
k = int(input('Enter da slice number: '))

a =  s.replace(s[:k],'')

print (a + s[:k])
