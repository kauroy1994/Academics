#get sentence and target
import nltk #import the nltk library for sentence processing
with open("posEx.txt") as pos: #open positive file and read sentences
    Poslines = pos.read().splitlines() 
with open("negEx.txt") as neg: #open negative file and read sentences
    Neglines = neg.read().splitlines()
sentenceIDs = {} #Dictionary for sentencesIDs and correspondingSentences
wordIDs = {} #Dictionary for wordIDs and correspondingWords
sIDCounter,wIDCounter = 1,1 #counter for uniqueness
def getWordID(Value):
    '''returns ID for a particular sentence'''
    position = wordIDs.values().index(Value)
    return wordIDs.keys()[position]

def getSentenceID(Value):
    '''returns ID for a particular sentence'''
    position = sentenceIDs.values().index(Value)
    return sentenceIDs.keys()[position]
#========================================MAKE SENTENCE AND WORD IDS FOR EACH SENTENCE IN POSITIVE AND NEGATIVE EXAMPLES====================
for line in Poslines:
    if line.split(":")[1] != "\"\"":
        key = str(line.split(":")[0])+"_"+"sentence"+str(sIDCounter) #key as docID_S<number>
        value = line.split(":")[1][1:-1] #value is the sentence string itself stripping off "" pair
        sIDCounter += 1
        sentenceIDs[key] = value #add the sentence id and sentence to the dictionary of sentence IDs
        tokens = nltk.word_tokenize(value)
        for word in tokens:
            key = str(line.split(":")[0])+"_"+"word"+str(wIDCounter) #key as docID_w<number>
            wIDCounter += 1
            wordIDs[key] = word #add the word id and word to the dictionary of word IDs
            
for line in Neglines:
    if line.split(":")[1] != "\"\"":
        key = str(line.split(":")[0])+"_"+"sentence"+str(sIDCounter) #key as docID_S<number>
        value = line.split(":")[1][1:-1] #value is the sentence string itself stripping off "" pair
        sIDCounter += 1
        sentenceIDs[key] = value #add the sentence id and sentence to the dictionary
        tokens = nltk.word_tokenize(value)
        for word in tokens:
            key = str(line.split(":")[0])+"_"+"word"+str(wIDCounter) #key as docID_w<number>
            wIDCounter += 1
            wordIDs[key] = word #add the word id and word to the dictionary of word IDs
#============================PRINT SENTENCE AND WORD===========================================================
#print sentenceIDs["AAVL-000119312515005317-d832044d424b4_sentence2993"]
#print wordIDs["AAVL-000119312515005317-d832044d424b4_word187050"]
print sentenceIDs["AAVL-000119312515005317-d832044d424b4_sentence3"]
