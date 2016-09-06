#! /bin/py
	
import sys

################################ cubes.py ##################################
# desc   : code that describes data types and operators in python          #
# author : @rishabhio                                                      #
# website: https://rishabh.io                                              #
# repo   : https://github.com/rishabhio/PythonCave                         #
# created: 07-09-16:01:11 ( DD-MM-YY:HH:MM )                               #
############################################################################
	
n = int(raw_input('Enter the value of N: '))
if n > 100:
	print 'N too large, program exiting!'
	sys.exit(0)
else:
	num = 1
	while num <= n:
		print 'Cube of %d is %d'%(num,num**3)
		num += 1 