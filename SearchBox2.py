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
    search_results=[(G.nodes[i]['penNames'][0],G.nodes[i]['domains'][query]) for i in list(G.nodes) if query in G.nodes[i]['domains'].keys()]
    search_results.sort(key = lambda x: x[1],reverse=True)
    return search_results[:5]



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
        groups=[group[0] for group in groups]

    return render_template('index2.html',domains=domains,selected_domain=selected_domain,groups=groups)





if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8000)