import urllib2

print 'Hi'
data = []
fh = open('4.Content_Two.txt','r')
a = fh.read()
fh.close()
#print a
b = a.split('_______________________________') 
#print type(b)
#print b 
    
for i in b :
    mystring = str(i)
    aa= mystring.split('\n')
    #print aa
    student = filter(None,aa)
    print student
    for i in student:
	iz = str(i)
        ii = iz.rstrip()
        ia = ii.lstrip()
	if  i=='\xc2\xa0':  
	    st = student.remove('\xc2\xa0')
			 
     
		    
    str1=','.join(student)
   
    FH1 = open('3.content_County.txt','a')
    FH1.writelines(str1)
    FH1.writelines('\n')
    
    
    
		    
FH1.close()
		    
		    
print 'Content been written to 3.content_County.txt'    
		    
