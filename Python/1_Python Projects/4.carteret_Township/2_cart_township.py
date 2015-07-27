'''
import string
from itertools import ifilter, imap
FH=open("TRIAL1.txt",'r')
Fh = open('TRIAL1_NEW_DEVELOPED.txt','a')
my_list=[]

for line in FH:
	
	b =line.splitlines()
	# Good
	
	if b==['']:
		
		
		
	else:
		e = my_list.extend(b)
		print e
		
		
		
	
		
	
	
	
Fh.close()

FH.close()
'''


import string
from itertools import ifilter, imap

def clensing():                                       # Function to Format the data 
	FH=open("1_cart_contentgrab.txt",'r') 
	#FH=open("TRIAL1.txt",'r')
	student_name=[]
	
	
	
	
	
	for line in FH:
		a=str( line.lstrip())
		b = a.rstrip()
		c =b.split('\n')
		
		
		
		ab = student_name.extend(c)
		
	student = filter(None,student_name)
	print student
		
	td8 = str(student)
	
	
	str1=','.join(student)
	FH.close()
	FH1 = open('2_cart_contentgrab.txt','w+')
	FH1.writelines(str1)
	
	
	
	FH1.close()
	
	
	
	
	print 'Content been written to 2_cart_contentgrab'
clensing()

	
	
	
	
	
		
	
		
		    
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	






















































































