import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all('a', {'class': 'index_singleListingTitles'}):
        content = post_text.string
        word = content.lower().split()
        for each_word in word:
            print(each_word)
            word_list.append(each_word)


start('')
