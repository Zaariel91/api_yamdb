API YAMDB

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Zaariel91/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirement.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Импортировать базу-данных из csv-файла:

```
python manage.py runscript import_csv
```

Запустить проект:

```
python3 manage.py runserver
```

Авторы: 
<a href="https://github.com/Zaariel91">Николай</a>
<a href="https://github.com/DarkAngeIx">Максим </a>
<a href="https://github.com/Valentina-Kriakova">Валентина</a>
