import json
import os
import networkx as nx
import matplotlib

class Author:
    
    def __init__(self, name, authorType, authorCategory, penNames, articles=None):
        self.name = name
        self.authorType = authorType
        self.articles = articles
        self.authorCategory = authorCategory
        self.penNames = penNames

    def printAuthor(self):
        print('Name =', self.name, 'Type =', self.authorType, 'Category =', self.authorCategory, 'NameList =',
              self.penNames)
    
    def __str__(self):
        return f'{self.name}'#    ,Type :{self.authorType}, Category: {self.authorCategory}, NameList: {self.penNames}'

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
fpath = "data/author_update/"
OUT_DIR = "data/author_update2/"
allData = os.listdir(fpath)
filepath = 'data/final/'
filepath2 = 'data/final2/'
facultyData = os.listdir(filepath)
studentData = os.listdir(filepath2)
facultyList = []
studentList = []
aList = []
for file in facultyData:
    # if path exists
    if os.path.exists(fpath + file):
        with open(fpath + file, "r") as f:
            author = json.load(f)
    else:
        with open(filepath + file, "r") as f:
            author = json.load(f)
    name = author['author']['name']
    if name == 'Dr. Doc. N. Arul Murugan':
        name = 'N. Arul Murugan'
    elif name == 'Ponnurangam Kumaraguru "PK"':
        name = 'Ponnurangam Kumaraguru'
    elif name == "Richa Gupta (Ph.D.)":
        name = 'Richa Gupta'
    nlist = [name.lower()]
    name = name.lower()
    temp = name.split(' ')
    if name=='raghava mutharaju':
        nlist.append('vr mutharaju')
    if name=='vivek bohara':
        nlist.append('va bohara')
    if name=='sanat biswas':
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

for file in studentData:
    if os.path.exists(fpath + file):
        with open(fpath + file, "r") as f:
            author = json.load(f)
    else:
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

with open('authorData.json', 'r') as f:
    data = json.load(f)
objList = []
newList = []
count = 0
rlist=[]
all_authors = []

def saveAuthorNames(pubs_data, filep):
    global count
    global rlist
    authors = []
    for file in pubs_data:
        if os.path.exists(fpath + file):
            with open(fpath + file, "r") as f:
                author = json.load(f)
        else:
            with open(filep + file, "r") as f:
                author = json.load(f)
        # with open(filep + file, "r") as f:
        #     author = json.load(f)
        for pub in author['articles']:
            if pub['title'] in data:
                paper = pub['title']
                data[paper] = [i.lower() for i in data[paper]]
                temp = []
                c = 0
                for i in data[paper]:
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
                        newList.append(Author(i, 'unknown', 'non_iiitd', [i]))
                        temp.append(newList[len(newList) - 1])
                if c == 0:
                    rlist+=data[paper]
                # temp has to be saved.
                author['articles'][author['articles'].index(pub)]["processed_authors"] = list(map(lambda x: x.name, temp))
            else:
                author['articles'][author['articles'].index(pub)]["processed_authors"] = []
        #save the author data
        authors.append(author)
        with open(OUT_DIR + file, "w") as f:
            json.dump(author, f, indent = 4)
    return authors

all_authors.extend(saveAuthorNames(facultyData, filepath))
all_authors.extend(saveAuthorNames(studentData, filepath2))

all_articles = []
for author in all_authors:
    all_articles.extend(author['articles'])

unique_articles = []
unique_titles = []
for article in all_articles:
    if article['title'] not in unique_titles:
        unique_articles.append(article)
        unique_titles.append(article['title'])

print("Unique articles: ", len(unique_articles))
print("All articles: ", len(all_articles))

with open("unique_articles.json", "w") as f:
    json.dump(unique_articles, f, indent = 4)
# for paper in data:
#     data[paper] = [i.lower() for i in data[paper]]
#     temp = []
#     c = 0
#     for i in data[paper]:
#         f = 0
#         for stat in aList:
#             if i in stat.penNames:
#                 c += 1
#                 if stat in temp:
#                     continue
#                 temp.append(stat)
#                 count += 1
#                 f = 1
#                 break
#         if f == 0:
#             newList.append(Author(i, 'unknown', 'non_iiitd', [i]))
#             temp.append(newList[len(newList) - 1])
#     if c == 0:
#         rlist+=data[paper]
#         # print(paper, data[paper])
#     # temp is list of authors: Author class

#     objList.append(temp)
# rlist = sorted(rlist, key = rlist.count,reverse = True)
# print(result)
# print(len(objList), count)
# rdict={}
# for i in rlist:
#     if i in rdict.keys():
#         rdict[i]+=1
#     else:
#         rdict[i]=1
# print(rdict)

# ctr = 0
# for combo in objList:
#     for i in range(len(combo)-1):
#         for j in range(i+1,len(combo)):
#             G.addEdge(combo[i],combo[j])



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
# G_=nx.Graph()
# for author in G.graph:
#     G_.add_node(author.name,articles=author.articles,authorCategory=author.authorCategory,
#                 authorType=author.authorType,penNames=author.penNames)

# for i in G.graph:
#     for j in G.graph[i]:
#         G_.add_edge(i.name,j.name,weight=G.graph[i][j])

# import pickle 
# with open('data/graph.pkl','wb') as f:
#     pickle.dump(G_,f)

