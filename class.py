
# 1.калькулятор
# def get_largest_expression_result(a, b):
#     x = a + b
#     b = a - b
#     c = a * b
#     i = a / b
#     sum = b, c, i
#     if x > len(sum):
#         return print(x)
#     elif b > sum:
#         return print(b)
#     elif c > sum:
#         return print(c)
#     elif i > sum:
#         return print(i)
#
# get_largest_expression_result(4,6)


# 2.функция сортировки
# def get_three_largest(ls: list) -> list:
#     x = ls
#     x.sort(reverse=True)
#     return x[0:3]
# get_three_largest([2,2,3,5,7,8,9,23])


# 3.Разпонание с картинки
# import pytesseract
# import cv2
# import matplotlib.pyplot as plt
# from PIL import Image

# image = cv2.('test-text.jpeg')
# # получаем строку
# string = pytesseract.image_to_string(image)
# # печатаем
# print(string)

import requests
from bs4 import BeautifulSoup as bs
# import csv
#
# # URL страницы для парсинга
# url = 'https://www.ghanaweb.com/GhanaHomePage/politics/'
#
# # Отправляем GET-запрос на получение страницы
# response = requests.get(url)
#
# # Создаем объект Soup из HTML-кода страницы
# soup = BeautifulSoup(response.content, 'lxml')
#
# # Находим все заголовки и статьи на странице
# articles = soup.find_all('div', class_='news-content')

# парсинг всех страниц доработать
# def parse_site(site_url):
#     all_news = []
#     page = 1
#     while True:
#         link = site_url + '/page/' + str(page)
#         r = requests.get(link)
#         soup = bs(r.text, 'lxml')
#         news = soup.find_all('div', class_='article_header')
#         if len(news) == 0:
#             break
#         x = [c.text for c in news]
#         del x[0]
#         all_news.extend(x)
#         page += 1
#     print(page)

# url = 'https://www.pravda.com.ua/rus/news/'

# parse_site(url)