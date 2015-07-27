
import urllib2
from bs4 import BeautifulSoup

FH=open('1_1.txt','r')
base_url="http://www.hpboro.com"
dept = []
url=[]
dept_final=[]
for line in FH:
    mylist=line.split('--')
    dept.append(mylist[1])
    url.append(mylist[0])
print url

    
    
    #print base_url+''+line
FH.close()

for i in dept :
    dept1=i.split('(')
   
    dept_final.append(dept1[0])
print dept_final



FH12=open('2_2.txt','a')
    

for a, b in zip(url, dept_final):
    FH12.writelines(b+'--'+base_url+''+a)
    FH12.writelines('\n')
    print b+'--'+base_url+''+a
FH12.close()


    






    
   


