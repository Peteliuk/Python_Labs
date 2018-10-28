#/usr/bin/env python3
import sys



s = raw_input('Enter da string: ')

if((s.count('(') == s.count(')'))
and (s.count('[') == s.count(']'))
and (s.count('{') == s.count('}'))
and (s.count('<') == s.count('>'))):
    print True
else:
    print False















