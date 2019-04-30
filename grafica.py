import networkx as nx                                                                                                                        
import matplotlib.pyplot as plt                                                 

#n=100 Number of nodes                                                          
ncols=10 #Number of columns in a 10x10 grid of positions                        

N=10 #Nodes per side                                                            
G=nx.grid_2d_graph(N,N)                                                         
pos = dict(zip(G.nodes(),G.nodes()))                                            
ordering = [(y,N-1-x) for y in range(N) for x in range(N)]                      
labels = dict(zip(ordering, range(len(ordering))))                              
nx.draw_networkx(G, pos=pos, with_labels=False, node_size = 250, node_color='lightblue')                                                                       
nx.draw_networkx_labels(G, pos=pos, labels=labels)                              
plt.axis('off')                                                                 
plt.show()
