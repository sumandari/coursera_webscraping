#!/usr/bin/env python3

import re
strings = 'From: sumansuman.email@domain.co.id To: yasmin@salsa.com  Mon Oct  5 09:14:16 2008'
x = re.findall('\S@\S',strings)
y = re.findall('\S+@\S+',strings)
z = re.findall('^From: (\S+@\S+)', strings)
print('\S@\S :', x)
print('\S+@\S+ :', y)
print('^From: (\S+@\S+): ', z)
