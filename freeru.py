from bs4 import BeautifulSoup
import json, requests, datetime
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'accepts': 'application/json, text/plain, */*',
    'user-Agent': ua.google
}
order_dict = []
for num_page in range(1, 10):
    try:
        url = f'https://freelance.ru/project/search/pro?c[0]=116&q=&m=or&e=&a=1&v=1&f=&t=&o=1&b=&page={num_page}'
    except:
        print(f'Всего страниц было найдено {num_page}')
        break
    
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    hrefOrder = soup.find_all('div', class_='box-title')
    for order in hrefOrder:
        temporary_dict = {}
        oName = order.find('a', target='_blank')
        order_name = order.find('a', target='_blank').text
        order_link = f'https://freelance.ru/{oName.get("href")}'
        order_price = order.find('div', class_='cost').text
        temporary_dict = {'name': order_name, 'price': order_price, 'link': order_link}
        order_dict.append(temporary_dict)

with open(f'freeru_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as file:
    try:
        json.dump(order_dict, file, indent = 4, ensure_ascii=False)
        print('Заказы получены')
    except:
        print('Заказы получить не удалось или не существует доступных')
