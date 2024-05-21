#!/usr/bin/python3
"""repellendus veritatis molestias dicta incidunt"""
import csv
import requests
import sys
import json

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
            EMPLOYEE_NAME = key["username"]

    value = []
    dict_row = {par: []}
    anoda_dict = {}
    dict_row[par].append(anoda_dict)

    for key in response_purl:
        value = key['completed']
        anoda_value = key['title']
        dict_row[par].append(anoda_dict)
        anoda_dict['task'] = value
        anoda_dict['completed'] = anoda_value
        anoda_dict['username'] = EMPLOYEE_NAME
        with open("2.json", 'w') as path:
            json.dump(dict_row, path)
