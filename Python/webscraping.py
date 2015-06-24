import urllib2
from bs4 import BeautifulSoup

 

FH=open('content.txt','w+')
def grab(): 
          
            
            


            url="http://www.co.middlesex.nj.us/Government/Departments/PSH/Pages/adult-youth_landing.aspx"
            opener=urllib2.build_opener()
            opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
            response=opener.open(url)
            soup=BeautifulSoup(response)
            headding= soup.title.string
            FH.writelines(headding)
                        
            for add in soup.findAll("div",{'class':'col-xs-12'}):
                        content1= (add.get_text().encode('utf-8'))
                       
                        
            #for add in soup.findAll("div",{'class':'col-md-12'}):
                        #content2= (add.get_text().encode('utf-8'))            
                        FH.writelines(content1)
                       
                       
                        
                        #FH.writelines(content2) 
                        
            FH.close() 
            
            #lines = open('content.txt').readlines()
            #open('newfile.txt', 'w').writelines(lines[3:-1])
            
grab() 
