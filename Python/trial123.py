f = open('links.txt','r')
for line in iter(f):
    print line
f.close()