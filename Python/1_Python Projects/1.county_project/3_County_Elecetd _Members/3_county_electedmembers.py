
def valid_data():

    fin = open("4.content_County.txt",'r')            # Function to Remove Unwanted  chunks of data from the whole dataset 
    #fin = open("content.txt",'r')
    fout = open("5.content_County.txt", "w+")
    #fout = open("TRIAL1.txt", "w")
    delete_list = ['Elected Officials,',',Profile']
    for line in fin:
        for word in delete_list:
            line = line.replace(word,"")
        fout.write(line)
    fin.close()
    fout.close()
    print "CONTENT HAS BEEN WRITTEN TO 2.content_County.txt"
    
valid_data()
'''

print get_tld("http://www.google.co.uk")
'''