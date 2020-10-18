import re

x = 'My 2 favorite numbers re 12 and 45'

# + = At least one
y = re.findall('[0-9]+',x)

print(y)