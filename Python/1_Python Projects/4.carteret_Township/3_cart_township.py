from itertools import izip
from itertools import *
import time

Fhout = open('3_cart_contentgrab.txt','a')

FH=open("2_cart_contentgrab.txt",'r') 
a=FH.read()
My_list= a.split(',')
township_name = (My_list[0])
township = (township_name).title()
My_list.remove(township_name)
print My_list
print township
print My_list



def pairwise(My_list):
    
            "s -> (s0,s1), (s2,s3), (s4, s5),(s6, s7),(s8, s9),(s10, s11),(s12, s13),(s14, s15),(s16, s17),(s18, s19),(s20, s21),(s22, s23),(s24, s25),(s26, s27),(s28, s29)"
            a = iter(My_list)
            return izip(a, a)


for x, y in pairwise(My_list):
            print x,',',y
            Fhout.write(x+','+y)
            Fhout.write('\n')


   
    
    
    
    
    
FH.close()
Fhout.close()       

 
time.sleep(10)



#shajsha


mylist=[]
Fhin = open('3_cart_contentgrab.txt','r')
Fhout= open('4_cart_catentefinal.txt','a')
m=Fhin.read()
mylist = m.split('\n')
print mylist 


def pairwise(mylist):
    
            "s -> (s0,s1), (s2,s3), (s4, s5),(s6, s7),(s8, s9),(s10, s11),(s12, s13)"
            a = iter(mylist)
            return izip(a, a)


for x, y in pairwise(mylist):
           
            Fhout.write(township+' ''Township'','+x+','+y)
            Fhout.write('\n')
           


Fhin.close()

Fhout.close()          


