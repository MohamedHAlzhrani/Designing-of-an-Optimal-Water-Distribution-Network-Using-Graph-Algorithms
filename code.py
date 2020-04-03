import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.tree.mst import minimum_spanning_tree
from networkx.generators.random_graphs import erdos_renyi_graph
import random
from networkx.classes.graph import Graph
G=nx.Graph()
G = nx.random_graphs.gnp_random_graph(100,0.50)
for (u,v,w) in G.edges(data=True):
    w['weight'] = random.randint(1,100) 

 # positions for all nodes

edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])

a=minimum_spanning_tree(G,algorithm='prim')

pos = nx.spring_layout(G,k=100,scale=33)

nx.draw_networkx_nodes(a, pos, node_size=125,node_color='red')

labels = nx.get_edge_attributes(a,'weight')

nx.draw_networkx_edge_labels(a,pos,edge_labels=labels,label_pos=0.5,font_size=8,font_color='blue')

nx.draw_networkx_edges(a, pos,width=1)

nx.draw_networkx_labels(a, pos, font_size=8, font_family='sans-serif')
#_____________________________________________________________________________prints comand & show comand___________________________________________________________________________________________________
A = nx.adjacency_matrix(G)
print("adjacency_matrix_OF_GRAPH ( G )")
print(A.todense())
print("Number of connection ( M ) =",len(a.edges))
print("Cost of building the water distribution network= ",a.size(weight='weight'))
plt.axis('off')
plt.show()



