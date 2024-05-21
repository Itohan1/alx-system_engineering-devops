#!/usr/bin/python3
"""repellendus veritatis molestias dicta incidunt"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'

    par = sys.argv[1]
    purl = f'https://jsonplaceholder.typicode.com/users/{par}/todos'
    response_purl = requests.get(purl)
    response_purl = response_purl.json()
    response = requests.get(url)
    response = response.json()

    anoda_todos = []
    title_list = []
    for key in response_purl:
        if key['completed'] is True:
            anoda_todos.append(key)
    NUMBER_OF_DONE_TASKS = len(anoda_todos)
    TOTAL_NUMBER_OF_TASKS = len(response_purl)

    for key in response:
        if key['id'] == int(par):
            EMPLOYEE_NAME = key['name']
            print(f'Employee {EMPLOYEE_NAME} is done with tasks', end='')
    print(f'({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for key in response_purl:
        if key['completed'] is True:
            TASK_TITLE = key['title']
            print(f'\t {TASK_TITLE}')
