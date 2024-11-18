import requests

files = {
    'file': open('upload.py', 'rb')
}

upload_file_response = requests.post('https://postman-echo.com/post', files=files)
if upload_file_response.status_code == 200:
    print(upload_file_response.text)
else:
    print(f'file upload error: {upload_file_response.status_code}')
