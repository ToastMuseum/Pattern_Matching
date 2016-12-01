# Character classes for regular expressions and
#		making your own character classes


# Shorthand character classes

# 			/d					digit 0-9
# 			/D					any character not a numeric digit 0-9
# 			/w					word characters: any letter, digit, or the underscore character
# 			/W					any character that is not a letter, digit, or underscore character
# 			/s					Space, tab, newline characters
# 			/S					any character that is not a space tab or newline


import re

# lets search a christmas list
# 	search for a value with (one or more digits separated by a space and on or more word characters
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,	7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')


# Make your own character classes
#		defined using square brackets '[]'

# lets make a character class that matches any vowel
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

# create a range of letters or numbers using a hyphen '-'
rangeRegex = re.compile(r'[a-zA-Z0-9.]')
rangeRegex.findall('RoboCop eats baby food. BABY FOOD.')


# You can create a negative character class with '^'
#		use it to match everything that is NOT in the defined character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

# Indicate that a match must occur at the beginning of the searched text with '^'
#		put the caret at the start of the regex
beginsWithRegex = re.compile(r'^Hello')
beginsWithRegex.search('Hello World')
beginsWithRegex.search('He said Hello') == None


# Indicate that a match must occur at the end of  the searched text with '$'
#		put that dollar sign at the end of the regex
endsWithRegex = re.compile(r'\d$')
endsWithRegex.search('Your number is 23')
endsWithRegex.search('32 is Your number$') == None


# Indicate that a match must be the entire regex a subset is not enough
#		put the caret first and the dollar sign last together
wholeStringRegex = re.compile(r'^\d+$')
wholeStringRegex.search('123456789')
wholeStringRegex.search('123456xy789') == None
wholeStringRegex.search('12 3456789') == None


# Match any character except a newline character with the '.' or wildcard character
#		To match an actual '.' use the escape '\.'
#		One '.' will matched with one character for example 'flat' will return 'lat'
#			'..at' will return 'flat'
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# Match Everything and Anything with '.*'
#		Default Mode: Greedy
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Get Last Name: Swifty')
mo.group(1)
mo.group(2)
mo.group()

# Match Everything nonGreedy
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve a man> for dinner.>')
mo.group()

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve a man> for dinner.>')
mo.group()


# Math Newlines using re.DOTALL 
#		can make the '.' character match all characters including the newline
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()


# Ignore Case Sensitive Text using 're.IGNORECASE' or 're.I'
batman = re.compile(r'batman', re.I)
batman.search('BatMan is part bat, part man, all badass').group()


