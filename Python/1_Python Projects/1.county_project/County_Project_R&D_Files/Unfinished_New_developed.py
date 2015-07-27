
import urllib2
from bs4 import BeautifulSoup

def folder():
   mypath = 'D:/bharat'
   if not os.path.isdir(mypath):
      os.makedirs(mypath)
      
def grab(line): 
                     
                       
                       
   FH=open('content.txt','w')

   url=line
   opener=urllib2.build_opener()
   opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
   response=opener.open(url)
   soup=BeautifulSoup(response)
   headding= soup.title.string
   FH.writelines(headding)
   
   for add in soup.findAll("div",{'class':'col-xs-12'}):
               content1= (add.get_text().encode('utf-8'))
              
               
             
               FH.writelines(content1)
	       print 'content grab done!!'
             
              
              
               
             
               
   FH.close() 
   

def valid_data():

   #fin = open("TRIAL.txt",'r')
   fin = open("content.txt",'r')
   fout = open("4.Content_Two.txt", "w+")
   #fout = open("TRIAL1.txt", "w+")
   delete_list = ['Share','Facebook','Twitter','Google plus','Linkedin','Tumblr','Email','Print','Contact me', '\r','\t',',','\xc2\xa0\xc2\xa0\xc2\xa0','\u00a0']
   for line in fin:
      for word in delete_list:
         line = line.replace(word,"")
      fout.write(line)
   fin.close()
   fout.close()
   print "CONTENT HAS BEEN WRITTEN TO 4.Content_Two.txt"
    





import string
from itertools import ifilter, imap

def clensing():
   FH=open("4.Content_Two.txt",'r')
   #FH=open("TRIAL1.txt",'r')
   student_name=[]
   
   
   
   
   
   for line in FH:
      a=str( line.strip(''))
      b =a.split('\n')
	   
	   
	   
      ab = student_name.extend(b)
	   
   student = filter(None,student_name)
   print student
   for i in student: 
	   if  i=='\xc2\xa0':  
		   st = student.remove('\xc2\xa0')
    
   
   td8 = str(student)
   
   
   str1=','.join(student)
   FH.close()
   FH1 = open('TRIAL1_NEW_DEVELOPED.txt','w+')
   FH1.writelines(str1)
   
   
   
   FH1.close()
   
   
   
   
   print student 
	
	
	
	
	
	
		
   




#main program starts fro here _________
fh1 = open('links.txt','r+')
num_lines = sum(1 for line in fh1)
for lin in iter(fh1):
            line = lin
            
            print line
            grab(line)
            #valid_data()
	    #clensing()
            
            
            
            
            
fh1.close()             
            




   
      

      
      
      
       
      
