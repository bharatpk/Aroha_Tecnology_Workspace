'''
fh1 = open('links.txt','r+')
num_lines = sum(1 for line in fh1)
print num_lines

a=10
for x in range(1, a+1):
    print x
   ''' 
#for x in range(1, 11) and y in range(10,21):
for (i,j) in [(i,j) for i in range(10,20) for j in range(20,30)]:
    print i,j
