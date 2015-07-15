import urllib2

handle= open('bpk.txt','r')
text = handle.read()
words = text.split()
counts = dict()
for word in  words:
    counts[word] = counts.get(word,0)+1
bigcount = None
bigword = None
for words,count in counts.items():
    if bigcount is None or count >bigcount:
        bigcount = word
        bigcount = count
print bigword,bigcount
