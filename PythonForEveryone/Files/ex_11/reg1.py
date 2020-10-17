import re

handle = open('mbox-short.txt')

for line in handle:
    if re.search('X-\S+:',line):
        line = line.rstrip()
        print(line)