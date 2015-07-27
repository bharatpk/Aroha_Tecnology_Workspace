
import urllib2
from bs4 import BeautifulSoup

'''
def grab():  #Reusing of function of county to grab content 
                        
                      
                        
                        
                        FH=open('1.Content_Grab_Township.txt','a')
            
                        url="http://www.hpboro.com/directory.aspx"
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
                                                #a =  row.get_text().encode('ascii','ignore')
                                              
                                               
                                                #print a  
                                                #FH.writelines(a)
                                                
                                                for link in soup.find_all('a'):
                                                                        ab=link.get('href')   
                                                                        print ab
                                                                        
                                                                        
                                                
                                            
                                            
                                                
                                   
                                    
                                  
                                                
                                               
                                   
                                   
                                    
                                  
                                    
                        FH.close() 
                        
                       
                        
                        
grab() 

            

print 'content been written to the text file 1.Content_Grab_Township.txt'

'''
FH=open('1_1.txt','w')
url="http://www.hpboro.com/directory.aspx"
opener=urllib2.build_opener()
opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
response=opener.open(url)
soup=BeautifulSoup(response)

productDivs = soup.findAll('div', attrs={'id' : 'CityDirectoryLeftMargin'})
for div in productDivs:
   # asa =  div.findAll('a') 
    for link in div.findAll('a'):
        links= (link.get('href'))
        dv = link.get_text()
        print dv
        FH.writelines(links+'--'+dv)
        
        
        FH.writelines('\n')
        
     
        
FH.close()

with open('1_1.txt') as f:
    print sum(1 for _ in f)
f.close()



        
        
        
        
        