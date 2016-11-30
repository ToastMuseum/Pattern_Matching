
# Grouping in regex requires '()' without escape '\'
#		(\d{3})-(\d{3}-\d{4})

# Groups can be referenced using group() and the integer order that they are entered
# 		


import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My Number is 415-555-4242.')		

for i in range(0,3):
	print('group(', i, '): ', mo.group(i))
	
print('group(): ', mo.group())



# receive all Groups at once as tuple: using groups()
mo.groups()
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


#pattern match a phone number that uses () around area code with '\'
phoneNumRegex = re.compile(r'(\(\d{3}\))(\d{3}-\d{4})')
mo = phoneNumRegex.search('My Number is (415)555-4242.')
mo.group(1)
mo.group(2)
mo.groups()


# Matching Multiple groups using '|' pipe
#		Whichever comes first in text will be selected as the Match Object
#		To match a '|' use the escape character '\|' 

PersonRegex = re.compile(r'Batman | Carl Grimes')
mo1 = PersonRegex.search('Batman or Carl Grimes')
mo1.group()

mo2 = PersonRegex.search('Carl Grimes or Batman')
mo2.group()

# Pattern match one of several patterns (batman, batmobile, batcopter, batbat)
batRegex = re.compile(r'Bat(man|mobile|copter|bat| and ball)')
mo = batRegex.search('I lost my Bat and ball')
mo.group()
mo.group(1)


# Optional Matching using '?'
#	Match zero or one of the groups preceding the '?'

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

# Look for phone numbers with or w/o an area code
phoneRegex = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')
mo1 = phoneRegex.search('my phone number is 999-999-9999')
mo2 = phoneRegex.search('my phone number is 999-9999')

mo1.group()
mo2.group()


# Match zero or more with '*'
batRegex = re.compile(r'(Bat(wo)*man)')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowowoman')
mo3.group()
	
	
# Match one or more with '+'
#		requires at least one match with the value within '()'
#		Will return none if no matches occur
batRegex = re.compile(r'(Bat(wo)+man)')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowowoman')
mo3.group()
	
	
# Match repeated patterns
haRegex = re.compile(r'(ha){3}')
mo = haRegex.search('hahaha and haha and hahahaha')

haRegex = re.compile(r'(ha){3,5}')
mo1 = haRegex.search('ha or haha or hahaha')
mo2 = haRegex.search('hahahaha or ha')
mo3 = haRegex.search('hahahahahaha')	

# Greedy vs NonGreedy ('?') Matching
#	NonGreedy returns the minimum match and Greedy the max match

greedyHaRegex = re.compile(r'(ha){3,5}')
mo1 = greedyHaRegex.search('hahahahahaha')
mo1.group()

nongreedyHaRegex = re.compile(r'(ha){3,5}?')
mo2 = nongreedyHaRegex.search('hahahahahaha')
mo2.group()


# Use the findall() method to find all matches 
 
