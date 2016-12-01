
# Using findall() method  
#		will return A list of strings of every match in search
#		No match object created 

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneNumRegex.findall('Cell: 415-555-999 Work: 212-555-0002')


# if groups appear in the regular expression findall() returns a list of tuples instead
#		one string for each group

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phoneNumRegex.findall('Cell: 415-555-999 Work: 212-555-0001')

