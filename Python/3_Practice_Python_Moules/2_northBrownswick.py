'''
def clensing():
	#FH=open("6.trial_content1.txt",'r')
	FH=open("TRIAL.txt",'r')
	FH1 = open('Trial1.txt','a')
	bpk=[]
	for i in FH:
		
		if i in  bpk:
			
			print i
		else:
			bpk.append(i)
			print bpk
			FH1.write(i)
			
			
		
clensing()
'''
'''
FH=open("TRIAL.txt",'r')
s = "I have a book to read."
aa =(s.partition("book")[2])
print aa
print(''.join(s.partition("book")[:2]))
'''

import string
from itertools import ifilter, imap
delimeter = "Council President"
def clensing ():
    FH=open("1.Content_Grab_Township.txt",'r')
    Fhout = open('2.Content_Grab_Township.txt','a')
    
    s = FH.read()
       
    aa =(s.partition(delimeter)[2])
   
  
    
    Fhout.write(aa)
    
    Fhout.close()
    FH.close()
    
    
    

print 'content been written to the text file 2.Content_Grab_Township.txt'
  
clensing()


def clensing_leven2():
    FH=open("2.Content_Grab_Township.txt",'r')
    Fhout = open('3.Content_clean_Township.txt','a')
    
    s = FH.read()
    delimeter2 = "E-Mail Councilman Socio"
    
    aaa =(s.partition(delimeter2)[0])
   
  
   
    Fhout.write(aaa)
    
    Fhout.close()
    FH.close()
    
    
    
  

print 'content been written to the text file 2.Content_Grab_Township.txt'
clensing_leven2()





def clensing():                                       # Function to Format the data 
	FH=open("3.Content_clean_Township.txt",'r') 
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
	FH1 = open('4.Content_clean_Township.txt','w+')
	FH1.writelines(delemeter)
	
	FH1.writelines(str1)
	
	
	
	FH1.close()
	
	
	
	
	print 'Content been written to 3.content_County.txt'
clensing()

	
	
 


        
        
        
	
	