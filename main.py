import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com'


def search_text(text_for_analise, list__):
    for word in KEYWORDS:
        compare = re.search(word, text_for_analise)
        if compare is not None:
            compare = compare.group(0)
            if word in list_:
                continue
            else:
                if word == compare:
                    date = article.find("time").attrs.get("title")
                    title = article.find("h2").find('span').text
                    link = article.find("h2")
                    link_ = link.find("a").attrs.get("href")
                    print(f"{date} - {title} - {URL + link_}")
                    list__.append(word)
                    return 'ok'
        else:
            compare = 'not ok'


if __name__ == '__main__':
    response = requests.get('https://habr.com/ru/all/')
    response.raise_for_status()
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all("article", class_="tm-articles-list__item")
    for article in articles:
        publication = article.find_all("p")
        list_ = list()
        query = ''
        for text in publication:
            text_ = text.text.strip()
            query = search_text(text_, list_)
        if query == 'ok':
            continue
        else:
            try:
                title_ = article.find("h2").find('span').text
                query = search_text(title_, list_)
            except AttributeError:
                continue
        if query == 'ok':
            continue
        else:
            tags = article.find_all("a", class_="tm-article-snippet__hubs-item-link")
            for tag in tags:
                tag = tag.text.strip()
                search_text(tag, list_)
