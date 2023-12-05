from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from parsers.utils import str_splitting, json_dump
from db import json_record
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mainDB']
collection = db['mainCollection']

def fetch_data(url, addition,  params, findBy, page_count = 3):
    ua = UserAgent()
    headers = {
        'accepts': 'application/json, text/plain, */*',
        'user-Agent': ua.google,
    }

    order_dict = []

    for num_page in range(1,page_count):
        params['pages'] = num_page
        res = requests.get(url + addition, headers=headers, params=params).text

        if not res:
            continue

        soup = BeautifulSoup(res, 'lxml')
        hrefOrder = soup.find_all(findBy['block'], class_ = findBy['class'])

        for order in hrefOrder:
            order_name = order.find(findBy['oName'], class_ = findBy['oClass']) if findBy['oClass'] else order.find(findBy['oName'])

            order_link = url + f'{order_name.get("href")}'

            price, hourOrProj  = str_splitting(order.find(findBy['order_block'], class_ = findBy['order_class']).text)
            order_dict.append({'name': order_name.text, 'price': price, 'Per&talk': hourOrProj, 'link': order_link})

    for order_json in order_dict:
        collection.insert_many(order_json)
    # json_record(order_dict, url)