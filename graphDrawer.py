import networkx as nx
import matplotlib.pyplot as plt
from pyparsing import with_class

fileName = input()

f = open(fileName,'r')
input = f.read().splitlines()
for line,i in zip(input,range(len(input))):
    input[i] = line.split(" ")
##Store V and E
V = int(input[0][0])
E = int(input[0][1])
edges = input[1:E+1]
print(edges)
##Make edges contain tuples of ints instead of strings
for edge,i in zip(edges,range(len(input))):
    edges[i] = [int(edge[0]),int(edge[1]),int(edge[2])]

print(edges)
###G = nx.Graph()

##G.add_nodes_from([0, 3])
G = nx.DiGraph()
for i in range(V):
    G.add_node(i,label = i)
for edge in edges:
    G.add_edge(edge[0],edge[1],weight = edge[2])

nx.draw_planar(G,with_labels=True)
dir = f'{fileName}.png'
plt.savefig(dir)