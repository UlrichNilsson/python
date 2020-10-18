import re

# Sample data
#handle = open('regex_sum_42.txt')
# Actual data
handle = open('regex_sum_1024433.txt')

sumofvalues=0

for line in handle:
    numbersinline=re.findall('[0-9]+',line)    
    for number in numbersinline:
        sumofvalues=sumofvalues+int(number)
        
print(sumofvalues)