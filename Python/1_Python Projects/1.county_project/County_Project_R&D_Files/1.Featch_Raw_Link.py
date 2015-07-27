

import urllib
import mechanize

def Raw_link():                                          #Function to Featch all the links from the source code 
	FH=open("1.Raw_links.txt",'a')
	baseurl = "http://www.co.middlesex.nj.us"
	url = "http://www.co.middlesex.nj.us/Government/Directory/Pages/directory.aspx"  
	b = mechanize.Browser()
	b.open(url)
	for link in b.links():
		
		FH.writelines(baseurl+"/"+link.url+"\n\n")                   #appending url  to baseurl to get ultimate link
		
	FH.close()

Raw_link()
print "LINKS HAS BEEN WRITTEN TO THE FILE Raw_Link.txt"



	
	


	
	