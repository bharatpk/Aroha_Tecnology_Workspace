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
	FH=open("2.content_County.txt",'r') 
	#FH=open("TRIAL1.txt",'r')
	student_name=[]
	
	
	
	
	
	for line in FH:
		a=str( line.lstrip())
		b = a.rstrip()
		c =b.split('\n')
		
		
		
		ab = student_name.extend(c)
		
	student = filter(None,student_name)
	print student
	for i in student: 
		if  i=='\xc2\xa0':  
			st = student.remove('\xc2\xa0')
	 
	
	td8 = str(student)
	
	
	str1=','.join(student)
	FH.close()
	FH1 = open('3.content_County.txt','w+')
	FH1.writelines(str1)
	
	
	
	FH1.close()
	
	
	
	
	print 'Content been written to 3.content_County.txt'
clensing()

	
	
	
	
	
		
	
		
		    
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	






















































































