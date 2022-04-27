import json
from tqdm import tqdm
import os
import math
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


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


def preprocess(text):
    """Takes a document and preprocesses the text"""
    # case folding and tokenize text
    tokens = list(map(lambda x: x.lower(), word_tokenize(text)))
    # remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]

    # Lemmatization
    lem = WordNetLemmatizer()
    tempRes = []
    for tok in filtered_tokens:
        lmtok = lem.lemmatize(tok)
        tempRes.append(lmtok)

    # remove punctuation marks
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tempRes]
    stripped = [w for w in stripped if w.strip() != '']

    return " ".join(stripped)


PAPERS = getPaperList()
DATA_PATH = "./data"


def getDocumentList():
    """Returns a list of all documents in the data folder"""
    return os.listdir(DATA_PATH)


def makePostingsList(doc_list):
    """
    Opens all documents in the data doc_list parameter and creates a postings list
    """
    postings_list = {}  # Dictionary of word: list of document ids
    length = len(doc_list)
    for idx in tqdm(range(length)):
        doc = doc_list[idx]
        if 'abstract' in doc.keys():
            text = doc['abstract']
        else:
            text = doc['title']
        preprocessed_text = preprocess(text)
        for word in preprocessed_text.split():
            if word not in postings_list:
                postings_list[word] = set()
                postings_list[word].add(idx)
            else:
                postings_list[word].add(idx)
    print("Validating list sorted")
    for word, posting in postings_list.items():
        postings_list[word] = sorted(posting)
    print("Posting lists sorted")
    return postings_list


doc_list = PAPERS
num_docs = len(doc_list)
postings = makePostingsList(doc_list)
vocab = postings.keys()


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


def dotProduct(query_vector, tf_idf):
    """
    Returns the dot product of the query vector dictionary and the tf-idf dictionary
    """
    dot_product = {}
    for doc in doc_list:
        dot_product[doc] = 0
        for word in vocab:
            dot_product[doc] += query_vector[word] * tf_idf[doc][word]
    return dot_product


def dotSum(dot_product):
    """
    Returns the dot sum of the dot product dictionary
    """
    dot_sum = 0
    for key in dot_product.keys():
        dot_sum += dot_product[key]
    return dot_sum


def findTopDocuments(tfidfscore):
    """
    Finds the top 5 documents according to the tfidf query vector
    """
    top_docs = sorted(tfidfscore.items(), key=lambda x: x[1], reverse=True)[:5]
    return [idx for idx in top_docs]


def getPostings(inp, postings):
    """
    Returns the postings list for the given word
    """
    if type(inp) == str:
        # print("Getting postings for word: ", inp, postings.get(inp, []))
        return postings.get(inp, [])
    else:
        # print("Getting postings for word: ", inp, inp)
        return inp


def inverseDocFrequency(word, postings):
    """
    Returns the inverse document frequency for the given word
    """
    return math.log(num_docs / (len(getPostings(word, postings))+1))


def tfIdf(vocab, doc_list, postings):
    """
    Returns the tf-idf dictionary for the given word and document
    """
    tf_idf = {}
    for doc in doc_list:
        doc = doc['title']
        tf_idf[doc] = {}
        for word in vocab:
            tf_idf[doc][word] = 0

    length = len(doc_list)
    for idx in tqdm(range(length)):
        doc = doc_list[idx]
        if 'abstract' in doc.keys():
            text = doc['abstract']
        else:
            text = doc['title']
        preprocessed_text = preprocess(text).split()
        doc_text = set(preprocessed_text)
        freq = len(preprocessed_text)
        for word in doc_text:
            tf_idf[doc['title']][word] = (preprocessed_text.count(
                word)/freq) * inverseDocFrequency(word, postings)
    return tf_idf


tf_idf = tfIdf(vocab, doc_list, postings)


def getTfIdfArticles(query):
    """
    This function takes a query and returns a list of papers that match the query.
    """
    papers = PAPERS
    query = input("Enter query string: ")
    # query = "I tuned into this group"
    query = preprocess(query)
    query_set = set(query.split())
    # print(query_set)

    query_vector = {}
    for word in vocab:
        query_vector[word] = 0
    for word in query_set:
        query_vector[word] = 1

    tf_score = dotProduct(query_vector, tf_idf)
    final_score = dotSum(tf_score)
    top_docs = findTopDocuments(tf_score)
    return final_score, top_docs


res = get_papers('networks')
print(len(res))
print(get_prof_freq(res))
