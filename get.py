import requests

queries = {
    'name': 'jack',
    'age': 21
}

response = requests.get('https://postman-echo.com/get', params=queries)
print('response.text'.center(40, '='))
print(response.text)
