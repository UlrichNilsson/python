import re

x = 'asdfasfda23452354sadfasf2345'

y = re.findall('[a-z0-9]',x)

print(y)
