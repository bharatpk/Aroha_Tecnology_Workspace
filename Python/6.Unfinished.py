


import string
from itertools import ifilter, imap


FH=open("6.trial_content1.txt",'r')
student_name=[]





for line in FH:
	a=str( line.strip(' '))
	b =a.split('\n')
	
	
	ab = student_name.extend(b)
	
student = filter(None,student_name)
 

td8 = str(student)


str1=', '.join(student)
FH.close()
FH1 = open('6.trail_content3.txt','w+')

FH1.writelines(str1.lstrip())



FH1.close()




print student 






	

	
	    























































































































































































































































