
def valid_data():

    #fin = open("TRIAL.txt",'r')
    fin = open("content.txt",'r')
    fout = open("4.Content_Two.txt", "w+")
    fout = open("TRIAL1.txt", "w+")
    delete_list = ['Share','Facebook','Twitter','Google plus','Linkedin','Tumblr','Email','Print','Contact me', '\r','\t',',','\xc2\xa0\xc2\xa0\xc2\xa0']
    for line in fin:
        for word in delete_list:
            line = line.replace(word,"")
        fout.write(line)
    fin.close()
    fout.close()
    print "CONTENT HAS BEEN WRITTEN TO 4.Content_Two.txt"
    
valid_data()