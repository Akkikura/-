import requests
from pprint import pprint
import json
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return{
            'Content-Type': 'application/json', 
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def get_upload_link(self, path_to_file):
        main_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(main_url, headers = headers, params = params)
        return(response.json())

    def upload(self, path_to_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(href, data = open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            pprint('Success')



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ' '
    token = ' '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)