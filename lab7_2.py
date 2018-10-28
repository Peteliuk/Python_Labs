#/usr/bin/env python3
import sys

s = raw_input('Enter da string: ')
clean = s.replace(' ','')
lower = clean.lower()
if(lower == lower[::-1]):
    print True
else:
    print False
