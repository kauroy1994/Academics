#Program to do approximate best bayes net structure for given data
from random import random,sample,randint
from math import log
N = 4 #number of nodes
M = 1000 #number of data points
nodes = [x for x in range(N)] #generate node indices
ranks = sample([x for x in range(N)],N) #generate ranks to avoid cycles
data = [[randint(0,1) for x in range(N)] for n in range(M)] #generate M data points
Graphs = {}
def generateDAG():
    #generates a DAG and adds to Graphs
    global nodes
    global ranks
    dict = {} #place holder for subDag
    for node in nodes:
        dict[node] = [] #place holder for connected vertices
    edgeProbability = 0.5 #random chance of an edge between nodes
    for i in range(N-1): #make subDAG
        for j in range(i+1,N):
            if ranks[i] > ranks[j]:
                if random() < edgeProbability:
                    dict[i].append(j)
            elif ranks[j] > ranks[i]:
                if random() < edgeProbability:
                    dict[j].append(i)
    return (dict)

def generateDAGs(X):
    #populates Graphs with X unique subDags
    global Graphs
    counter = 1
    for i in range(X):
        subDag = generateDAG()
        if subDag not in Graphs.values():
            Graphs[counter] = subDag
            counter += 1
            
def getLogl(dP,dag):
    #returns log likelihood of data point according to the model
    global data
    likelihood = 1 #initialize likelihood
    for key in dag:
        if len(dag[key]) == 0: #if node not dependent on anything, just count number of occurences of value/total
            count = 0
            for dPoint in data:
                if dP[key] == dPoint[key]:
                    count += 1
            likelihood *= count/M
        else:
            countN,countD = 1,1 #else count Joint node values and divide by count of marginal of node values that it depends on
            foundN,foundD=1,1
            num,den = [],[]
            num.append(key)
            for value in dag[key]:
                num.append(value)
                den.append(value)
            for dPoint in data:
                for var in num:
                    if dP[var] != dPoint[var]:
                        foundN = 0
                if foundN:
                    countN += 1
                for var in den:
                    if dP[var] != dPoint[var]:
                        foundD = 0
                if foundD:
                    countD += 1
            likelihood *= countN/countD
                
    return likelihood

generateDAGs(100) #generate dags using 100 iterations
logDict = {}
for key in Graphs:
    dag = Graphs[key]
    logl = 0 #initialize log likelihood
    for dP in data:
        logl += log(getLogl(dP,dag)) #calculate loglikelihood for every data point and sum
    logDict[logl] = dag

print("Best Bayes net structure for given data is: ")
maximum = max(list(logDict.keys())) #get Dag with maximum total loglikelihood i.e. sum and print
print(logDict[maximum])