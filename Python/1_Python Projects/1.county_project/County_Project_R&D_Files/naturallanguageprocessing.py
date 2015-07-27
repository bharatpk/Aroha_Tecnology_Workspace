import nltk
#nltk.download()
#from nltk.book import *
x= 'hi bharat kundapur welcome to "aroha tecnology "inc'
tok = nltk.word_tokenize(x)
print tok
tagged = nltk.pos_tag(tok)
print tagged

