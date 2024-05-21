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

    for key in response:
        if key['id'] == int(par):
            EMPLOYEE_NAME = key['username']

    for key in response_purl:
        value = key['completed']
        anoda_value = key['title']
        print(f'"{par}"', end='')
        print(f',"{EMPLOYEE_NAME}",', end='')
        print(f'"{value}",', end='')
        print(f'"{anoda_value}"')
