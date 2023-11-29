import sqlite3, json
from parsers.utils import get_name

conn = sqlite3.connect('maindb.db')

cur = conn.cursor

cur.execute(
'''
    CREATE TABLE jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        name TEXT
        price TEXT
        PerTalk TEXT
        link TEXT
    )
''')

def json_record(order_dict, url):
    name = get_name(url)

    with open('./storage/{name}_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        cur.execute('INSERT INTO jobs (name, price, PerTalk, link) VALUES (?, ?, ?, ?)', 
                    item['name'], item['price'], item['Per&Talk'], item['link'])

    conn.commit()
    conn.close()
    pass