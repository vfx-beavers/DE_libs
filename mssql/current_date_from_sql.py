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

last_date_sql_query = "SELECT MAX(SfFileCreationDate) as last_date FROM [Snapshot].[S15_csv_RU_CALL]" #2024-02-29 13:04:21.000
last_date_df = pd.read_sql_query(last_date_sql_query, engine, parse_dates=['last_date'])
#print(last_date_df)
last_date_var = last_date_df['last_date'].iloc[0]
last_date = pd.to_datetime(last_date_var, format="%Y-%m-%d %H:%M:%S.%f")
print('last date',last_date)
c_date = datetime.today().replace(microsecond=0)#.date()
print('c_date',c_date)
ev_date = datetime.strptime(re.search(r'\d{2}.\d{2}.\d{4}', "RU_CALL_Feb2024-02.01.2024.csv").group(), '%m.%d.%Y')#.date()
print('ev_date',ev_date)



