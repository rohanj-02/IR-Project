from bs4 import BeautifulSoup
import requests
import json
import os
from tqdm import tqdm
from scholarly import scholarly
from scholarly import ProxyGenerator
import copy

pg = ProxyGenerator()
# success = pg.ScraperAPI("81715ec6176c5b721005c1e1c0943dd6")
success = pg.ScraperAPI("ca007cedd5337eeb898c34b77951b901")
# success = pg.FreeProxies()
print("Proxy connection status: ", success)
scholarly.use_proxy(pg)

IN_DIR = "../data/final2"
OUT_DIR = "../data/author_update"

for doc_id in os.listdir(IN_DIR):
    if os.path.exists(f"{OUT_DIR}/{doc_id}"):
        print("Exists")
        continue
    doc = json.load(open(f"{IN_DIR}/{doc_id}", "r"))
    new_articles = []
    i = 0
    for idx in tqdm(range(len(doc['articles']))):
        article = doc['articles'][idx]
    # for article in doc["articles"]:
        meta = {}
        try:

            query_str = article["title"]
            search_query = scholarly.search_pubs(query_str)
            meta = ""
            for query in search_query:
                meta = query
                break
            # req = requests.get(article["link"], proxies = {
            #     "https": f'http://{PROXIES[i]}'
            # })
            # soup = BeautifulSoup(req.content, "lxml")
            # table = soup.find(id="gsc_oci_table")
            # while table is None:
            #     req = requests.get(article["link"], proxies = {
            #         "https": f'http://{PROXIES[i]}'
            #      })
            #     soup = BeautifulSoup(req.content, "lxml")
            #     table = soup.find(id="gsc_oci_table")
            #     i += 1

            # fields = table.find_all(class_="gs_scl")
            # for field in fields:
            #     key = field.find(class_="gsc_oci_field").text
            #     value = field.find(class_= "gsc_oci_value").text
            #     meta[key] = value
            # TO_DELETE = ["Total citations", "Scholar articles", "Description"]
            # for key in TO_DELETE:
            #     if key in meta:
            #         del meta[key]
        except Exception as e:
            print(e)
            print(article['link'])
        print(meta)
        article["info"] = meta
        new_articles.append(article)
        new_doc = copy.deepcopy(doc)
        new_doc["articles"] = new_articles
        with open(f"{OUT_DIR}/{doc_id}", "w") as outfile:
            json.dump(new_doc, outfile, indent=4)
