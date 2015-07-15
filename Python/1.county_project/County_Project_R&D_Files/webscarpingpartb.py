import urllib2
from bs4 import BeautifulSoup

 

fh1 = open('links.txt','r+')
for lin in iter(fh1):
            line = lin           
            print line
            


            def grab(line): 
                      
                        
                        
                        FH=open('content.txt','a')
            
                        url=line
                        opener=urllib2.build_opener()
                        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
                        response=opener.open(url)
                        soup=BeautifulSoup(response)
                        headding= soup.title.string
                        FH.writelines(headding)
                        
                        for add in soup.findAll("div",{'class':'col-xs-12'}):
                                    content1= (add.get_text().encode())
                                   
                                    
                                  
                                    FH.writelines(content1)
                                    
                                   
                                   
                                    
                                  
                                    
                        FH.close() 
                        
                       
                        
                        
            grab(line) 
fh1.close()            
            
print 'Task Completed'
print 'content been written to the text file content.txt'
