


import string
from itertools import ifilter, imap


FH=open("content.txt",'r')
student_name=[]





for line in FH:
	a=str( line.strip(' '))
	b =a.split('\n')
	
	
	ab = student_name.extend(b)
	
#str1=''.join(student_name)
#print str1
#print student_name



student = filter(None,student_name)
 
#std = student.remove("\r")

#td1 = student.remove("\t\r")
td2 = student.remove("Contact me")
td2 = student.remove("Facebook")
td2 = student.remove("Twitter")
td3 = student.remove("Share")
td4 = student.remove("Google plus")
td5 = student.remove("Linkedin")
td6 = student.remove("Tumblr")
td7 = student.remove("Email")
td7 = student.remove("Print")
td8 = str(student)
#print td8
str1=' '.join(student)
FH.close()
FH1 = open('content.txt','w+')
FH1.writelines(str1.lstrip())
FH1.close()





print student 






	

	
	    
























































































































































































































































