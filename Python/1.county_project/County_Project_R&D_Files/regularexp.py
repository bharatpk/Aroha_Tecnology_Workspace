#regular expression 
#!/e/bin/python
'''import re
#FH=open("Everything.exe",'r')
#a = FH.readlines()
line = "soura.muk@yahoo.con sjdhskaj@kljqdlqkj.com"
print re.findall(r'(\w[\w.]+)@([\w.]+)',line)
'''
'''
import re
FH=open("a.txt",'r')

for line in FH.readlines():
	pat = re.findall("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",line)
	FH.close()
print pat
'''

import re
FH=open("a.txt",'r')
a=FH.read()
FH.close()
ipaddress=re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",a)

print ipaddress

	
'''
import re
#FH=open("Everything.exe",'r')
#a = FH.readlines()
line = "192.168.1.1 192.168.1.2 "
print re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",line)
'''