from bs4 import BeautifulSoup as bs
import requests

url = 'https://flagma.co.uk/ru/my/2337860/vacancies/'

def vacancies(link):
    r = requests.get(link)
    soup = bs(r.text, 'lxml')
    news = soup.find_all('div', class_='article_header')
    print(news)



def news():
    url = 'https://habr.com/ru/news/'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    all_news = soup.find('div', class_='tm-articles-list')
    article = all_news.find('article', class_='tm-articles-list__item')
    print(article)

news()