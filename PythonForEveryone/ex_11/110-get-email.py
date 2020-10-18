import re

handle = open('mbox-short.txt')

for line in handle:
    for email in re.findall('\S+@\S+',line):
        print(email)