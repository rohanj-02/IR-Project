import json
import os


class Author:
    def __init__(self, name, authorType, authorCategory, penNames, articles=None):
        self.name = name
        self.authorType = authorType
        self.articles = articles
        self.authorCategory = authorCategory
        self.penNames = penNames
    def printAuthor(self):
        print('Name =',self.name,'Type =',self.authorType, 'Category =',self.authorCategory, 'NameList =',self.penNames)

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
filepath = 'C:\\Users\\gitsa\\Documents\\GitHub\\IR-Project\\data\\final\\'
filepath2 = 'C:\\Users\\gitsa\\Documents\\GitHub\\IR-Project\\data\\final2\\'
facultyData = os.listdir(filepath)
studentData = os.listdir(filepath2)
facultyList = []
studentList = []
for file in facultyData:
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
    if name == "gajendra ps raghava":
        nlist.append('GPS Raghava')
        nlist.append('G Raghava')
        nlist.append('GP Raghava')
        nlist.append('Gs Raghava')
    elif len(temp) == 2:
        nlist.append(temp[0] + ' '+temp[1][0])
        nlist.append(temp[0][0] + ' '+temp[1])
    elif len(temp) == 3:
        nlist.append(temp[0][0] + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' '+temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' '+temp[1] + ' ' + temp[2])
        nlist.append(temp[0] + ' '+temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' '+temp[1][0] + ' ' + temp[2][0])
        nlist.append(temp[0] + ' '+temp[1] + ' ' + temp[2][0])
        nlist.append(temp[0] +' ' +temp[1][0] + temp[2][0])
        nlist.append(temp[0][0] +' '+ temp[1] + ' ' + temp[2][0])
    elif len(temp) == 4:
        nlist.append(temp[0][0] + temp[1][0] + temp[2][0] + ' ' + temp[3])
    else:
        print('Not Processed')
    facultyList.append(Author(name.lower(),'faculty','iiitd',nlist, author['articles']))


for file in studentData:
    with open(filepath2 + file, "r") as f:
        author = json.load(f)
    name = author['author']['name']
    nlist=[name.lower()]
    name=name.lower()
    temp=name.split(' ')
    if len(temp)==1:
        pass
    elif len(temp)==2:
        nlist.append(temp[0] + ' '+temp[1][0])
        nlist.append(temp[0][0] + ' '+temp[1])
    elif len(temp)==3:
        nlist.append(temp[0][0] + temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' '+temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' ' + temp[2])
        nlist.append(temp[0][0] + ' '+temp[1] + ' ' + temp[2])
        nlist.append(temp[0] + ' '+temp[1][0] + ' ' + temp[2])
        nlist.append(temp[0] + ' '+temp[1][0] + ' ' + temp[2][0])
        nlist.append(temp[0] + ' '+temp[1] + ' ' + temp[2][0])
        nlist.append(temp[0] +' ' +temp[1][0] + temp[2][0])
        nlist.append(temp[0][0] +' '+ temp[1] + ' ' + temp[2][0])
    elif len(temp)==4:
        nlist.append(temp[0][0]+temp[1][0]+temp[2][0]+' '+temp[3])
    else:
        print('Not Processed')
    studentList.append(Author(name.lower(),'student', 'iiitd',nlist,author['articles']))

G.addEdge(studentList[0],studentList[3])
G.addEdge(studentList[3],studentList[5])
G.addEdge(studentList[3],studentList[5])
print(G.graph)
# for s in facultyList:
#     s.printAuthor()

# for file in facultyData:
#     with open(filepath + file, "r") as f:
#         author = json.load(f)
#     facultyList.append(author['author']['name'])
