#!/usr/bin/python3
"""repellendus veritatis molestias dicta incidunt"""
import requests
import sys
import csv


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

    csv_row = []

    for key in response_purl:
        value = key['completed']
        anoda_value = key['title']
        csv_row.append(f'"{par}"')
        csv_row.append(f',"{EMPLOYEE_NAME}"')
        csv_row.append(f',"{value}"')
        csv_row.append(f',"{anoda_value}"')
        csv_row.append("\n")
    with open('2.csv', 'w') as output_file:
        for cs in csv_row:
            output_file.write(str(cs))
