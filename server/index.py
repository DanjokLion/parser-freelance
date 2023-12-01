from parsers.fetch_tasks import fetch_data
import subprocess

sites = [
    {
        'url': 'https://freelance.habr.com/',
        'addition': 'tasks',
        'params' : {
            'only_with_price':'true',
            'categories': 'development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other',
            'pages': ''
        },
        'findBy': {'block': 'article', 'class': 'task task_list', 'oName': 'a', 'oClass': '','order_block': 'span', 'order_class': 'count'}
    },
    {
        'url': 'https://www.freelancejob.ru/',
        'addition': 'projects/p',
        'params' : {},
        'findBy': {'block': 'div', 'class': 'x17', 'oName': 'a','oClass': 'big', 'order_block': 'div', 'order_class': 'x18'}
    }
]

if __name__ == '__main__':
    for site in sites:
        fetch_data(site['url'], site['addition'], site['params'], site['findBy'])
    subprocess.run(['uvicorn', 'main:app', '--host', '127.0.0.1', '--port', '8000'])