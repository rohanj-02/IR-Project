from serpapi import GoogleSearch
import os,json
params = {
  "api_key": '32f82bcb8ddd61f38c8a5c6e09b95f2a3b7153420e3f248d936bf85dbab0c72e',
  "engine": "google_scholar_author",
  "author_id": "WAChZv4AAAAJ",
  "hl": "en",
}
search = GoogleSearch(params)
results = search.get_dict()
with open("sample.json", "w") as outfile:
  json.dump(results, outfile)
for article in results['articles']:
  article_title = article['title']
  article_link = article['link']
  article_authors = article['authors']
  article_publication = article['publication']
  cited_by = article['cited_by']['value']
  cited_by_link = article['cited_by']['link']
  article_year = article['year']
  print(f"Title: {article_title}\nLink: {article_link}\nAuthors: {article_authors}\nPublication: {article_publication}\nCited by: {cited_by}\nCited by link: {cited_by_link}\nPublication year: {article_year}\n")

f = open('sample.json')
data = json.load(f)
print(data)