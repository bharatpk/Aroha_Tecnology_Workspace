html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sist" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="siste" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


from bs4 import BeautifulSoup
'''
soup = BeautifulSoup(html_doc, 'html.parser')
print   soup.title
print  soup.title.name
print soup.title.parent.name
print soup.head.parent.name
print soup.p
print soup.p['class']
print soup.a
aa = soup.a['href']
#print aa
links=soup.find_all('a')
print links
for i in links :
    print i['href']
    
    
for link in soup.find_all('a'):
    print(link.get('href'))
    
    
print(soup.get_text())

for i in soup.find_all('a'):
    print(link.get('class'))
    
head_tag = soup.head.text
print head_tag




import re
for tag in soup.find_all(re.compile("^b")):
    print('-----'+tag.name)
    
soup.find_all(["a", "b"])
    
    
for tag in soup.find_all(True):
    print(tag.name)    
    
    
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(has_class_but_no_id)


print soup.find_all(string="Elsie")

first_link = soup.a
first_link.find_all_next(string=True)


print first_link.find_next("p")
print soup.select("body a")
print  soup.select("html head title")

'''
print soup.original_encodin
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

p=  tag.contents
print p[0]
print p[1]

print soup.get_text("|", strip=True)
print soup.original_encodin


    
    

 
