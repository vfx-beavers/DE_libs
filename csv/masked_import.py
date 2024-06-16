import glob
import pandas as pd

pd.set_option('display.max_colwidth', None)

files = glob.glob(r'E:/DE/xxxx/source_csv_folder/V1/tb_*.csv')
print("\n".join(files))


df_outer_join = pd.concat([pd.read_csv(f) for f in glob.glob(r'E:/DE/xxxx/source_csv_folder/V1/tb_*.csv')], axis=0, ignore_index=True)
print(df_outer_join)

df_inner_join = pd.concat([pd.read_csv(f) for f in glob.glob(r'E:/DE/xxxx/source_csv_folder/V1/tb_*.csv')], axis=0, ignore_index=True, join="inner")
print(df_inner_join)