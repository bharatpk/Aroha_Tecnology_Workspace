
import urllib2
from bs4 import BeautifulSoup


def grab(): 
                        
                      
                        
                        
                        FH=open('TRIAL.txt','w')
            
                        url="http://www.co.middlesex.nj.us/Government/Departments/BDE/Pages/Office_Workforce.aspx"
                        opener=urllib2.build_opener()
                        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
                        response=opener.open(url)
                        soup=BeautifulSoup(response)
                        headding= soup.title.string
                        FH.writelines(headding)
                        
                        for add in soup.findAll("div",{'class':'col-xs-12'}):
                                                content1= add.get_text().encode('ascii','ignore')
                                                
                                   
                                    
                                  
                                                FH.writelines(content1)
                                                
                                   
                                   
                                    
                                  
                                    
                        FH.close() 
                        
                       
                        
                        
grab() 

            
print 'Task Completed'
print 'content been written to the text file content.txt'