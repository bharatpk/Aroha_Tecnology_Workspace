'''
import urllib2

handle= open('3.content.txt','r')
text = handle.read()
words = text.split()
counts = dict()
handle.close()
handle= open('3.content.txt','w')
for line in  words:
    handle.writelines(line+'\n')
    print line
print 'done '    
handle.close()'''

'''
FH1=open('conteddadant.txt','wb')
FH = open('3.content.txt','r')
for line in FH:
	line1 = filter(None,line)
	
	
	FH1.writelines(line1)
FH.close()
FH1.close()
'''

	#a=str( line.strip(' '))
	#b =a.split('\n')
	#
	
	#ab = student_name.extend(b)
	
#student = filter(None,student_name)



 


