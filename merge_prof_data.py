import os
import json

OUT_DIR = "./data"

with open("jsonFiles/faculty_data.json", "r") as f:
    faculty_data = json.load(f)

author_ids = [v for k, v in faculty_data.items()]
author_ids = list(filter(lambda x: x != "", author_ids))

for a_id in author_ids:
    filtered = list(filter(lambda x: x.find(a_id) != -1, os.listdir(OUT_DIR)))
    if len(filtered) == 0:
        print(f"No documents for {a_id}")
        continue
    final = {}
    with open(f"{OUT_DIR}/{filtered[0]}", "r") as infile:
        data = json.load(infile)
        final = data
    # print(a_id)
    # print(final.keys())
    if "articles" not in final.keys():
        final["articles"] = []
    if "co_authors" not in final.keys():
        final["co_authors"] = []
    for doc in filtered[1:]:
        with open(f"{OUT_DIR}/{doc}", "r") as infile:
            data = json.load(infile)
            if "articles" in data.keys():
                final["articles"] += data["articles"]
            if "co_authors" in data.keys():
                final["co_authors"] += data["co_authors"]

    # remove duplicate co_authors
    ids = [x["author_id"] for x in final["co_authors"]]
    ids = list(set(ids))
    final_co_authors = []
    for idx in range(len(final["co_authors"])):
        if final["co_authors"][idx]["author_id"] in ids:
            final_co_authors.append(final["co_authors"][idx])
            ids.remove(final["co_authors"][idx]["author_id"])
    final["co_authors"] = final_co_authors
    final["search_metadata"]["total_articles"] = len(final["articles"])
    final["search_metadata"]["total_co_authors"] = len(final["co_authors"])

    with open(f"{OUT_DIR}/final/{a_id}.json", "w") as outfile:
        json.dump(final, outfile, indent=4)
