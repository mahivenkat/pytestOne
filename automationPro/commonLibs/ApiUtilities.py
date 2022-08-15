import requests

x = requests.get('https://w3schools.com')
print(x.status_code)


url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

y = requests.post(url, myobj)

print(y.text)