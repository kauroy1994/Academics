class Agent(object):
    '''Agent class'''

    stateGraph = {} #will store the adjacency list
    cityIndex = {} #stores city indices
    InputList = None #list of cities distance triple
    distances = {}

    @staticmethod
    def readFile(fileName):
        '''reads file and calls generateInputList'''
        with open(fileName) as Input:
            rows = (row.strip().split() for row in Input)
            Agent.InputList = list(zip(*rows))
        Agent.generateCityIndices(0) #pass start index

    @staticmethod
    def generateCityIndices(index):
        '''generates indices for cities'''
        for rowIndex in range(2):
            for city in Agent.InputList[rowIndex]:
                if city not in Agent.cityIndex.keys():
                    Agent.cityIndex[city] = index
                    index += 1

    @staticmethod
    def getName(number):
        '''returns Name of city given the index'''
        position = list(Agent.cityIndex.values()).index(number) 
        return(list(Agent.cityIndex.keys())[position])
        
    @staticmethod
    def makeStateGraph():
        '''constructs state Graph'''
        for key in Agent.cityIndex:
            Agent.stateGraph[Agent.cityIndex[key]] = [] #initialize all to empty lists

        length = len(Agent.InputList[0])
        for city in range(length):
            Agent.distances[(Agent.InputList[0][city],Agent.InputList[1][city])] = float(Agent.InputList[2][city])#add distance to add when making path
            Agent.distances[(Agent.InputList[1][city],Agent.InputList[0][city])] = float(Agent.InputList[2][city])
            Agent.stateGraph[Agent.cityIndex[Agent.InputList[0][city]]].append(Agent.cityIndex[Agent.InputList[1][city]])
            Agent.stateGraph[Agent.cityIndex[Agent.InputList[1][city]]].append(Agent.cityIndex[Agent.InputList[0][city]])
        
    @staticmethod
    def BFS(source,destination):
        '''returns distance of path from source to destination found by bfs'''
        nodeInfo = []
        
        for i in range(len(Agent.stateGraph)):
            nodeInfo.append([-1,-1]) #distance, pred
    
        nodeInfo[source][0] = 0
    
        Paths = [source]
        while Paths:
            node = Paths.pop(0)
            if node == destination:
                print(Agent.getName(node))
                break
            print(Agent.getName(node)," --> ",end='')    
            for i in Agent.stateGraph[node]:
                if nodeInfo[i][0] == -1: #not visited
                    nodeInfo[i][0] = nodeInfo[node][0] + 1
                    nodeInfo[i][1] = node
                    Paths.append(i)


        if node != destination:
            return False
            
        #get path from source to destination and calculate path distance
        pathDistance = 0 #initialize
        Paths = [Agent.getName(destination)] #add destination to path
            
        while destination != source:
            pathDistance += Agent.distances[(Agent.getName(nodeInfo[destination][1]),Agent.getName(destination))]
            Paths.append(Agent.getName(nodeInfo[destination][1]))
            destination = nodeInfo[destination][1]
                        
        return("Path: " + str(Paths[::-1]) + "\nDistance: " + str(pathDistance) + "\n")

    @staticmethod
    def DFS(source,destination,limit=-1): #limit enter when implementing iterative deepening
        '''returns distance and path from source to destination found by dfs'''
        nodeInfo = []
        
        for i in range(len(Agent.stateGraph)):
            nodeInfo.append([-1,-1]) #distance, pred
    
        nodeInfo[source][0] = 0
    
        Paths = [source]

        for key in Agent.stateGraph:
            Agent.stateGraph[key] = (Agent.stateGraph[key])[::-1] #change input to consider left path first, otherwise right considered
            
        while Paths:
            node = Paths.pop()
            if node == destination:
                print(Agent.getName(node))
                break
            print(Agent.getName(node)," --> ",end='')                
            for i in (Agent.stateGraph[node]):
                if nodeInfo[i][0] == -1: #not visited
                    if limit!= -1:
                        if nodeInfo[node][0] + 1 <= limit:
                            nodeInfo[i][0] = nodeInfo[node][0] + 1
                            nodeInfo[i][1] = node
                            Paths.append(i)
                    else:
                        nodeInfo[i][0] = nodeInfo[node][0] + 1
                        nodeInfo[i][1] = node
                        Paths.append(i)
                        
        if node != destination:
            print("Not Found")
            return False
        #get path from source to destination and calculate path distance
        pathDistance = 0 #initalize
        Paths = [Agent.getName(destination)] #add destination to path
            
        while destination != source:
            pathDistance += Agent.distances[(Agent.getName(nodeInfo[destination][1]),Agent.getName(destination))]
            Paths.append(Agent.getName(nodeInfo[destination][1]))
            destination = nodeInfo[destination][1]                
                        
        return("Path: " + str(Paths[::-1]) + "\nDistance: " + str(pathDistance) + "\n")

                            
    @staticmethod
    def getDistance(source,destination,method):
        '''returns distance between source and destination using given method'''
        source,destination = Agent.cityIndex[source],Agent.cityIndex[destination]

        if method == "BFS":
            print(190*'=')
            print("Method: Breadth First Search")
            print(Agent.BFS(source,destination))
            

        elif method == "DFS":
            print(190*'=')
            print("Method: Depth First Search")
            print(Agent.DFS(source,destination))

        elif method == "ID":
            print(190*'=')
            print("Method: Iterative Deepening")
            for i in range(1,len(Agent.cityIndex)):
                print("\nTrying depth: "+str(i)+"\n")
                result =  Agent.DFS(source,destination,i)
                if result != False:
                    break

            print(result, "\nNode found after searching through to level: "+ str(i)+"\n")

    @staticmethod
    def Run():
        '''run BFS,DFS and ID to find path between source and destination input and compares execution'''
        Agent.readFile("Romania.txt")
        while True:
            print(190*'=')
            source = input("Enter first city or press s to exit: ")
            if source == 's':
                break
            destination = input("Enter second city or press s to exit: ")
            if destination == 's':
                break
            if (source in Agent.cityIndex.keys()) and (destination in Agent.cityIndex.keys()):
                print() #newline
                Agent.makeStateGraph()
                Agent.getDistance(source,destination,"BFS")
                Agent.getDistance(source,destination,"DFS")
                Agent.getDistance(source,destination,"ID")
            else:
                print("City Doesnt exist!\n")

Agent.Run()

                    
            
            
    
