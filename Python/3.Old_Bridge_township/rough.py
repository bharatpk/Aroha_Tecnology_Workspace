'''import re
str = "h3110 23 cat 444.4 rabbit 11 2 dog"
for i in str.split():
    if i.isdigit():
        print i
    else:
        print 'i'

'''
'''

def clensing1():
    P_no=[]
    name=[]
student_name=[]
FH= open('2_a.txt')
FH1 = open('3_a.txt','w+')

    
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
   
'''
'''
import requests

link = "http://www.somesite.com/details.pl?urn=2344"
f = requests.get(link)

print f.text
    
   
   '''
'''
from tld import get_tld
town_ship=get_tld("http://www.eastbrunswick.org/content/202/default.aspx")
t =  town_ship.split('.')
town = t[0]
township = town.title()
print township
'''
import urllib2
from bs4 import BeautifulSoup 

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


