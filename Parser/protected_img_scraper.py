import requests
import os
from bs4 import BeautifulSoup

os.chdir('G:/downloads/Scrap/images')

url="https://superzoom.onlinesuperimage.com/fsicache/server?type=image&source=/onlinekat/onlinekat_mm/prod-backend/wfr/wfr-104927/en_GB/000{}.jpg&left=0&right=1&top=0&bottom=1&height=1500&quality=80"

for page in range(866921,868444):
    print(url.format(page))
    response = requests.get(url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')

    with open(f"tillage_{page}.jpg",'wb') as file:
     file.write(response.content)