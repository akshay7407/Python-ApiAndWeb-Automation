import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName':'Akshay Gaikwad'},)
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
for actualBook in dict_response:
    if dict_response[0]['isbn'] == 'vhshj':
        print(actualBook)
        break

expectedBook = {
        "book_name": "rest api automation",
        "isbn": "vhshj",
        "aisle": "64453"
    }

assert actualBook == expectedBook
