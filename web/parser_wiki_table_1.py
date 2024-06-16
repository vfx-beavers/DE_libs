import pandas as pd
import requests
from bs4 import BeautifulSoup
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# GET-запрос к веб-странице
url = 'https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B9%D0%BE%D0%BD%D1%8B_%D0%B8_%D0%BF%D0%BE%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B'
response = requests.get(url)
print(response.status_code)

# Парсинг HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Находим таблицу на странице
table = soup.find_all('table')[0]

# Преобразование HTML-таблицы в DataFrame
df = pd.read_html(str(table))[0]

# Удаление столбцов и строчек
df.drop(['Флаг', 'Герб', 'Название cоответствующего  внутригородского  муниципального образования:  муниципального округа / поселения /  городского округа[5]'], axis=1, inplace=True)
df.drop(df.index[range(125, 146)], axis=0, inplace=True)

# Переименование столбцов
df.columns.values[0] = "id"
df.columns.values[1] = "district"
df.columns.values[2] = "adm_area"
df.columns.values[3] = "area_skm"
df.columns.values[4] = "population"
df.columns.values[5] = "density_skm"
df.columns.values[6] = "living_all_sqm"
df.columns.values[7] = "living_pp_sqm"

# Чистка полей и корректировка значений
df['population'] = df['population'].str.replace('↘', '', regex=False)
df['population'] = df['population'].str.replace('↗','', regex=False)
df['population'] = df['population'].str.replace(r'\s*', '', regex=True)
df['population'] = df['population'].astype('int64')
df['area_skm'] = df['area_skm'].astype('float64').div(100).round(2)
df['living_all_sqm'] = df['living_all_sqm'].mul(1000).round(2)
df['living_pp_sqm'] = df['living_pp_sqm'].div(10).round(2)

#df.info()
#print(df)

engine = create_engine('postgresql+psycopg2://pguser:pgpwd@localhost:15432/de')
con = engine.connect()

df.to_sql('stg_district', con=engine, if_exists='append', index=False, schema='public', method='multi')

#print('отправлено')
