#!/usr/bin/python3
"""repellendus veritatis molestias dicta incidunt"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    purl = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    response_purl = requests.get(purl)
    response_purl = response_purl.json()
    response = requests.get(url)
    response = response.json()

    anoda_todos = []
    title_list = []
    for key in response_purl:
        if key['completed'] is True:
            anoda_todos.append(key)
    length_purl = len(anoda_todos)
    length_response = len(response_purl)

    for key in response:
        if key['id'] == 2:
            value = key['name']
            print(f'Employee {value}', end='')
    print(f' is done with tasks({length_purl}/{length_response}):')
    for key in response_purl:
        if key['completed'] is True:
            value = key['title']
            print(f'\t {value}')
