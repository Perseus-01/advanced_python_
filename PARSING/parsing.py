from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

host = 'https://spb.hh.ru'
main = f'{host}/search/vacancy?text=python&area=1&area=2'
keywords = ['django', 'flask']
headers = Headers(browser='firefox', os='win').generate()
main_page = requests.get(main, headers=headers).text
bs = BeautifulSoup(main_page, features='lxml') 
vacancy_links = []
salary = []
city = []
company = []
final_list = []


vacancies_list = bs.find_all('a', class_='serp-item__title')

#geting vacancies links
def get_link():
    for vacancy in vacancies_list:
        link = vacancy['href']    
        descr = (BeautifulSoup(requests.get(link, headers=headers).text, features='lxml')).find('div', {'data-qa': 'vacancy-description'}).text  #зачем здесь фигурные скобки (в html их нет)???
        for word in keywords:
            if word in descr.lower():
                vacancy_links.append(link)

#getting salaries
def get_salary():
    for item in vacancy_links:
        result = (BeautifulSoup(requests.get(item, headers=headers).text, features='lxml')).find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text
        salary.append(result)

#getting cities
def get_city():
    for item in vacancy_links:
        result = (BeautifulSoup(requests.get(item, headers=headers).text, features='lxml')).find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
        city.append(result)

#getting companies
def get_company():
    for item in vacancy_links:
        result = (BeautifulSoup(requests.get(item, headers=headers).text, features='lxml')).find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text
        company.append(result)

#combining all data
def get_data(vacancy_links, salary, city, company):
    all_data = zip(vacancy_links, salary, city, company)
    for link, salary, city, company in all_data:
        dictionary = {'link': link,
                     'salary': salary,
                     'city': city,
                     'company': company}
        final_list.append(dictionary)

#почему в словаре на первом месте city, а не link? Как сделать желаемый порядок?    

#functions call
get_link()
get_salary()
get_city()
get_company()
get_data(vacancy_links, salary, city, company)

# #saving the dictionary to json:
with open('data_saved_to_json.json', 'w') as file:
    json.dump(final_list, file, indent=4, ensure_ascii=False)

