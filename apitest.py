import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
myobj = {'somekey': 'somevalue'}
x = requests.post(url ,data= myobj)
print(x.text)
