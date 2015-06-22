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
with open("content.txt" ,'r+') as f:
    for line in f:
        print line                 

