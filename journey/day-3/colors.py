#! /bin/py
	

################################ colors.py #################################
# desc   : code that describes data types and operators in python          #
# author : @rishabhio                                                      #
# website: https://rishabh.io                                              #
# repo   : https://github.com/rishabhio/PythonCave                         #
# created: 07-09-16:01:11 ( DD-MM-YY:HH:MM )                               #
############################################################################
	
favColor = raw_input('Enter your Favourite Color: ')
favColor = favColor.lower() #change user input to lower case
personality = ''
if favColor == 'violet':
	personality = 'optimistic'
elif favColor == 'indigo':
	personality = 'independend'
elif favColor == 'blue':
	personality = 'practical'
elif favColor == 'green':
	personality = 'conservative'
elif favColor == 'yellow':
	personality = 'trustworthy'
elif favColor == 'orange':
	personality = 'reliable'
elif favColor == 'red':
	personality = 'loving'
else:
	personality = 'unpredictable'
		
print 'Your personality is: ',personality