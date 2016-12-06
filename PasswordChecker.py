
# Detects if password is strong
#
#		1. At least 8 characters
#		2. Contains both upper and lowercase
#		3. At least 1 digit


import re

password_list = ['aaaaaaa','1234567', '12345678', '1234567a', '123456B', '123a4567G', 'A8aaaaaaa', '8Aaaaaaaa', 'aA8aaaaaaa']


for password in password_list:
	
	matchObj1 = re.search(r'([0-9A-Za-z]){8,}', password)
	matchObj2 = re.search(r'([0-9])', password)
	matchObj3 = re.search(r'([A-Z])', password)
	matchObj4 = re.search(r'([a-z])', password)
	
	#if re.match(r'[0-9A-Za-z]{8,}', password):
	if  matchObj1 and matchObj2 and matchObj3 and matchObj4:
		print('Strong')
		#print (password)
	else:
		print('weak')
		

