import pandas as pd
import glob
import time
import os
import pyodbc
import sqlalchemy
import pymssql
import calendar
import re
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from datetime import datetime, timedelta
from warnings import filterwarnings

filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')

engine = create_engine("mssql+pymssql://sa:qwerty123456_@localhost/STAGE", isolation_level="AUTOCOMMIT")
connection = engine.connect()

# last_date
last_date_sql_query = "SELECT MAX(SfFileCreationDate) as last_date FROM [Snapshot].[S15_csv_RU_CALL]" #2024-02-29 13:04:21.000
last_date_df = pd.read_sql_query(last_date_sql_query, engine, parse_dates=['last_date'])
last_date_var = last_date_df['last_date'].iloc[0]
last_date = pd.to_datetime(last_date_var, format="%Y-%m-%d %H:%M:%S.%f") #last_date = datetime.strptime("2024-01-03", '%Y-%m-%d').date() #old for test

c_date = datetime.today().replace(microsecond=0)#.date()
dir = 'E:/DE/Ak/csv/V6/' 
ev_files = glob.glob(dir + "RU_CALL_*-*.*.*.csv") #everyday files
cn_files = glob.glob(dir + "RU_CALL_*'*_consolidated.csv") #consolidate files


ev_csv_list = []
for ev_path in ev_files:
    ev_name = os.path.basename(ev_path)
    #print(f_name)
    # Проверяем дату в имени файла
    try:
        ev_date = datetime.strptime(re.search(r'\d{2}.\d{2}.\d{4}', ev_name).group(), '%m.%d.%Y')#.date()
        #print(f_date)
    except ValueError:
        continue  # Пропускаем файлы с неправильным форматом имени

    if ev_date <= c_date and ev_date > last_date:
        # Загружаем файл в DataFrame
        global df_ev
        df_ev = pd.read_csv(ev_path, index_col=None, header=0, on_bad_lines='warn', sep = ";", engine='python')

        # Далее можно выполнять необходимые операции с DataFrame
        print(f"Загружен файл {ev_name} с датой {ev_date}")
    else:
        # Пропускаем файлы с датой позднее текущей
        print(f"Файл {ev_name} не будет обработан")


#print(df_ev)

cn_csv_list = []
for cn_path in cn_files:
    cn_name = os.path.basename(cn_path)
    #print(cn_name)
    # Проверяем дату в имени файла
    try:
        cn_date = datetime.strptime('01.'+re.search(r'\d{2}\'\d{4}', cn_name).group(), "%d.%m\'%Y")#.date()
        #print(cn_date)
    except ValueError:
        continue  # Пропускаем файлы с неправильным форматом имени

    if cn_date <= c_date and cn_date > last_date:
        # Загружаем файл в DataFrame
        global df_cn
        df_cn = pd.read_csv(cn_path, index_col=None, header=0, on_bad_lines='warn', sep = ";", engine='python')
        #print(df_cn)

        # Далее можно выполнять необходимые операции с DataFrame
        print(f"Загружен файл {cn_name} с датой {cn_date}")
    else:
        # Пропускаем файлы с датой позднее текущей
        print(f"Файл {cn_name} не будет обработан")


#print(df_cn)

