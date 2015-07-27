
import urllib2
from pyquery import PyQuery
from bs4 import BeautifulSoup


def grab():  #Reusing of function of county to grab content 
                        
                      
                        
                        
                        FH=open('1.Content_Grab_Township.txt','a')
            
                        url="http://www.northbrunswicknj.gov/council_main.html"
                        opener=urllib2.build_opener()
                        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
                        response=opener.open(url)
                        soup=BeautifulSoup(response)
                      
                        
                        headding= soup.title.string
                        print headding
                        
                        ''' 
                        doc = PyQuery(soup)
                                              
                        for td in doc("table").find("td.text-align:center"):
                                                print td.text, td.getnext().text 
                                                '''
                        a = soup.get_text().encode('ascii','ignore')
                        print a
                        FH.writelines(a)
                       # print headding 
                      
                        
                        #for add in soup.findAll("div",{'main wide grid_12 clearfix'}):
                         #                       content1= add.get_text().encode('ascii','ignore')
                         #                       print content1
                         #                       print '-------------------------------------------------------'
                        '''                   
                       
                                      
                        for row in soup.find_all('tr'):
                                               # grade = row.select('td')
                                                a =  row.get_text().encode('ascii','ignore')
                                              
                                               
                                                print a  
                                                FH.writelines(a)
                        '''
                
                        '''
                        for div in soup.findAll('div'):
                                                a = div.findAll('table')
                                                print a
                                                
                                   
                           '''         
 
grab() 

            

print 'content been written to the text file 1.Content_Grab_Township.txt'