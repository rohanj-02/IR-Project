import os
import json

dirs = os.listdir("./data/author_update")
all_dirs = os.listdir("./data/final")
left = set(all_dirs) - set(dirs)

count = 0
for doc in left:
    # open file
    with open(f"./data/final/{doc}", "r") as f:
        data = json.load(f)
        print(len(data["articles"]))
        count += len(data["articles"])
print("Total count: ", count)