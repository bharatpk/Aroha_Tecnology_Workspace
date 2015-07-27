
        

#matches = re.findall("(^(\d)?)", filetext)
#main program ---------
p_no=[]
name=[]
fhfinal = open('final_township.txt','w')


textfile = open('3_a.txt', 'r')
#textfile = open('4_a.txt', 'a')
filetext = textfile.read()
aa=str(filetext)
print aa

for i in aa.split(','):
    if i[0].isdigit() :
        
        print i
        p_no.append(i)
        
    else:
        name.append(i)
        print i
print p_no
print name
for (i,j) in zip(name, p_no):
    
    fhfinal.writelines(i+','+j)
    fhfinal.writelines('\n')    
   
   
fhfinal.close()
        
    

        
#main prgram ------     
'''
textfile = open('3_a.txt', 'r')
#textfile = open('4_a.txt', 'a')
find_list = [732,9,7,0,1,2,3,4,5,6,8,10]
filetext = textfile.read()
aa=str(filetext)
p_no=[]
name=[]



for i in aa.split(','):
	for j  in find_list:
		if str(j) in str(i):
			#print i
			p_no.append(i)
			break
			
			
			
			
		else:
			print i
			name.append(i)
			break
			
#print name
#print p_no
			
		
		
        
        
       
    
  
   
#a=[int(s) for s in aa.split(',') if s.isdigit()]
'''