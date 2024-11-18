import requests

print('upload file'.center(40, '='))

files = {
    'file': open('upload.py', 'rb')
}

upload_file_response = requests.post('https://postman-echo.com/post', files=files)
if upload_file_response.status_code == 200:
    print('file upload done')
    print(upload_file_response.text, end='\n\n')
else:
    print(f'file upload error: {upload_file_response.status_code}', end='\n\n')

print('download file'.center(40, '='))

downlaod_file_response = requests.get('https://postman-echo.com/stream/2048', stream=True)
if downlaod_file_response.status_code == 200:
    with open('download.txt', 'wb') as f:
        for chunk in downlaod_file_response.iter_content(chunk_size=1024):
            f.write(chunk)
    print('file download done')
else:
    print(f'file download error: {downlaod_file_response.status_code}')
