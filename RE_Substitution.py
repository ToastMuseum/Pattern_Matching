
# Substituting new text in place of a text pattern using the 'sub()' method
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

# Substituting with multiple options
#		'\1,\2,\3,...etc' will substitute the new text into the corresponding group where \1 refers to group1
namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.sub(r'\1****', 'Agent Alice gave Agent Eve the secret documents because Agent Pablitos said Agent Bob was a double agent.')

namesRegex = re.compile(r'Agent (\w)(\w*)')
namesRegex.sub(r'\2****', 'Agent Alice gave Agent Eve the secret documents because Agent Pablitos said Agent Bob was a double agent.')

