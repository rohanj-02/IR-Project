import matplotlib
import networkx as nx
import pickle
from pyvis.network import Network

with open('Models/graphBlockchain.pkl', 'rb') as f:
    G = pickle.load(f)
iiitd_profs=[i for i in list(G.nodes) if G.nodes[i]['authorCategory']=='iiitd' and G.nodes[i]['authorType']=='faculty']
G_=G.subgraph(iiitd_profs)
network=Network(notebook=True)
network.from_nx(G_)
network.show('blockchain.html')