from itertools import izip
            
import urllib2
from bs4 import BeautifulSoup 
import string
FH=open("3.Content_clean_Township.txt",'r')
Fhout = open('4.Content_clean_Township.txt','a')
#i = [1,2,3,4,5,6,7,8,9,4]
delete_list=['- Bio']
for line in FH:
            for word in delete_list:
                        line = line.replace(word,"")
        

My_list = line.split(',')
print My_list

def pairwise(My_list):
    
            "s -> (s0,s1), (s2,s3), (s4, s5),(s6, s7),(s8, s9),"
            a = iter(My_list)
            return izip(a, a)


    


url="http://www.eastbrunswick.org/content/202/293/default.aspx"
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
    
for x, y in pairwise(My_list):
            print x,',',y
            Fhout.write(township+' ''Township'','+x+','+y) #township+' ''Township'','+x+','+y
            Fhout.write('\n')
            
FH.close()
Fhout.close()            
    
    



    

    
