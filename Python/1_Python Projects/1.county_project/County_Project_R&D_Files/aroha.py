#import sys
#import codecs
#sys.stdout
#sys.stdout.encoding 
import urllib
from bs4 import BeautifulSoup

url = "http://www.co.middlesex.nj.us/Government/Directory/Pages/directory.aspx/"
html = urllib.urlopen(url).read()


soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
    script.extract()    
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)
f = codecs.open('bpk1.txt', 'w', encoding='utf-8')
f.write(text)
f.close() 