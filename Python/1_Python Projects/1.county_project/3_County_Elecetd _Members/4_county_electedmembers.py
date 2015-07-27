from itertools import izip

from tld import get_tld
            
import urllib2
from bs4 import BeautifulSoup 
import string
FH=open("5.content_County.txt",'r')
Fhout = open('6.content_County_elected officials.txt','a')
#i = [1,2,3,4,5,6,7,8,9,4]
for line in FH:
            My_list = line.split(',')
print My_list

def pairwise(My_list):
    
            "s -> (s0,s1), (s2,s3), (s4, s5),(s6, s7),(s8, s9),(s10, s11),(s12, s13),(s14, s15),(s16, s17),(s18, s19)"
            a = iter(My_list)
            return izip(a, a)


    


url="http://www.co.middlesex.nj.us/Government/ElectedOfficials/Pages/default.aspx"
opener=urllib2.build_opener()
opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
response=opener.open(url)
soup=BeautifulSoup(response)
headding= soup.title.string
print headding
h = headding
domain = get_tld(url)
print domain 
a =domain.split('.')
township=a[0].title()
t = township
print township
name= 'County'
    
for x, y in pairwise(My_list):
            print x,',',y
            Fhout.write(township+' '+name+','+x+','+y)
            Fhout.write('\n')
            
FH.close()
Fhout.close()            
    
    



    

    
