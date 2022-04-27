from bs4 import BeautifulSoup
from regex import F
import requests
import json

req = requests.get("https://iiitd.irins.org/")
soup = BeautifulSoup(req.content, "lxml")

depLinks = []
for link in soup.findAll('a'):
    s = link.get('href')
    if isinstance(s, str) and s.find("https://iiitd.irins.org/faculty/index/Department+") != -1:
        depLinks.append(s)


profLinks = []

for deplink in depLinks:
    req = requests.get(deplink)
    soup = BeautifulSoup(req.content, "lxml")
    for link in soup.findAll('a'):
        s = link.get('href')
        if isinstance(s, str) and s.find("https://iiitd.irins.org/profile/") != -1:
            profLinks.append(s)


faculty_data = {}

empty = []

for proflink in profLinks:
    req = requests.get(proflink)
    soup = BeautifulSoup(req.content, "lxml")
    name = ""
    id = ""
    for ul in soup.findAll('ul', {'class': 'name-location'}):
        name = ul.find('strong').text.strip()
    if name == "":
        for div in soup.findAll('div', {'class': 'name-location'}):
            name = div.find('strong').text.strip()
            break

    for span in soup.findAll('span', {'id': 'i_google_sid'}):
        id = span.find('a').text.strip()

    faculty_data[name] = id

    if id == "" and name != "":
        empty.append(name)

    if name == "":
        print(proflink)


with open("../data/empty.txt", 'w') as out:
    for name in empty:
        out.write(name+'\n')

# with open("facutly_data.json", "w") as outfile:
#     json.dump(faculty_data, outfile)
