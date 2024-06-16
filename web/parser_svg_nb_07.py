import pandas as pd
import json
import requests
import lxml.html
import os
from lxml import html
from lxml import etree
from pandas import json_normalize

html = requests.get('http://localhost:8000/spuffed_page.html')
tree = lxml.html.fromstring(html.content)
rvs_13_temp = tree.xpath('.//g[@id="shape3748-255"]//text')[0]
rvs_13_level = tree.xpath('.//g[@id="shape3745-261"]//text')[0]
rvs_13_volume = tree.xpath('.//g[@id="shape3742-267"]//text')[0]
rvs_13_pressure = tree.xpath('.//g[@id="shape3739-273"]//text')[0]
rvs_13_mass = tree.xpath('.//g[@id="shape2851-279"]//text')[0]
    
rvs_22_temp = tree.xpath('.//g[@id="shape3835-524"]//text')[0]
rvs_22_level = tree.xpath('.//g[@id="shape3838-530"]//text')[0]
rvs_22_volume = tree.xpath('.//g[@id="shape3841-536"]//text')[0]
rvs_22_pressure = tree.xpath('.//g[@id="shape3844-542"]//text')[0]
rvs_22_mass = tree.xpath('.//g[@id="shape3847-548"]//text')[0]

rvs_82_temp = tree.xpath('.//g[@id="shape3932-793"]//text')[0]
rvs_82_level = tree.xpath('.//g[@id="shape3935-799"]//text')[0]
rvs_82_volume = tree.xpath('.//g[@id="shape3938-805"]//text')[0]
rvs_82_pressure = tree.xpath('.//g[@id="shape3941-811"]//text')[0]
rvs_82_mass = tree.xpath('.//g[@id="shape3944-817"]//text')[0]
result = """[
            {{
	  	"Name": "13",
		"Temp": "{}",
		"Level": "{}",
		"Volume": "{}",
		"Pressure": "{}",
		"Mass": "{}",
		"Availability": "-"
            }},
            {{
	  	"Name": "22",
		"Temp": "{}",
		"Level": "{}",
		"Volume": "{}",
		"Pressure": "{}",
		"Mass": "{}",
		"Availability": "-"
            }},
            {{
	  	"Name": "82",
		"Temp": "{}",
		"Level": "{}",
		"Volume": "{}",
		"Pressure": "{}",
		"Mass": "{}",
		"Availability": "-"
            }}
]
"""
result_string = result.format(rvs_13_temp.text, rvs_13_level.text, rvs_13_volume.text, rvs_13_pressure.text, rvs_13_mass.text,
rvs_22_temp.text, rvs_22_level.text, rvs_22_volume.text, rvs_22_pressure.text, rvs_22_mass.text, rvs_82_temp.text, rvs_82_level.text, rvs_82_volume.text, rvs_82_pressure.text, rvs_82_mass.text)
print(result_string)
df = pd.read_json(result_string, orient ='name')
df['Temp'] = df['Temp'].str.replace(' ', '')
df['Temp'] = df['Temp'].str.replace('°C', '')
df['Level'] = df['Level'].str.replace(' ', '')
df['Level'] = df['Level'].str.replace('м', '')
df['Volume'] = df['Volume'].str.replace(' ', '')
df['Volume'] = df['Volume'].str.replace('м³', '')
df['Pressure'] = df['Pressure'].str.replace(' ', '')
df['Pressure'] = df['Pressure'].str.replace('кг/м³', '')
df['Mass'] = df['Mass'].str.replace(' ', '')
df['Mass'] = df['Mass'].str.replace('кг', '')
df ['Temp'] = pd.to_numeric(df['Temp'], errors='ignore')
df ['Level'] = pd.to_numeric(df['Level'], errors='ignore')
df ['Volume'] = pd.to_numeric(df['Volume'], errors='ignore')
df ['Pressure'] = pd.to_numeric(df['Pressure'], errors='ignore')
df ['Mass'] = pd.to_numeric(df['Mass'], errors='ignore')
pd.options.display.float_format = "{:,.2f}".format
print(df)
print(df.dtypes)
df.to_csv('./NBV_out.csv', encoding='utf-8', quotechar='"', quoting=1, index_label=None, index=False, na_rep='0', float_format='%.2f')
df.to_json('./NBV_out_json.json', orient='records', indent=2)
