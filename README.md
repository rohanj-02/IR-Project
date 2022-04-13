# Running the project

Use the following commands to run the project:

```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 <filename>
```

- Using env is optional but will help keep your laptop clean.
- Above commands are for linux, should work in mac.
- If you are using windows, copilot generated these commands (idk if they work):

```
virtualenv venv
source venv\Scripts\activate
pip3 install -r requirements.txt
python3 <filename>
```

# Directory Structure

## ./data

Files kept in the "./data/" directory are scraped files from serpapi. These are the output of fetch_prof_data.py file

## ./data/final

Files kept in the "./data/final/" directory are the merged versions of the scraped files from the serpapi. These are the output of merge_prof_data.py file

## irins_scrape.py

The file scrapes author ids of professors and populates that into faculty_data.json

## fetch_prof_data.py

The file takes the author ids from faculty_data.json and scrapes the data from serpapi and saves it in the ./data/ directory

## merge_prof_data.py

The file merges the scraped data from the ./data/ directory and saves it in the ./data/final/ directory. All the articles are appended directly and co-authors are also appended but they are de-duplicated based on the author id of each co-author.
