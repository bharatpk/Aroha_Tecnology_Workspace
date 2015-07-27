'''import urllib
htmlfile = urllib.urlopen("http://www.co.middlesex.nj.us/Government/Directory/Pages/directory.aspx")
htmlraw = htmlfile.read()
print htmlfile 
'''

import urllib
#from bs4 import Beautifulsoup
#import urlparse
import mechanize
FH=open("bpk.txt",'w')
baseurl = "http://www.co.middlesex.nj.us"
url = "http://www.co.middlesex.nj.us/Government/Directory/Pages/directory.aspx"
b = mechanize.Browser()
b.open(url)
for link in b.links():
	#print link.url
	#a = link.url
	#FH=open("bpk.txt",'w')
	FH.writelines(baseurl+"/"+link.url+"\n\n")
	
FH.close()

