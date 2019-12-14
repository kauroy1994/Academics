class Astar(object):

    Heuristic = {} #static member variable, heuristic dictionary
    Graph = {} #store the graph in adjacency list format

    @staticmethod
    def readFile(fileName):
        '''function to read heuristic file and populate dictionary'''
        with open(fileName) as Heuristics:
            lines = Heuristics.readlines() #reading file lines

        length = len(lines)

        #populate dictionary
        for i in range(length):
            lines[i] = lines[i].strip("\n") #strips each line of its newline
            item = lines[i].split() #create individual dictionary key value pair
            Astar.Heuristic[item[0]] = float(item[1])

    






