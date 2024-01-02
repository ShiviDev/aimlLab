class Graph:
    def __init__(self, startNode, graph, heuristicNodeList):
        self.start=startNode
        self.graph=graph
        self.h=heuristicNodeList
        self.parent={}
        self.solutionGraph={}
        self.status={}

    def getNeighbors(self,v):
        return self.graph.get(v,'')
    
    def getStatus(self,v):
        return self.status.get(v,0)
    
    def setStatus(self,v,value):
        self.status[v]=value

    def applyAOstar(self):
        self.aoStar(self.start,False)

    def printSolution(self):
        print("traverse the graph from start node:",self.start)
        print("--------------------")
        print(self.solutionGraph)
        print("----------------------------------")

    def getHeuristicNodeValue(self,v):
        return self.h.get(v,0)
    
    def setHeuristicNodeValue(self,v,value):
        self.h[v]=value

    def computeMinimumCostChildNodes(self, v):
        minimumCost=0
        costToChildNodeListDict={} #cost to child node, with cost as key, and array of node as value
        costToChildNodeListDict[minimumCost]=[]
        flag=True #determine if its processing the first set of child nodes.
        for nodeInfoTupleList in self.getNeighbors(v):#returns [[(node,weights)],[(nod,weight)]]
            cost=0
            nodeList=[]
            for n, weight in nodeInfoTupleList:#[(node,weights),(node,weights)]
                cost=cost+self.getHeuristicNodeValue(n)+weight
                nodeList.append(n)
            if flag==True:
                minimumCost=cost
                flag=False
                costToChildNodeListDict[minimumCost]=nodeList
            else:
                if minimumCost>cost:
                    minimumCost=cost
                    costToChildNodeListDict[minimumCost]=nodeList
        return minimumCost, costToChildNodeListDict[minimumCost]

    def aoStar(self, v, backTracking):
        print("heuristic values: ",self.h)
        print("solution graph: ",self.solutionGraph)
        print("currently processing node: ",v)
        print("------------------------------")
        if self.getStatus(v)>=0: #unexplored node
            min, nodeList = self.computeMinimumCostChildNodes(v)
            print(min,nodeList)
            self.setHeuristicNodeValue(v,min)
            #self.setStatus(v,len(nodeList))
            solution=True #solution found
            for n in nodeList:
                self.parent[n]=v #set parent
                if self.getStatus(n)!=-1:
                    solution=False #soultion set to false
            if solution==True: #nodes have been fully explored
                self.setStatus(v,-1) #set the parents status to fully explore
                self.solutionGraph[v]=nodeList
            if v!=self.start: #not the starting node allow backtracking
                self.aoStar(self.parent[v],True)
            if backTracking==False: #initially, explore the given path fully
                for node in nodeList:
                    self.setStatus(node,0)
                    self.aoStar(node,False)

print("Graph 1")
h = {'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1}    
graph1= {
    'A':[[('B',1),('C',1)],[('D',1)]],
    'B':[[('G',1)],[('H',1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
} 
g1=Graph('A',graph1,h)       
g1.applyAOstar()
g1.printSolution()