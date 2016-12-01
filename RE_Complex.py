

# Complex Regexes

# VERBOSE mode can be used to make organizing the regular expression easier

# Complex regular expression 
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# Organizing Expression
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?					# area code
	(\s|-|\.)?							# separator
	\d{3}								# first 3 digits
	(\s|-|\.)							# separator
	\d{4}								#last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?)		#extension
	)''', re.VERBOSE)
	
	

# Combining re.IGNORECASE, re.DOTALL, re.VERBOSE
# 		use the '|' bitwise operator to select among the three modes

#create a regular expression that is case-insensitive and includes newlines
regexVal = re.compile('foo', re.IGNORECASE | re.DOTALL)

# create a regular expression that is case-insensitive, includes newlines, and allows organizing/comments
regexVal = re.compile('foo', re.IGNORECASE| re.DOTALL | re.VERBOSE)

