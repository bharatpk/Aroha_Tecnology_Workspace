


import string
from itertools import ifilter, imap


#FH=open("6.trial_content1.txt",'r')
FH=open("TRIAL1.txt",'r')
student_name=[]





for line in FH:
	a=str( line.strip(''))
	b =a.split('\n')
	
	
	
	ab = student_name.extend(b)
	
student = filter(None,student_name)
print student
st = student.remove('\xc2\xa0')
 

td8 = str(student)


str1=','.join(student)
FH.close()
FH1 = open('TRIAL2.txt','w+')
str2= str1.strip(',')
str3 =str2.rstrip("")
str4=str3.rstrip(',')
str7=str4.strip(',')
FH1.writelines(str7.lstrip())



FH1.close()




print student 






	

	
	    
























































































































































































































































