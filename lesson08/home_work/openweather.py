
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
import re
import pycountry_convert


class Builder:
    def __init__(self, article):
        for a, b in article.items():
            setattr(self, a, b)


class GetCityForecast:
    def __init__(self, country, city):
        self.country = country
        self.city = city
        with open('app.id', 'r', encoding='UTF-8') as f:
            self._appid = f.readlines()[1]

    def _findcityid(self):
        """Find the city ID from the file"""
        with open('city.list.json', 'r') as f:
            citylist = json.load(f)
            cityid = 0
            for j in citylist:
                if j['country'] == self.country and j['name'] == self.city:
                    cityid = j['id']
            if cityid != 0:
                return cityid
            else:
                print("City or country doesn't exist in database")
                exit(1)

    def gethttpdata(self):
        """Pull information into file from website using 'wget'"""
        url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(
            self._findcityid()) + '&&units=metric&APPID=' + str(self._appid)
        outputfile = 'data/' + self.city + '.json'
        if os.path.exists(outputfile):
            os.remove(outputfile)
        try:
            wget.download(url, outputfile)
        except:
            print("Couldn't download file. Exiting")
            exit(1)

    def _parsehttpdata(self):
        with open(os.path.join('data/', self.city + '.json'), 'r', encoding='UTF-8') as f:
            httpdatain = json.load(f)
            httpdataout = Builder(httpdatain)
        return httpdataout

    def dumptosqldb(self):
        """Create new database and dump data"""
        forecast_db = 'forecast.db'
        conn = sqlite3.connect(forecast_db)
        conn.close()

        with sqlite3.connect(forecast_db) as conn:
            conn.execute("""
                create table IF NOT EXISTS forecast (
                    id          integer PRIMARY KEY,
                    country     text,
                    name        text,
                    date        date,
                    temperature float,
                    weather_id  integer
                );
                """)
            conn.execute("""
                insert or replace into forecast (id, country, name, 
                date, temperature, weather_id) VALUES (?,?,?,?,?,?)""", (
                self._parsehttpdata().id,
                self._parsehttpdata().sys["country"],
                self._parsehttpdata().name,
                datetime.datetime.utcfromtimestamp(int(self._parsehttpdata().dt)).strftime('%Y-%m-%d %H:%M:%S'),
                self._parsehttpdata().main["temp"],
                self._parsehttpdata().weather[0]["id"]
                )
            )

    def readfromsqldb(self):
        """Read forecast from database and print output"""
        forecast_db = 'forecast.db'

        with sqlite3.connect(forecast_db) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from forecast where id={}".format(self._parsehttpdata().id))
            for row in cur.fetchall():
                id, country, name, date, temperature, weather_id = row
                return id, country, name, date, temperature, weather_id

    def __str__(self):
        self.gethttpdata()
        self.dumptosqldb()
        return "City ID: %s, Country Code: %s, " \
               "City Name: %s, Date and Time: %s, " \
               "Temperature: %s C, Weather ID: %s" % (self.readfromsqldb())


print(GetCityForecast(input("Please enter the country code: "),
                      input("Please enter the city name to get Weather Conditions: ")))











