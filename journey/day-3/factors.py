#! /bin/py

################################ factors.py ################################
# desc   : code that describes data types and operators in python          #
# author : @rishabhio                                                      #
# website: https://rishabh.io                                              #
# repo   : https://github.com/rishabhio/PythonCave                         #
# created: 07-09-16:01:11 ( DD-MM-YY:HH:MM )                               #
############################################################################
	
m = int(raw_input('Enter lower bound: '))
n = int(raw_input('Enter upper bound: '))
count = 0
for i in range(m,n):
	if i % 3 == 0 and i % 5 == 0:
		count = count + 1
		
print 'There are %d numbers divisible by both 3 and 5 in the range %d %d'%(count,m,n)