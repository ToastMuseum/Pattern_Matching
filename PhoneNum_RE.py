
# Finding a phone number in text using regular expressions (regexes)


# All regex functions in Python are in the re module.

# Regular Expression Matching:
#	1. import regex module 'import re'
#	2. Create regex object 're.compile()' - use raw string to allow escape characters
#	3. Pass string into regex objects search() method - returns Match object
#	4. Call Match object group() method to return matched text

#	Use regexpal.com/ for more information

import re

#create a regex object using re.compile()
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')


mo = phoneNumRegex.search('My number is 415-555-4242.')
print('phone number found: ' +  mo.group()) 
