#col-md-12 dark-bg dark-bg-person



import urllib2
from bs4 import BeautifulSoup


def grab():                              # Function to Fetch content from a web page using Url 
                        
                      
                        
                        
                        FH=open('1.content_County.txt','w')    
            
                        url="http://www.co.middlesex.nj.us/Government/ElectedOfficials/Pages/default.aspx"
                        opener=urllib2.build_opener()
                        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
                        response=opener.open(url)
                        soup=BeautifulSoup(response)
                        headding= soup.title.string
                        FH.writelines(headding)
                        print headding 
                        
                        content1=soup.get_text().encode('ascii','ignore')
                        
                        #for add in soup.findAll("div",{'col-md-12 dark-bg dark-bg-person'}):
                                      #          content1= add.get_text().encode('ascii','ignore')
                                                 
                                    
                                     
                                   
                        FH.writelines(content1)
                                                 
                                    
                                   
                                    
                                  
                                    
                        FH.close() 
                        
                       
                        
                        
grab() 


print 'content been written to the text file 1.content_County.txt'


	
	


	
	