import requests

body = {
    "name": 'jack',
    'age': 21
}

form_data_response = requests.post('https://postman-echo.com/post', data=body)
print('form_data_response.text'.center(40, '='))
print(form_data_response.text, end='\n\n')

json_data_response = requests.post('https://postman-echo.com/post', json=body)
print('json_data_response.text'.center(40, '='))
print(json_data_response.text)
