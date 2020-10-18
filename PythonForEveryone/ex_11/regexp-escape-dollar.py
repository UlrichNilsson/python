import re

x = 'I have alot of $ and even more $'

y = re.findall('\$',x)

print(y)