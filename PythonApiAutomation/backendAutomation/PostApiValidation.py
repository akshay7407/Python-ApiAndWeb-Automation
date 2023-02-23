import requests
from payload import addBookPayload
from utilities.configuaration import *
from utilities.resources import *
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# AddBookUrl

addBookUrl = getConfig()['API']['endpoint'] + ApiResources.addBook
deleteBookUrl = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers= {"Content-Type": "application/json"}
addBook_response = requests.post(addBookUrl, json=addBookPayload('Akkii'),
                                 headers=headers)

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)

# DeleteBook
deleteBook_response = requests.post(deleteBookUrl,
                                    json={"ID": bookId}, headers= headers)

print(deleteBook_response.text)
del_res = deleteBook_response.json()
msg = del_res['msg']
assert msg == "book is successfully deleted"
assert deleteBook_response.status_code == 200

#Authentication
url = "https://api.github.com/user"
url2 = "https://api.github.com/user/repos"
se = requests.session()
se.auth = auth=('ibmentor',getPass())
github_response = requests.get(url,verify=False,auth=('ibmentor',getPass()))
print(github_response.status_code)

#Authentication2
resp = se.get(url2)
print(resp.status_code)