from serpapi import GoogleSearch
import os
import json
from tqdm import tqdm

OUT_DIR = "./data"
API_KEYS = [
    'b4e0fce698af7831793b240383c8f879213b2137a177e2d683620ca081f342a3'
    '70c1ee921bb0a2b35a6922a33ee673ca0cf0381811f116fe8f4beb7097d326a1',
    '32f82bcb8ddd61f38c8a5c6e09b95f2a3b7153420e3f248d936bf85dbab0c72e',
    'd3f9461b5f25451d6c1f2a66bc7d749bc6ee8abb5de88818bede8c27d944da90',
    '9d852139883524e8c5cd0ae15856a6dd6bf43d1c2516784ff68b3dcb35acfe7f'
]
API_KEY = API_KEYS[0]

# load author ids
with open("./faculty_data.json", "r") as f:
    faculty_data = json.load(f)

author_ids = [v for k, v in faculty_data.items()]
author_ids = list(filter(lambda x: x != "", author_ids))
# ["WAChZv4AAAAJ"]


def already_exist(file_name):
    filtered = list(filter(lambda x: x.find(
        file_name) != -1, os.listdir(OUT_DIR)))
    return len(list(filtered)) > 0


for idx in tqdm(range(len(author_ids))):
    a_id = author_ids[idx]
    start = 0
    if already_exist(a_id):
        print(f"Skipping {a_id}")
        continue
    while True:
        params = {
            "api_key": API_KEY,
            "engine": "google_scholar_author",
            "author_id": a_id,
            "hl": "en",
            "start": start,
            "num": 100,
        }
        search = GoogleSearch(params)
        print("Searching for author id: " + a_id)
        results = search.get_dict()
        if "error" in results:
            print(results["error"])
            print("Changing API Key")
            if API_KEYS.index(API_KEY) + 1 >= len(API_KEYS):
                print("No more API Keys")
                break
            API_KEY = API_KEYS[API_KEYS.index(API_KEY) + 1]
        else:
            with open(f"{OUT_DIR}/{a_id}_{start // 100 + 1}.json", "w") as outfile:
                json.dump(results, outfile, indent=4)
            try:
                if len(results["articles"]) == 100:
                    start += 100
                else:
                    break
            except Exception as e:
                print(e)
                print(results)
                break
    print(f"{a_id} done")
