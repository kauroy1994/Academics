#program to get all sentences out of a file
import nltk
with open("/Users/Kaushik/Downloads/lvi/docs500/BCDS-000119312511016485-d424b4.txt") as file1:
    text = file1.read().replace('\n','') #read the file using descriptor
    sents = nltk.sent_tokenize(text) #get sentences
primaryPhrases = ["offered", "by us","we are offering","common stock","we are selling","offered","offering of","initial"]
secondaryPhrases = ["offered by the selling stockholders","selling stockholder named in","supplement","is offering an addtional","of our"]
def relevant(sentence):
    for phrase in primaryPhrases:
        if phrase in sentence.lower():
            return True
    for phrase in secondaryPhrases:
        if phrase in sentence.lower():
            return True
    return False
for sentence in sents:
    if relevant(sentence):
        print "BCDS-000119312511016485-d424b4:"+"\""+sentence[:-1]+"\":"+str(int(0))

