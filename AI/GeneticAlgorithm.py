#Program to understand and demonstrate genetic algorithm
#Program to find best assignment of numbers 0-9 and operators +,-,*,/ to get a number
from random import sample,random #import random number generator
def Bin(Dec):
    #returns binary equivalent of a decimal number
    bin=[0,0,0,0]
    i = 3
    while Dec!=0:
        r = Dec%2 #extract remainder
        bin[i] = r #create binary number
        Dec = Dec//2 #divide decimal and re-iterate
        i -= 1
    return(bin) #return binary number

encodings = {}
for item in range(0,10):
    encodings[item] = Bin(item)
encodings['+'] = [1,0,1,1] #encodings for operators
encodings['-'] = [1,0,1,0]
encodings['*'] = [1,1,0,1]
encodings['/'] = [1,1,1,0]
keyList = list(encodings.keys()) #get list of just keys
valueList = list(encodings.values()) #get list of just values

def isDigit(x):
    #return boolean value based on digit or not
    try:
        float(x)
        return True
    except ValueError:
        return False
    
def decode(chromosome):
    #decodes the chromosome
    decoded = []
    for item in chromosome:
        index = valueList.index(item)
        decoded.append(keyList[index])
    return(decoded)

def getChromosome():
    #return a random chromosome
    chromosome = [] #place holder for random chromosome
    indices = sample(range(14),14) #sample 14 random numbers
    for index in indices: #create random chromosome
        chromosome.append(encodings[keyList[index]])
    return(chromosome) #return random chromosome

def parseChromosome(chromosome):
    #creates parser stack and returns it
    decoded = decode(chromosome)
    parserStack= []
    for item in decoded:
        if len(parserStack) == 0:
            parserStack.append(item)
        elif (isDigit(parserStack[len(parserStack)-1])) and (not isDigit(item)):
            parserStack.append(item)
        elif (not isDigit(parserStack[len(parserStack)-1])) and (isDigit(item)):
            parserStack.append(item)
    if len(parserStack)%2 == 1: #steps to make sure stack starts and ends with digit
        if not isDigit(parserStack[0]):
            parserStack = parserStack[1:len(parserStack)-1]
    elif len(parserStack)%2 == 0:
        if not isDigit(parserStack[0]):
            parserStack = parserStack[1:]
        elif isDigit(parserStack[0]):
            parserStack = parserStack[:len(parserStack)-1]
            
    return(parserStack) #return parserStack
    
def fitnessScore(chromosome,n):
    #returns fitness score of chromosome
    parserStack = parseChromosome(chromosome)
    empty = 1
    evaluationStack = []
    for item in parserStack:
        if empty==1:
            evaluationStack.append(item)
            empty = 0
        elif empty==0:
            top = len(evaluationStack)-1 #get stack top
            if isDigit(evaluationStack[top]): #if top is digit just push
                evaluationStack.append(item)
            elif not isDigit(evaluationStack[top]): #if not compute and push
                operator = evaluationStack.pop()
                digit = evaluationStack.pop()
                if operator == '+':
                    evaluationStack.append(digit+item)
                elif operator == '-':
                    evaluationStack.append(digit-item)
                elif operator == '*':
                    evaluationStack.append(digit*item)
                elif operator == '/':
                    if item!=0:
                        evaluationStack.append(digit/item)
                    else:
                        evaluationStack.append(digit)
    if n - evaluationStack[0] == 0:
        return("perfect")
    else:
        return(1/(n - evaluationStack[0])**2)

def getChromosomes(n):
    #return n random chromosomes
    chromosomes = [] #place holder for n chromosomes
    for i in range(n): #generate n
        chromosomes.append(getChromosome())
    return(chromosomes)

def normalize(vector):
    #returns normalized vector of values
    normalized = []
    for item in vector:
        normalized.append(item/sum(vector))
    return(normalized)

def select(chromosomes,distribution):
    #returns two candidates sampled from distribution
    selection=[]
    N = len(distribution) #length of distribution vector
    while len(selection)!=N: #make sure you sample N chromosomes
        selection = []
        for i in range(0,N):
            prob = random() #uniform random number
            if prob < distribution[0]: #sample based on probability
                selection.append(chromosomes[0])
            else:
                for i in range(1,N):
                    if prob >= distribution[i-1] and prob < distribution[i]:
                        selection.append(chromosomes[i])
    return(selection) #return samples

def Dist(chromosomes,number):
    #returns distribution on chromosomes based on fitness function
    fitnessScores = []
    for chromosome in chromosomes: #compute fitness score on chromosomes
        fitnessScores.append(fitnessScore(chromosome,number))
    return(normalize(fitnessScores)) #return probability of each chromosome

def crossOver(candidates,crossOverFraction):
    #returns cross over candidates
    crossOverIndex = round(crossOverFraction*len(candidates[0])) #get crossover point
    for i in range(0,4,2): #perform crossover
        temp = candidates[i][crossOverIndex:]
        candidates[i][crossOverIndex:] = candidates[i+1][crossOverIndex:]
        candidates[i+1][crossOverIndex:] = temp
    return(candidates)

def mutate(crossedOver,probability):
    #mutates bits with probability
    for i in range(4):
        for j in range(14):
            bitSequence = crossedOver[i][j]
            for k in range(4):
                if random() < probability:
                    bitSequence[k] = 1 - bitSequence[k]
                    if bitSequence in valueList:
                        crossedOver[i][j] = bitSequence
    return(crossedOver)
    
def main():
    #main function
    number = float(input("Enter a number: ")) #input the number
    chromosomes = getChromosomes(4) #initialize 4 random chromosomes
    crossOverFraction = 0.8
    mutationProbability = 0.001
    print('='*40)
    for chromosome in chromosomes: #compute fitness score on chromosomes
        print(fitnessScore(chromosome,number))
    for i in range(150): #see fitness scores for 150 generations
        print('='*40)
        print("Generation: ",i+1)
        distribution = Dist(chromosomes,number) #generate probability distribution over them
        candidates = select(chromosomes,distribution) #sample based on the distribution
        crossedOver = crossOver(candidates,crossOverFraction) #cross over candidates
        mutated = mutate(crossedOver,mutationProbability) #mutate bits with mutation probability
        chromosomes = mutated #replace with new generation and keep checking fitness
        for chromosome in chromosomes:
            print(fitnessScore(chromosome,number))
        
main()
