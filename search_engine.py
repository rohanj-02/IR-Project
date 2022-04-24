import json
from tqdm import tqdm

def getPaperList():
    # read json file
    with open('jsonFiles/unique_articles.json') as json_file:
        papers = json.load(json_file)
    res = []
    for paper in papers:
        cur = {}
        cur['title'] = paper['title']
        cur['authors'] = paper['processed_authors']
        if 'info' in paper.keys():
            if type(paper['info']) == type({}) and 'bib' in paper['info'].keys():
                if 'abstract' in paper['info']['bib'].keys():
                    cur['abstract'] = paper['info']['bib']['abstract']
        res.append(cur)
    # papers = map(lambda x: {
    #     'title': x['title'], 
    #     'authors': x['processed_authors'], 
    #     "abstract": x['info']['bib']['abstract'] 
    #     }, papers)
    return res

PAPERS = getPaperList()

def get_papers(query):
    """
    This function takes a query and returns a list of papers that match the query.
    """
    papers = PAPERS
    res = []
    # papers = [paper for paper in papers if query in paper['title']]
    for i in tqdm(range(len(papers))):
        paper = papers[i]
        if query in paper['title']:
            res.append(paper)
    return res

def get_prof_freq(res):
    """
    This function takes a list of papers and returns a dictionary of the frequency of each professor in the list.
    """
    prof_freq = {}
    for paper in res:
        for author in paper['authors']:
            if author in prof_freq.keys():
                prof_freq[author] += 1
            else:
                prof_freq[author] = 1
    # get sorted list of professors
    prof_freq = sorted(prof_freq.items(), key=lambda x: x[1], reverse=True)
    return prof_freq

res = get_papers('networks')
print(len(res))
print(get_prof_freq(res))
