import json
from cso_classifier import CSOClassifier

clfmodel = CSOClassifier(modules="both", enhancement="first", explanation=True)
with open('jsonFiles/publicationData.json', 'r') as f:
    data = json.load(f)
ctr = 0
for paper in data:
    result = clfmodel.run(paper)
    data[paper]['domain']=result['enhanced']
    ctr+=1
    if ctr%100==0:
        print(ctr,'completed')
with open('jsonFiles/publicationData.json', 'w') as f:
    json.dump(data,f,indent=4)