'''import re
str = "h3110 23 cat 444.4 rabbit 11 2 dog"
for i in str.split():
    if i.isdigit():
        print i
    else:
        print 'i'

'''


def clensing1():
    P_no=[]
    name=[]
student_name=[]
FH= open('2_a.txt','r')
FH1 = open('3_a.txt','a')

    
for line in FH:
    a=str( line.rstrip())
    c = a.lstrip()
    b =c.split('\n')
   
    
    
    
		    
		    
		    
    ab = student_name.extend(b)
   
    
    
student = filter(None,student_name) 
asas= ','.join(student)
FH1.write(asas)

fh2 = open('3_a.txt','r')



FH.close()
FH1.close()
   
   
    
   
    