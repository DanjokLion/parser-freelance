import datetime, json, os, re


def str_splitting(arg):
    if not arg[0].isdigit(): return 0, arg
    arg = list(arg)
    dig = []
    tp = []
    for i in arg:
        try:
            a = int(i)
            dig.append(i)
        except:
            tp.append(i)
    return int(''.join(dig)), ''.join(tp).lstrip()

def get_name(url):
    return re.search('\.([a-x]+)\.+[a-z]{2}[a-z]*\/', url).group(1)

def json_dump(order_dict, url):
    name = get_name(url)
    with open(f'./storage/{name}_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as file:
        try:
            json.dump(order_dict, file, indent = 4, ensure_ascii=False)
            print('Заказы получены')
        except:
            print('Заказы получить не удалось или не существует доступных')
    
