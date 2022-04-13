import os
import json

OUT_DIR = "./data"

with open("./faculty_data.json", "r") as f:
    faculty_data = json.load(f)

author_ids = [v for k, v in faculty_data.items()]
author_ids = list(filter(lambda x: x != "", author_ids))

for a_id in author_ids:
    filtered = list(filter(lambda x: x.find(a_id) != -1, os.listdir(OUT_DIR)))
    if len(filtered) == 0:
        print(f"No documents for {a_id}")
        continue
    final = {}
    with open(f"{OUT_DIR}/{f}", "r") as infile:
        data = json.load(infile)
    final = data
    for doc in filtered:
        with open(f"{OUT_DIR}/{doc}", "r") as infile:
            data = json.load(infile)
        final["articles"] += data["articles"]
        final["co-authors"] += data["co-authors"]

    # remove duplicate co-authors
    ids = [x["author_id"] for x in final["co-authors"]]
    ids = list(set(ids))
    final_co_authors = []
    for idx in range(len(final["co-authors"])):
        if final["co-authors"][idx]["author_id"] in ids:
            final_co_authors.append(final["co-authors"][idx])
            ids.remove(final["co-authors"][idx]["author_id"])
    final["co-authors"] = final_co_authors

    with open(f"{OUT_DIR}/final/{a_id}.json", "w") as outfile:
        json.dump(final, outfile, indent=4)
