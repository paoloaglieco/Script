import requests

url = 'https://assets.tryhackme.com/img/THMLogo.png'
r = requests.get(url, allow_redirects=True)
open('THMLogo.png', 'wb').write(r.content)
