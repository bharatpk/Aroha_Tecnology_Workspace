
import cookielib
import urllib2
import re
from urllib2 import urlopen

from cookielib import CookieJar
import time
FH=open("bpk.txt",'r+')

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#opener.addheader=[('User-agent','Mozilla/5.0')]
    
    
    

def main(): 
    try:
        
        li=FH.read()
        FH.close()
        FHfinal=open("2.Valid_Links.txt",'a')
        
        selectedlinks=open("Raw_Links.txt",'r+')
        opener=urllib2.build_opener()
        opener.addheaders=[('user_agent','Chrome/43.0.2357.124')]
        try:
            links = re.findall('(https?://\S+)',li)   #final all http and https links
            for link in links:
                #print link
                
                
                if 'aspx' in link:                   #Find all .aspx  valied links 
                    #print link
                 
                    FHfinal.writelines(link+'\n') 
                    try:                
                        linksource = opener.open(link).read()           # opening the each link and read the source code of the link
                    except Exception ,e:
                        print link
                        pass
                    
                    
                    pass
                    
        except Exception, e:
            print str(e)        
        
    except Exception, e:
        print str(e)
        FHfinal.close()
        code.close()
main()
print "CONTENT HAS BEEN WRITTEN TO THE file 2.Valid_Links.txt"





    

   