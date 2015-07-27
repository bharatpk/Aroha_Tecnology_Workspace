



import os, sys
def naive_unicode_fixer(text):
    while True:
        match = POSSIBLE_UTF8_SEQUENCE.search(text)
        if match:
            fixed = match.group(1).encode('latin-1').decode('utf-8')
            text = text[:match.start()] + fixed + text[match.end():]
        else:
            return text
        
fh = open('4.Content_Two.txt','r+')
text= fh.readlines()
naive_unicode_fixer(text)
fh.close()

