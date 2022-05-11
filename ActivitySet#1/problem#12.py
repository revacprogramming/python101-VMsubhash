# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
print( sum( [ int(i) for i in re.findall('[0-9]+',open("regx_sum_1548421.txt","r").read()) ] ) )