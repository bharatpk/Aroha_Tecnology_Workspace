fin = open("content.txt",'r')
fout = open("4.Content_Two.txt", "w+")
delete_list = ['Share','Facebook','Twitter','Google plus','Linkedin','Tumblr','Email','Print','Contact me', '\r']
for line in fin:
    for word in delete_list:
        line = line.replace(word,"")
    fout.write(line)
fin.close()
fout.close()
print "CONTENT HAS BEEN WRITTEN TO 4.Content_Two.txt"