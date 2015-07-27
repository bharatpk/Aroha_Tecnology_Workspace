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

def clensing ():
    FH=open("1.Content_Grab_Township.txt",'r')
    Fhout = open('2a.Content_clean_Township.txt','a')
    
    s = FH.read()
    delimeter = "To view Council member biography click on the word Bio"
    
    aa =(s.partition(delimeter)[2])
   
  
    
    Fhout.write(aa)
    
    Fhout.close()
    FH.close()
    
    
    

print 'content been written to the text file 2.Content_Grab_Township.txt'
  
clensing()


def clensing_leven2():
    FH=open("2a.Content_clean_Township.txt",'r')
    Fhout = open('2.Content_clean_Township.txt','a')
    
    s = FH.read()
    delimeter = "KeyLinks"
    
    aa =(s.partition(delimeter)[0])
   
  
    
    Fhout.write(aa)
    
    Fhout.close()
    FH.close()
    
    
    
  

print 'content been written to the text file 2.Content_Grab_Township.txt'
clensing_leven2()



        
        
        
	
	