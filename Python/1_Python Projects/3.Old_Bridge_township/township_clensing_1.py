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
#function to strip from phone and extenction 
'''
def clensing ():
    FH=open("1_a.txt",'r')
    Fhout = open('2_a.txt','a')
    
    s = FH.read()
    delimeter = "Phone/Extension"
    
    aa =(s.partition(delimeter)[2])
    
   
  
    #Fhout.write(delimeter)
    Fhout.write(aa)
    
    
    Fhout.close()
    FH.close()
   ''' 
#function to remove unwwanted data  
'''
def valid_data():

    fin = open("2_a.txt",'r')
    #fin = open("content.txt",'r')
    #fout = open("4.Content_Two.txt", "w+")
    fout = open("2_after_a.txt", "w")
    delete_list = ['Email','Fax','.']
    for line in fin:
        for word in delete_list:
            line = line.replace(word,"")
        fout.write(line)
    fin.close()
    fout.close()
   
   ''' 

    
    
    
    
  
clensing()
valid_data()    





        
        
        
	
	