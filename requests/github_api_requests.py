import requests

# pass
#from getpass import getpass # Импортируем метод getpass из одноимённой библиотеки для ввода пароля доступа.
#requests.get('https://api.github.com/user', auth=('username', getpass())
             
# ref
#r = requests.get('https://api.github.com', auth=('user', 'pass'))
#print (r.status_code, r.headers['content-type'])

# wo ssl
# requests.get('https://api.github.com', verify=False)


# session w saved params
# with requests.Session() as session:
#    session.auth = ('login', getpass())
#    response = session.get('https://api.github.com/user')
# # Выведем ответ на экран.
# print(response.headers)
# print(response.json())

# типы запросов 
# r = requests.post('https://httpbin.org/post', data = {'key':'value'})  
# r = requests.put('https://httpbin.org/put', data = {'key':'value'})  
# r = requests.delete('https://httpbin.org/delete')  
# r = requests.head('https://httpbin.org/get')  
# r = requests.options('https://httpbin.org/get')  

# Передача параметров в URL
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']} 
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url) 

# проверка состояния ответа
# r = requests.get('https://httpbin.org/get')
# r.status_code
# 200

# r.status_code == requests.codes.ok
# True

# bad_r = requests.get('https://httpbin.org/status/404')
# bad_r.status_code
# 404
# bad_r.raise_for_status()


# Заголовки ответов
# r.raise_for_status()



response = requests.get('https://api.github.com/events')
print (response.text)
