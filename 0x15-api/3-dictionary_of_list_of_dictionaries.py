#!/usr/bin/python3
"""repellendus veritatis molestias dicta incidunt"""
import json
import requests

if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    response = response.json()

    dict_row = {}

    for key in response:
        var_list = []
        id = key["id"]
        purl = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
        response_purl = requests.get(purl)
        response_purl = response_purl.json()
        for j in response_purl:
            each_user = {}
            each_user["username"] = key["username"]
            each_user['task'] = j['title']
            each_user['completed'] = j['completed']
            var_list.append(each_user)
        dict_row[id] = var_list

    with open("todo_all_employees.json", 'w') as path:
        json.dump(dict_row, path)
