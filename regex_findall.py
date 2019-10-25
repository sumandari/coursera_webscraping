#!/usr/bin/env python3
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]', x)
z = re.findall('[0-9]+', x)
print('find all [0-9]', y)
print('find all [0-9]+', z)
