import pandas as pd

df = pd.DataFrame({"d": ['2018-03-20T19:48:12.000Z', '2018-07-20T14:33:09.000Z', '2018-07-20T14:33:55.000Z']})
df["d"] = pd.to_datetime(df["d"], format="%Y-%m-%d %H:%M:%S.%f")
print(df)

