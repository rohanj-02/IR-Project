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

## Running the Flask server

- After installing the requirements, run the following command to start the server:

```
python3 SearchBox.py
```

Go to http://localhost:8000/ to see the search box.

# Directory Structure

## ./data

Files kept in the "./data/" directory are scraped files from serpapi. These are the output of fetch_prof_data.py file

## ./data/final

Files kept in the "./data/final/" directory are the merged versions of the scraped files from the serpapi. These are the output of merge_prof_data.py file

## ./data_extraction

### article_author_update.py

Adds abstract to the research papers in the data/final2 directory and saves them in data/author_update directory

### fetch_prof_data.py

The file takes the author ids from faculty_data.json and scrapes the data from serpapi and saves it in the ./data/ directory

### irins_scrape.py

The file scrapes author ids of professors and populates that into faculty_data.json

### merge_prof_data.py

The file merges the scraped data from the ./data/ directory and saves it in the ./data/final/ directory. All the articles are appended directly and co-authors are also appended but they are de-duplicated based on the author id of each co-author.

### map_author_to_pubs.py

The file extracts all the authors in each publication and adds them to the publication data and saves it in data/author_update2 directory.

### getMoreData.py

It is used to extract data from scholar of students of iiitd

### getAbstract.py

It is used to prepare a dict containing title abstract author

### matchAuthors.py

It is used to get a structured dataset of authors and paper

## static/

The directory contains static files for frontend (css, js files)

## templates/

The directory contains the html templates for the frontend

## graph.py

This file contains the graph generation code. A graph is first generated using our custom Graph class and is then converted into a networkx graph for easier analysis.

## domainModelling.py

It extracts the domain of the research publication based on the abstract and title of the paper.

## metrics.ipynb

It evaluates the scoes of researcher on the new metric which we propose.

## metrics.ipynb

It generates the metrics for the homogenous and heterogenous graph that we have made.

## search_engine.py

The file contains the search engine code for TF-IDF based ranking of recommending research papers based on a given query.

## SearchBox.py

The file contains the Flask server code.

## visualization.py

The file is used to display the visualization of the subgraphs made based on the domains.

## jsonFiles/

The directory contains processed data in the form of json files

### authorData.json

Stores the name of the research paper published and a list of the authors

### faculty_data.json

Stores the mapping of professors to their google scholar IDs

### new_data.json

Stores the mapping of IIITD Students to their google scholar IDs

### publicationData.json

Stores basic details about a paper such as authors, abstract and domains

### unique_articles.json

Contains all the details of the published articles in our data

## Models/

The directory contains the pickled models used for the analysis

### graph.pkl

NetworkX graph

### graphBlockchain.pkl

NetworkX subgraph for the blockchain domain

### graphComputerNetworks.pkl

NetworkX subgraph for the computer networks domain

### graphComputerVision.pkl

NetworkX subgraph for the computer vision domain

### graphFacialRecognition.pkl

NetworkX subgraph for the facial recognition domain

### graphMathematics.pkl

NetworkX subgraph for the mathematics domain

### postings.p

Posting list of the abstract of all the papers

### res.p

## Reports/

Our reports for the previous submissions for the project.
