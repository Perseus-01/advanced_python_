import requests
import pprint

# def hello_world():
#     while True:
#         yield 'Hello World!'

# hello_world_generator = hello_world()
# for item in hello_world_generator:
#     print(item)

# range(1, 2)

# def my_range(start, end):  
#     cursor = start
#     while cursor < end:
#         yield cursor
#         cursor += 1

# for item in my_range(1, 4):
#     print(item)

def swapi_people():
    next_page = 'https://swapi.dev/api/people'
    while next_page:
        response = requests.get(next_page).json()
        next_page = response['next']
        results = response['results']
        for item in results:
            yield item

# for item in swapi_people():
#     print(item)

high_people = (
    item for item in swapi_people() 
    if item.get('height') != 'unknown' and int(item.get('height', 0))> 190
) 

for item in high_people:
    print(item)



