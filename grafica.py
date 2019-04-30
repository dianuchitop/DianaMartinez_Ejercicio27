import networkx as nx                                                                                                                        
import matplotlib.pyplot as plt                                                 

                                                       
ncols=6

N=7 #Nodes per side                                                            
G=nx.grid_2d_graph(N,N)                                                         
pos = dict(zip(G.nodes(),G.nodes()))                                            
ordering = [(y,N-1-x) for y in range(N) for x in range(N)]                      
labels = dict(zip(ordering, range(len(ordering))))                              
nx.draw_networkx(G, pos=pos, with_labels=False, node_size = 300, node_color='green')                                                                       
nx.draw_networkx_labels(G, pos=pos, labels=labels)                              
plt.axis('off')                                                                 
plt.show()
plt.savefig("ldjnd")
