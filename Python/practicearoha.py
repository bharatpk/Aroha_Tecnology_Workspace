'''

import sys
with open("content.txt" ,'r+') as f:
    for line in f:
        if not line.isspace():
            sys.stdout.write(line) 
            f.write(line)
            

'''
'''
import re
FH=open("content.txt",'r')
a=FH.read()
with open("content.txt" ,'r+') as f:
    for line in f:
        if re.match(r'^\s*$', line):
            print line
'''            
'''with open("content.txt" ,'r+') as f:
    for line in f:
        print line                 

'''

from __future__ import division  
import nltk, re, pprint
from nltk import word_tokenize

from urllib import request

raw = response.read().decode('utf8')
type(raw)

len(raw)
1176893
raw[:75]b
