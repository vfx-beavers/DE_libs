import requests
import urllib3
from lxml import html

#login
payload = {'username': 'login','password': 'pass'}
netGearSiteLogin = requests.post("https://cgpeers.to/login.php",data=payload,allow_redirects=True)
with requests.Session() as session: post = session.post("https://cgpeers.to/login.php", data=payload)
r = session.get("https://cgpeers.to/rules.php")
print(r.data)   
print(r.status_code) 
print(r.text)
