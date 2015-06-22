'''from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    
    def handle_data(self, data):
        print "", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')


'''
'''a = ['a', 'b', 'c']
link = "a123"
if any(x in link for x in a):
  print link
else:
  print "no strings found in str"
'''

with open('filename.ext') as input_file:
    for i, line in enumerate(input_file):
        print line,
print "{0} line(s) printed".format(i+1)



    
