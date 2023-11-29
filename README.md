FrostRay Parser Freelance
-----------------------------------
### Основные файлы:

* `index.py` - парсинг заказов в json файлы
* `main.py` - файл сервера fastapi

### Установка зависимостей
    pip install
    fastapi, fake_useragent, bs4, requests, pydantic

    cd <project_dir>/client
    npm install
    
### Запуск:
    cd <project_dir>/server
    python index.py
    uvicorn main:app --host <x.x.x.x> --port <port>

    cd <project_dir>/client
    npm start
