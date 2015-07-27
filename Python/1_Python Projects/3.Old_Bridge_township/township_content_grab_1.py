
import urllib2
from bs4 import BeautifulSoup


def grab(): 
                        
                      
                        
                        
                        FH=open('1_a.txt','a')
            
                        url="http://www.oldbridge.com/content/137/default.aspx"
                        opener=urllib2.build_opener()
                        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
                        response=opener.open(url)
                        soup=BeautifulSoup(response)
                        headding= soup.title.string
                        print headding
                        my_list=[]
                       # print headding 
                      
                        
                        #for add in soup.findAll("div",{'main wide grid_12 clearfix'}):
                         #                       content1= add.get_text().encode('ascii','ignore')
                         #                       print content1
                         #                       print '-------------------------------------------------------'
                                               
                                        
                                                
                        for row in soup.find_all('table',{'class' : 'ContentTemp_Directory'}):
                                               # grade = row.select('th')
                                                a =  row.get_text().encode('ascii','ignore')
                                                list_content=my_list.append(a)
                                               
                                                
                                                
                                                
                                              
                                               
                                                print a  
                                                FH.writelines(a)
                        print my_list
                                            
                        FH.close() 
grab() 

            
