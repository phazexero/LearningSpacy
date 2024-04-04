import bs4
import sys
import requests

wiki_page = 'india'
res = requests.get(f'https://en.wikipedia.org/wiki/{wiki_page}' )
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,"html.parser")

with open(wiki_page+".txt", "w", encoding="utf-8") as f:
    for i in wiki.select('p'):
        f.write(i.getText())