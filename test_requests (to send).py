import requests
from pprint import pprint

# Задача 1 "Кто самый умный супергерой?"
def smartest_hero(hero_list = ['Hulk', 'Captain America', 'Thanos']):    
    all_json = 'https://akabab.github.io/superhero-api/api/all.json'
    respjson = requests.get(all_json)
    js = respjson.json()

    most_intelligent = {'name_mast_hero': None, 'intel': 0}
  
    for name_hero in hero_list:
        for hero in js:
            for values_all_json in hero.values():
                if values_all_json == name_hero:                             
                    if most_intelligent['intel'] < hero['powerstats']['intelligence']:
                        most_intelligent['intel'] = (hero['powerstats']['intelligence'])
                        most_intelligent['name_mast_hero'] = name_hero
                        
    print(f"Самый умный герой {most_intelligent['name_mast_hero']}. Показатель интелекта составляет {most_intelligent['intel']}") 
      
    
if __name__ == '__main__':
    smartest_hero()

if __name__ == '__main__':
    smartest_hero(['Lady Deathstrike', 'Legion', 'Iron Man'])
    


# Задача 2 "пишем программу для сохранения файла на Яндекс диске с таким же именем"

TOKEN = 'ХХХ'

class YandexDisk:
    
    def __init__ (self, token: str):
        self.token = token
        
    def yd_get_headers(self): #задаем заголовки (используемые в нескольких функциях)
        return {
            'Content-Type': 'application/json', # данные заголовки обязателны для яндекс диска
            'Authorization': 'OAuth {}'.format(self.token)
        }
        
        
    def get_upload (self, disk_file_path: str, file_name: str): # обязательные параметры функции это путь где будет лежать файл на яндеас диске и его название
        up_file_path = 'https://cloud-api.yandex.net/v1/disk/resources/upload' # получаем ссылку для загрузки файла от яндекс API
        headers = self.yd_get_headers() # используем заданные заголовки запросов
        params = { # обязательные требуемые параметры
            'path': disk_file_path,  # путь где будет лежать файл на яндес диске
            'overwrite': 'true' # признак, т.е. если такой файл уже есть что с ним делать (если "true" значит перезаписать)
        }
        response = requests.get(up_file_path, params=params, headers=headers) # выполняем запрос по адресу с обязательными параметрами и заголовками
        response_link = response.json() # получаем данные с ссылкой для загрузки файла в нежном для нас формате (которая фактически храниться в словаре под ключем "href")
        href = response_link['href'] # берм из словаря только ссылку где будет лежать файл
        file_upload = requests.put(href, data=open(file_name, 'rb')) # по полученному адресу и нужный файл (указан в параметрах функции) загружаем на яндекс диск
        return f'Загрузка файла {file_name} завершена.'
        
        
        
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files' # получаем список файлов на яндес диске упорядоченный по имени от яндекс API
        headers = self.yd_get_headers() # используем заданные заголовки запросов
        response = requests.get(files_url, headers=headers) # выполняем запрос по адресу с обязательными заголовками
        return response.json() # полученный ответ преобразуем в .json для удобной обработки
        

if __name__ == '__main__': # при запуске создаем экземпляр класса YandexDisk. Применям функцию get_files_list и получаем списко файлов на яндекс диске 
    yd = YandexDisk(token=TOKEN)
    pprint(yd.get_files_list())
    
    
    
    
if __name__ == '__main__':   # при запуске создаем экземпляр класса YandexDisk. Применяем функцию get_upload и загружаем нужный файл на яндекс диск
    yd_upload = YandexDisk(token=TOKEN)
    path_to_file = yd_upload.get_upload('Task-2/file_zadacha_2.txt', 'file_zadacha_2.txt')
    pprint(path_to_file)



