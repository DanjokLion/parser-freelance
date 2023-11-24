from bs4 import BeautifulSoup
import json, requests, datetime
from fake_useragent import UserAgent
from scriptsParse import str_splitting

ua = UserAgent()
headers = {
    'accepts': 'application/json, text/plain, */*',
    'user-Agent': ua.google,
}
order_dict = []
for num_page in range(1, 3):
    url = f'https://www.freelancejob.ru/projects/p{num_page}'

    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    hrefOrder = soup.find_all('div', class_='x17')

    for order in hrefOrder:
        temporary_dict = {}
        oName = order.find('a', class_='big')
        order_name = order.find('a', class_='big').text
        order_link = f'https://www.freelancejob.ru/{oName.get("href")}'
        price, hourOrProj  = str_splitting(order.find('div', class_='x18').text)
        temporary_dict = {'name': order_name, 'price': price, 'Per&talk': hourOrProj, 'link': order_link}
        order_dict.append(temporary_dict)


with open(f'freejob_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as file:
    try:
        json.dump(order_dict, file, indent = 4, ensure_ascii=False)
        print('Заказы получены')
    except:
        print('Заказы получить не удалось или не существует доступных')