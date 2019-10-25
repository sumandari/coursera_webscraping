hand = open('text.txt', 'rt')
for line in hand:
    line = line.rstrip()
    if line.find('from:') >= 0:
        print(line)
hand.close()

print("using regex", "="*30)

import re
hand = open('text.txt', 'rt')
for line in hand:
      line = line.rstrip()
      if re.search('from:', line):
          print(line)
