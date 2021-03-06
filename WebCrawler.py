import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://buckyroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a', {'class': 'item-name'}):
            href = link.get('herf')
            print(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.find_all('a', {'class': 'item-name'}):
        print(item_name.string)
    for link in soup.find_all('a'):
        href = "https://buckyroom.org" + link.get('href')
        print(href)


trade_spider(1)
