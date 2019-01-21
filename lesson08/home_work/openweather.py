
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import os
import wget
import json
import sqlite3
import datetime
import pytemperature


class Builder:
    def __init__(self, article):
        for a, b in article.items():
            setattr(self, a, b)


class WeatherForecast:
    def __init__(self, city):
        self.city = city

    # Read the APP ID from the file
    def appid(self):
        with open('app.id', 'r', encoding='UTF-8') as f:
            return f.readlines()[1]

    # Find the city ID from the file
    def findcityid(self):
        with open('city.list.json', 'r') as f:
            citylist = json.load(f)
            cityid = 0
            for i in citylist:
                if i['name'] == self.city:
                    cityid = i['id']
            if cityid != 0:
                return cityid
            else:
                print("City doesn't exist in database")

    # Pull information from website using 'wget'
    def gethttpdata(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(self.findcityid()) + '&APPID=' + str(self.appid())
        output = 'data/' + self.city + '.json'
        filename = wget.download(url, output)
        return filename

    # Parse the file and return only id, name, forecast_id, date and temperature
    def openforecast(self):
        with open(self.gethttpdata(), 'r', encoding='UTF-8') as f:
            fc_in = json.load(f)
            fc_out = Builder(fc_in)
        return fc_out

    # Create new database and dump data
    def dumptosqldb(self):
        forecast_db = 'forecast.db'
        conn = sqlite3.connect(forecast_db)
        conn.close()
        os.remove(forecast_db)

        with sqlite3.connect(forecast_db) as conn:
            conn.execute("""
                create table forecast (
                    id          integer PRIMARY KEY,
                    name        text,
                    date        date,
                    temperature float,
                    weather_id  integer
                );
                """)
            conn.execute("""
                insert into forecast (id, name, date, temperature, weather_id) VALUES (?,?,?,?,?)""", (
                self.openforecast().id,
                self.openforecast().name,
                datetime.datetime.utcfromtimestamp(int(self.openforecast().dt)).strftime('%Y-%m-%d %H:%M:%S'),
                pytemperature.k2c(self.openforecast().main["temp"]),
                self.openforecast().weather[0]["id"]
                )
            )

    # Read forecast from database and print output
    def readfromsqldb(self):

        forecast_db = 'forecast.db'
        self.dumptosqldb()

        with sqlite3.connect(forecast_db) as conn:
            conn.row_factory = sqlite3.Row

            cur = conn.cursor()
            cur.execute("select * from forecast")
            for row in cur.fetchall():
                print(row)
                id, name, date, temperature, weather_id = row
                return id, name, date, temperature, weather_id

    def __str__(self):
        return "City ID: %s, City Name: %s, Date and Time: %s, Temperature: %s, Weather ID: %s" % (self.readfromsqldb())


print(WeatherForecast(input("Please enter the city name to get Weather Conditions: ")))







