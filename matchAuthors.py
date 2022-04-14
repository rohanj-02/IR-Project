import os
import json

filepath='C:\\Users\\gitsa\\Documents\\GitHub\\IR-Project\\data\\final\\'
filepath2='C:\\Users\\gitsa\\Documents\\GitHub\\IR-Project\\data\\final2\\'

authorsData=os.listdir(filepath)
authorsData+=os.listdir(filepath2)
dataList=[]
authorList=[]
allAuthors=[]
ctr=0
count=0
publications=[]
ac=0
tc=0
for file in authorsData:
    try:
        with open(filepath+file, "r") as f:
            dataList.append(json.load(f))
    except:
        with open(filepath2+file, "r") as f:
            dataList.append(json.load(f))
    authorList.append(dataList[ctr]['author']['name'])
    for article in dataList[ctr]['articles']:
        count+=1
        if article['title'] not in publications:
            publications.append(article['title'])
            allAuthors.append(article['authors'])
    ctr+=1

allAuthors=[i.split(',') for i in allAuthors]
diffAuthors=[]
for i in allAuthors:
    tmp=[]
    for j in i:
        k=j.strip()
        if k!='' and k!='...':
            tmp.append(k)
    diffAuthors.append(tmp)
print(len(publications),len(allAuthors),len(diffAuthors))
# print(diffAuthors)
data={}
for i in range(len(publications)):
    data[publications[i]]=diffAuthors[i]
with open('authorData.json','w') as f:
    json.dump(data,f,indent=4)









