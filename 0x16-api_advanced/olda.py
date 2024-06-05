#!/usr/bin/python3
""""""

import requests

def number_of_subscribers(subreddit):
    CLIENT = "aGP54m8QlFSrk19tAc-DGg"
    SECRET_KEY = "3sGfheOiH8titWro2HzxKiGzgOhQ6A"
    auth = requests.auth.HTTPBasicAuth(CLIENT, SECRET_KEY)

    with open("pw.text", "r") as text:
        pw = text.read()

    data = {
            "grant_type": "password",
            "username": "Itohan_Momo",
            "password": pw
    }
    headers = {"User-Agent": "myApp/0.0.1"}
    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    return(res.json())
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'
    response = requests.get("https://www.reddit.com/api/v1/me", headers=headers)
    """headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}"""
    """url = "https://www.reddit.com/r/python/about.json
    url = "https://oauth.reddit.com/python/mine/subscriber/after"
    r = requests.get(url, headers=headers, allow_redirects=False)
    print(r.json)
    if r.status_code == 200:
        data = r.json()
        subscribers = data["data"]["subscribers"]"""
