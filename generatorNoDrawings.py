import random
import networkx as nx
import matplotlib.pyplot as plt
from pyparsing import with_class


def DFS(test, i, V):
    for edge in test[i]:
        if edge[1] == V: return 1
        return DFS(test,edge[1],V)
    return 0

def drawGraph(fileName):
    f = open(fileName,'r')
    input = f.read().splitlines()
    for line,i in zip(input,range(len(input))):
        input[i] = line.split(" ")
    ##Store V and E
    V = int(input[0][0])
    E = int(input[0][1])
    edges = input[1:E+1]
    ##Make edges contain tuples of ints instead of strings
    for edge,i in zip(edges,range(len(input))):
        edges[i] = [int(edge[0]),int(edge[1]),int(edge[2])]

    ###G = nx.Graph()

    ##G.add_nodes_from([0, 3])
    G = nx.DiGraph()
    for i in range(V):
        G.add_node(i,label = i)
    for edge in edges:
        G.add_edge(edge[0],edge[1],weight = edge[2])

    nx.draw_shell(G,with_labels=True)
    dir = f'{fileName}.png'
    plt.savefig(dir)
    G.clear()
    plt.close()

Vmin, Vmax, Emin, Emax, W, testCases, scramble = map(int,input().split())
## Vmin      = minimum number of vertice in graph
## Vmax      = max number of vertice in graph
## Emin      = min number of edges pr vertice
## Emax      = max number of edges pr vertice 
# OBS May create a vertice with more edges than Emax, if it is necessary to ensure all vertice are reachable from start and all vertice can reach the end.
## W         = Weight of any given edge will be (-W <= weight <= W)
## testCases = Number of tests you want
## scramble  = 1 if you want the edgelist to be scrambled

## Run all test cases
for caseNo in range(testCases):
    V = random.randint(Vmin,Vmax)
    V = V-1
    test = [[]]
    ## Make random graph with V vertice all with Emin to Emax amount of edges, all with a weight between -W and W
    for i in range(V):
        test.append([])
        usedNodes = []
        for ii in range(random.randint(Emin,Emax)):
            nextNode = random.randint(i+1,V)
            if(len(usedNodes) >= V-i): continue
            while nextNode in usedNodes:   
                nextNode = random.randint(i+1,V)
            test[i].append((i, nextNode, random.randint(-W,W)))
            usedNodes.append(nextNode)

        
    canReachFrom0 = [0] * len(test)

    ##Finds the root node for each cluster that is not reachable from 0
    for node in test: 
        for edge in node:
            canReachFrom0[edge[1]] = 1
    ##For each root not not reachable from 0, connect it to a node before itself
    for i in range(len(canReachFrom0)):
        if canReachFrom0[i] > 0 or i == 0: continue
        startOfEdge = random.randint(0,i-1)
        test[startOfEdge].append((startOfEdge, i, random.randint(-W,W)))
    ##Now all nodes are reachable from 0 

    canReachEnd = [0] * len(test)
    ## Find all nodes not able to reach the end node
    for node,i in zip(test,range(len(canReachFrom0))):
        canReachEnd[i] = DFS(test,i,V)
    ## For each node, check if it can reach end, if it cannot, add new edge to node that can reach end
    for i in range(len(canReachEnd)):
        if i == V or canReachEnd[i]:continue
        newEdgeEnd = random.randint(i,V)
        while(canReachEnd[newEdgeEnd]):
            newEdgeEnd = random.randint(i,V)
        test[i].append(i,newEdgeEnd,random.randint(-W,W))

    ## Make list of all edges, topologically sorted, to make output file
    topologicallySortedEdges = []
    for node in test:
        for edge in node:
            topologicallySortedEdges.append(edge)
    if(scramble == 1): random.shuffle(topologicallySortedEdges)
    ## Write testcase to file
    fileName = f'{caseNo}.in'
    with open(fileName,'w') as l:
        firstLine = f'{V+1} {len(topologicallySortedEdges)}'
        l.write(f'{firstLine}\n')
        for edge in topologicallySortedEdges:
            l.write(f'{edge[0]} {edge[1]} {edge[2]}\n')