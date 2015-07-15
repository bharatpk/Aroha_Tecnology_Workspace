
import urllib2
from bs4 import BeautifulSoup


def grab():  #Reusing of function of county to grab content 
                        
                      
                        
                        
                        FH=open('1.Content_Grab_Township.txt','a')
            
                        url="http://www.eastbrunswick.org/content/202/default.aspx"
                        opener=urllib2.build_opener()
                        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
                        response=opener.open(url)
                        soup=BeautifulSoup(response)
                        headding= soup.title.string
                        print headding
                       # print headding 
                      
                        
                        #for add in soup.findAll("div",{'main wide grid_12 clearfix'}):
                         #                       content1= add.get_text().encode('ascii','ignore')
                         #                       print content1
                         #                       print '-------------------------------------------------------'
                                               
                                                                                                             #FH.writelines(content1)
                                          
                                                
                        for row in soup.find_all('tr'):
                                               # grade = row.select('th')
                                                a =  row.get_text().encode('ascii','ignore')
                                              
                                               
                                                print a  
                                                FH.writelines(a)
                                                
                                            
                                            
                                                
                                   
                                    
                                  
                                                
                                               
                                   
                                   
                                    
                                  
                                    
                        FH.close() 
                        
                       
                        
                        
grab() 

            

print 'content been written to the text file 1.Content_Grab_Township.txt'