import requests 
import configparser
#TASK_1
# Дан список с визитами по городам и странам. Напишите код, 
# который возвращает отфильтрованный список geo_logs, 
# содержащий только визиты из России."

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def show_russia_visits(dict):
    filtered_list = []
    for visit in geo_logs:
        if 'Россия' in list(visit.values())[0]:
            filtered_list.append(visit)
    print(filtered_list, '\n')

russia = show_russia_visits(geo_logs)


#TASK_2
# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_ids(dict):
    result = set()
    for i in ids.values():
        result.update(i)
    print(result)

unique_ids_list = unique_ids(ids)

#TASK_4
# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.

def max_sales(dict):
    result = {max(stats, key=stats.get)}
    return result

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

expected_stats = max_sales(stats)



# YANDEX API


token = 'y0_AgAAAAAUtDPCAAnOawAAAADhsgic_9NNnUavRCmHKEepidKuaexZnpg'


class Yandex:
    def __init__(self, token, url='https://cloud-api.yandex.net/v1/disk/resources'):
        self.token = token
        self.url = url

    def _get_headers(self):
        return {'Content_Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_folder(self, folder_path):
        headers = self._get_headers()
        params = {'path': folder_path}
        response = requests.put(self.url, headers=headers, params=params)
        return response.status_code
    
    def delete_folder(self, folder_path):
        headers = self._get_headers()
        params = {
            'path': folder_path,
            'permanently': 'true',
            'force_async': 'true'}
        response = requests.delete(self.url, headers=headers, params=params)
        return response.status_code


yandex_user = Yandex(token=token)
yandex_user.create_folder('%2Ftest_folder')




