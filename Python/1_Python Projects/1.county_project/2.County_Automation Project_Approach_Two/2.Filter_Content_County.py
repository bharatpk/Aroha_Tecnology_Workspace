
def valid_data():

    fin = open("1.content_County.txt",'r')            # Function to Remove Unwanted  chunks of data from the whole dataset 
    #fin = open("content.txt",'r')
    fout = open("2.content_County.txt", "w+")
    #fout = open("TRIAL1.txt", "w")
    delete_list = ['Share','Facebook','Twitter','Google plus','Linkedin','Tumblr','Email','Print','Contact me', '\r','\t',',','\xc2\xa0\xc2\xa0\xc2\xa0','\u00a0']
    for line in fin:
        for word in delete_list:
            line = line.replace(word,"")
        fout.write(line)
    fin.close()
    fout.close()
    print "CONTENT HAS BEEN WRITTEN TO 2.content_County.txt"
    
valid_data()
