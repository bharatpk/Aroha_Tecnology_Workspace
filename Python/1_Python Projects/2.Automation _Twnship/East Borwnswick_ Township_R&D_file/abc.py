
import string
from itertools import ifilter, imap

def clensing():                                       # Function to Format the data 
	FH=open("2.Content_clean_Township.txt",'r') 
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
	FH1 = open('3.Content_clean_Township.txt','w+')
	FH1.writelines(str1)
	
	
	
	FH1.close()
	
	
	
	
	print 'Content been written to 3.content_County.txt'
clensing()