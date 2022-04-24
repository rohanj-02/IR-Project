import json
import os
import networkx as nx
import matplotlib
import pickle

class Author:

    def __init__(self, name, authorType, authorCategory, penNames, articles=None, domain={}):
        self.name = name
        self.authorType = authorType
        self.articles = articles
        self.authorCategory = authorCategory
        self.penNames = penNames
        self.domains = {}

    def add_domain(self, sdomain):
        if sdomain in self.domains.keys():
            self.domains[sdomain] += 1
        else:
            self.domains[sdomain] = 1

    def printAuthor(self):
        print('Name =', self.name, 'Type =', self.authorType, 'Category =', self.authorCategory, 'NameList =',
              self.penNames, 'Domains =',self.domains)


    def __str__(self):
        return f'{self.name}'  # ,Type :{self.authorType}, Category: {self.authorCategory}, NameList: {self.penNames}'

    def __repr__(self):
        return str(self)


class Graph:
    def __init__(self, graph={}):
        self.graph = graph

    def addNode(self, node):
        self.graph[node] = {}

    def addEdge(self, node1, node2=None):
        if node2 is None:
            if node1 not in self.graph.keys():
                self.graph[node1] = {}
        elif node1 in self.graph.keys():
            if node2 not in self.graph.keys():
                self.graph[node2] = {}
            if node2 in self.graph[node1].keys():
                self.graph[node1][node2] += 1
            else:
                self.graph[node1][node2] = 1
            if node1 in self.graph[node2].keys():
                self.graph[node2][node1] += 1
            else:
                self.graph[node2][node1] = 1
        else:
            self.graph[node1] = {}
            if node2 not in self.graph.keys():
                self.graph[node2] = {}
            self.graph[node2][node1] = 1
            self.graph[node1][node2] = 1


G = Graph()
filepath = 'data/final/'
filepath2 = 'data/final2/'
facultyData = os.listdir(filepath)
studentData = os.listdir(filepath2)
facultyList = []
studentList = []
aList = []
for file in facultyData:
    with open(filepath + file, "r") as f:
        author = json.load(f)
    name = author['author']['name']
    if name == 'Dr. Doc. N. Arul Murugan':
        name = 'N. Arul Murugan'
    elif name == 'Ponnurangam Kumaraguru "PK"':
        name = 'Ponnurangam Kumaraguru'
    elif name == "Richa Gupta (Ph.D.)":
        name = 'Richa GGupta'
    nlist = [name.lower()]
    name = name.lower()
    temp = name.split(' ')
    if name == 'raghava mutharaju':
        nlist.append('vr mutharaju')
    if name == 'vivek bohara':
        nlist.append('va bohara')
    if name == 'sanat biswas':
        nlist.append('sk biswas')
    if name == 'bijendra jain':
        nlist.append('bn jain')
    if name == 'mukesh mohania':
        nlist.append('mk mohania')
    if name == "gajendra ps raghava":
        nlist.append('gps raghava')
        nlist.append('g raghava')
        nlist.append('gp Raghava')
        nlist.append('gs Raghava')
    elif len(temp) == 2:
        nlist.append(temp[0] + ' ' + temp[1][0])
        nlist.append(temp[0][0] + ' ' + temp[1])
    elif len(temp) == 3:
        nlist.append(temp[0][0] + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[1] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[1][0] + ' ' + temp[2][0])
        nlist.append(temp[0] + ' ' + temp[1] + ' ' + temp[2][0])
        nlist.append(temp[0] + ' ' + temp[1][0] + temp[2][0])
        nlist.append(temp[0][0] + ' ' + temp[1] + ' ' + temp[2][0])
    elif len(temp) == 4:
        nlist.append(temp[0][0] + temp[1][0] + temp[2][0] + ' ' + temp[3])
    else:
        print('Not Processed')
    aList.append(Author(name.lower(), 'faculty', 'iiitd', nlist, author['articles']))
aList.append(Author('ritu gupta', 'unknown', 'non_iiitd', ['r gupta','ritu gupta','ritu g']))
for file in studentData:
    with open(filepath2 + file, "r") as f:
        author = json.load(f)
    name = author['author']['name']
    nlist = [name.lower()]
    name = name.lower()
    temp = name.split(' ')
    if name == 'kuldeep yadav':
        nlist.append('ks yadav')
    if len(temp) == 1:
        pass
    elif len(temp) == 2:
        nlist.append(temp[0] + ' ' + temp[1][0])
        nlist.append(temp[0][0] + ' ' + temp[1])
    elif len(temp) == 3:
        nlist.append(temp[0][0] + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[1] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[1][0] + ' ' + temp[2][0])
        nlist.append(temp[0] + ' ' + temp[1] + ' ' + temp[2][0])
        nlist.append(temp[0] + ' ' + temp[1][0] + temp[2][0])
        nlist.append(temp[0][0] + ' ' + temp[1] + ' ' + temp[2][0])
    elif len(temp) == 4:
        nlist.append(temp[0][0] + temp[1][0] + temp[2][0] + ' ' + temp[3])
    else:
        print('Not Processed')
    aList.append(Author(name.lower(), 'student', 'iiitd', nlist, author['articles']))
l = []
# for i in aList:
#     i.printAuthor()

with open('publicationData.json', 'r') as f:
    data = json.load(f)

objList = []
newList = []
domainList = []
count = 0
rlist = []
for paper in data:
    data[paper]["authors"] = [i.lower() for i in data[paper]["authors"]]
    temp = []
    c = 0
    for i in data[paper]["authors"]:
        f = 0
        for stat in aList:
            if i in stat.penNames:
                c += 1
                if stat in temp:
                    continue
                temp.append(stat)
                count += 1
                f = 1
                break
        if f == 0:
            aList.append(Author(i, 'unknown', 'non_iiitd', [i]))
            temp.append(aList[len(aList) - 1])
    if c == 0:
        rlist += data[paper]["authors"]
        # print(paper, data[paper])
    objList.append(temp)
    domainList.append(data[paper]['domain'])
# print(domainList[5])
ctr=0

for i in range(len(objList)):
    for author in objList[i]:
        for domain in domainList[i]:
            author.add_domain(domain)
# rlist = sorted(rlist, key = rlist.count,reverse = True)
# print(result)``
# print(len(objList), count)
# rdict={}
# for i in rlist:
#     if i in rdict.keys():
#         rdict[i]+=1
#     else:
#         rdict[i]=1
# print(rdict)
ctr = 0
print(len(objList), len(domainList))
cc=0
for combo in objList:
    for i in range(len(combo) - 1):
        for j in range(i + 1, len(combo)):
            if combo[i].authorCategory == 'iiitd':
                G.addEdge(combo[i], combo[j])
            elif combo[j].authorCategory == 'iiitd':
                G.addEdge(combo[j], combo[i])

# with open ('graph3.txt','w') as f:
#     f.write(str(G.graph))

# print(G.graph)


# ddict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,}
# for a in G.graph:
#     for b in G.graph[a]:
#         if G.graph[a][b]>20:
#             print(a.name,b.name)
#         else:
#             ddict[G.graph[a][b]]+=1
# print(ddict)

# Convert The Graph to NetorkX Graph
G_=nx.Graph()
for author in G.graph:
    G_.add_node(author.name,articles=author.articles,authorCategory=author.authorCategory,
                authorType=author.authorType,penNames=author.penNames,domains=author.domains)
for i in G.graph:
    for j in G.graph[i]:
        G_.add_edge(i.name,j.name,weight=G.graph[i][j])

import pickle
with open('graph.pkl','wb') as f:
    pickle.dump(G_,f)