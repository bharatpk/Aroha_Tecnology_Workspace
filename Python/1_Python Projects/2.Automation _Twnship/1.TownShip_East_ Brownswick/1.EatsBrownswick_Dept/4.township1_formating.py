
        
import urllib2
from bs4 import BeautifulSoup 
import string
url="http://www.eastbrunswick.org/content/202/default.aspx"
opener=urllib2.build_opener()
opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
response=opener.open(url)
soup=BeautifulSoup(response)
headding= soup.title.string
print headding
a =headding.split(',')
b = str(a[0])
c = b.split('-')
township = c[1]
print township
#matches = re.findall("(^(\d)?)", filetext)
#main program ---------
p_no=[]
name=[]

township_specifier='Township'



fhfinal = open('4.final_township.txt','a')


textfile = open('3.Content_clean_Township.txt', 'r')
#textfile = open('4_a.txt', 'a')
filetext = textfile.read()
aa=str(filetext)
#print aa
textfile.close()

for i in aa.split(','):
    if i[0].isdigit() :
        print i
        
        
       
        p_no.append(i)
        
    else:
        name.append(i)
        
print p_no
print name
for (i,j) in zip(name, p_no):
    print name
    
    fhfinal.writelines(township+' '+township_specifier+','+i+','+j)
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
