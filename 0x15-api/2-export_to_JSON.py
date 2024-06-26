#!/usr/bin/python3
"""repellendus veritatis molestias dicta incidunt"""
import json
import requests
import sys

if __name__ == '__main__':
    par = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{par}'
    purl = f'https://jsonplaceholder.typicode.com/users/{par}/todos'
    response_purl = requests.get(purl)
    response_purl = response_purl.json()
    response = requests.get(url)
    response = response.json()

    dict_row = {}
    var_list = []

    for key in response_purl:
        anoda_dict = {}
        anoda_dict['task'] = key['title']
        anoda_dict['completed'] = key['completed']
        anoda_dict['username'] = response["username"]
        var_list.append(anoda_dict)
    dict_row[par] = var_list

    file_name = f'{par}.json'
    with open(file_name, 'w') as path:
        json.dump(dict_row, path)
