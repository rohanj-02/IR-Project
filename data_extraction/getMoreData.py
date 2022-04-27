import os
import json

filepath = 'C:\\Users\\gitsa\\Documents\\GitHub\\IR-Project\\data\\final\\'
authorsData = os.listdir(filepath)
dataList = []
authorList = []
coauthors = set()
newauthors = {}
ctr = 0
count = 0
for file in authorsData:
    with open(filepath+file, "r") as f:
        dataList.append(json.load(f))
    count += len(dataList[ctr]['articles'])
    authorList.append(dataList[ctr]['author']['name'])
    clist = dataList[ctr]['co_authors']
    for author in clist:
        if 'email' in author.keys() and author['email'] == 'Verified email at iiitd.ac.in':
            coauthors.add((author['name'], author['author_id']))
    ctr += 1
for author in coauthors:
    if author[0] not in authorList:
        newauthors[author[0]] = author[1]
with open('../jsonFiles/new_data.json', 'w') as jsonfile:
    json.dump(newauthors, jsonfile, indent=4)
