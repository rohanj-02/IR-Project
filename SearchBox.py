from flask import Flask, render_template, request
from flask.helpers import flash
import pickle
import numpy as np
import pickle
import networkx as nx

with open('Models/graph.pkl','rb') as f:
    G=pickle.load(f)    

iiitd_profs=[i for i in list(G.nodes) if G.nodes[i]['authorCategory']=='iiitd']
G_=G.subgraph(iiitd_profs)



def get_domain_networks(query,homogeneous=True):    
    g=G_ if homogeneous==True else G
    domain_list=nx.get_node_attributes(g,'domains')
    domain_authors=[author for author in domain_list if query in domain_list[author].keys()]
    domain_cliques=list(nx.algorithms.find_cliques(g.subgraph(domain_authors)))
    domain_scores=[np.mean([domain_list[author][query] for author in clique]) for clique in domain_cliques]
    clique_scores=list(zip(domain_cliques,domain_scores))
    clique_scores.sort(reverse=True,key=lambda x:x[1])
    search_results=[clique[0] for clique in clique_scores[:min(10,len(clique_scores))] ]
    return search_results



app = Flask(__name__)
with open("AllDomains.pkl","rb") as file:
    domains = pickle.load(file)


@app.route('/',methods = ['GET','POST'])
def home():
    selected_domain = domains[0]
    print("hello")
    groups = []
    if request.method=='POST':
        domain = request.form['search-input']
        model = request.form['model']   
        selected_domain = domain
        groups = get_domain_networks(selected_domain,model)
        groups=[','.join(group) for group in groups]

    return render_template('index.html',domains=domains,selected_domain=selected_domain,groups=groups)





if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8000)