from bs4 import BeautifulSoup
import json, requests, datetime
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'accepts': 'application/json, text/plain, */*',
    'user-Agent': ua.google,
}
order_dict = {}

for num_page in range(1,30):
    try:
        url = f'https://freelance.habr.com/tasks?only_with_price=true&categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other&page={num_page}'
    except:
        print(f'Всего страниц было найдено {num_page}')
        break

    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    hrefOrder = soup.find_all('article', class_='task task_list')

    for order in hrefOrder:
        oName = order.find('a')
        order_name = order.find('a').text
        order_link = f'https://freelance.habr.com/{oName.get("href")}'
        order_price = order.find('span', class_='count').text
        
        order_dict[order_name] = [order_price, order_link]


with open(f'order_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as file:
    try:
        json.dump(order_dict, file, indent = 4, ensure_ascii=False)
        print('Заказы получены')
    except:
        print('Заказы получить не удалось или не существует доступных')