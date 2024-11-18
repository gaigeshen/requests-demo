import requests
from tqdm import tqdm

downlaod_file_response = requests.get('https://download.bell-sw.com/java/21.0.4+9/bellsoft-jdk21.0.4+9-windows-amd64-full.zip', stream=True)
if downlaod_file_response.status_code == 200:
    total = int(downlaod_file_response.headers.get('Content-Length', 0))
    with open('jdk21.zip', 'wb') as f, tqdm(total=total, unit='B', unit_scale=True) as pbar:
        for chunk in downlaod_file_response.iter_content(chunk_size=1024):
            f.write(chunk)
            pbar.update(len(chunk))
    print('file download done')
else:
    print(f'file download error: {downlaod_file_response.status_code}')
