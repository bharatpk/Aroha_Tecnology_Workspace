


import string
from itertools import ifilter, imap


FH=open("content.txt",'r')
student_name=[]





for line in FH:
	a=str( line.strip(' '))
	b =a.split('\n')
	
	
	ab = student_name.extend(b)
	




student = filter(None,student_name)
 
#std = student.remove("\r")

#td1 = student.remove("\t\r")
if  'Contact me' in student:
 
	td2 = student.remove("Contact me")
if  'Facebook' in student:
	td2 = student.remove("Facebook")
if  'Twitter' in student:
	td2 = student.remove("Twitter")
if  'Share' in student:
	td3 = student.remove("Share")
if  'Google plus' in student:

	td4 = student.remove("Google plus")
if  'Linkedin' in student:
	
	td5 = student.remove("Linkedin")
if  'Tumblr' in student:
	td6 = student.remove("Tumblr")
if  'Print' in student:
	td7 = student.remove("Print")
td8 = str(student)

str1=' '.join(student)
FH.close()
FH1 = open('content.txt','w+')
FH1.writelines(str1.lstrip())
FH1.close()




print student 






	

	
	    
























































































































































































































































