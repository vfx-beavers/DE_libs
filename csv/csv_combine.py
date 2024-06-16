from datetime import datetime
import glob
import pandas as pd

pd.set_option('display.max_colwidth', None)

month = 10
files = glob.glob(f"E:/DE/Ak/csv/V4/tb_orders_2022.{month}.*.csv")
print("\n".join(files))

df = pd.concat([pd.read_csv(f) for f in glob.glob(f"E:/DE/Ak/csv/V4/tb_orders_2022.{month}.*.csv")], axis=0, ignore_index=True)
print(df)

#s = pd.Series(['LatitudeOnSumbit', 'LongitudeOnSubmit'])
#pd.to_numeric(s, errors='coerce', downcast="float")

print(df.dtypes)

# df_sales.to_csv('/home/sales.csv', index=False, encoding='utf-8-sig')
#datetime.fromisoformat('2011-11-04')
#datetime.fromisoformat('2011-11-04T00:05:23')
#datetime.datetime(2011, 11, 4, 0, 5, 23)