import urllib2
from bs4 import BeautifulSoup

 
#delimeter='_______________________________'
fh1 = open('links.txt','r+')
num_lines = sum(1 for line in fh1)
print num_lines

#for lin in iter(fh1):
for i in range(1, num_lines+1):
            for lin in iter(fh1):

            
                        line = lin.encode('ascii','ignore') 
            
                        fhtrial = open('bpk'+ num_lines+1 +'.txt','a')
                        print line
            


                        def grab(line): 
                      
                        
                        
                                    FH=open('3.content.txt','a')
            
                                    url=line
                                    opener=urllib2.build_opener()
                                    opener.addheaders=[('user_agent','Chrome/43.0.2357.124')] #grab the content and put it in a file 
                                    response=opener.open(url)
                                    soup=BeautifulSoup(response)
                                    headding= soup.title.string
                                    FH.writelines(headding)
                        
                                    for add in soup.findAll("div",{'class':'col-xs-12'}):
                                  
                                                content1= (add.get_text().encode('utf-8'))
                                   
                                    
                                  
                                                Ffhtrial.writelines(content1)
                                   
                                   
                                    
                                                # FH.writelines('\n'+delimeter+'\n')          
                                    
                                                FH.close() 
                        
                                                fhtrial.close()
                        
                        
                        grab(line) 
            
          
           
            
            
fh1.close()            
            
print 'Task Completed'
print 'content been written to the text file content.txt'