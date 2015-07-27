'''
import json as simplejson
import urllib2
fh = open('TRIAL2.txt')
url = "http://www.co.middlesex.nj.us/Government/Departments/Admin/Pages/default.aspx"
req = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(req)
json = simplejson.load(f)
for item in json:
    print item
    


'''

import csv
import sys
import json

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
fieldnames=[1,2,3,4,5,6,7,8]
filename='result.txt'

def convert(filename):
  csv_filename = filename
  print "Opening CSV file: ",csv_filename
  f=open(csv_filename, 'r')
  csv_reader = csv.DictReader(f,fieldnames)
  json_filename = csv_filename.split(".")[0]+".json"
  print "Saving JSON to file: ",json_filename
  jsonf = open(json_filename,'w')
  data = json.dumps([r for r in csv_reader])
  jsonf.writelines(data)
  
  
  f.close()
  jsonf.close()
convert(filename)

'''

#!/usr/bin/python
import demjson
data = []
fh =open('result.txt','r')
for line  in fh:
    
    

    json = demjson.encode(line).encode('utf-8','ignore')
    data.extend(json)
    
j = "".join(data)
print str(j)
      
  '''