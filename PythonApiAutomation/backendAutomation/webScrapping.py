import requests
from bs4 import BeautifulSoup

data = requests.get("https://courses.rahulshettyacademy.com/courses")
soap = BeautifulSoup(data.content, 'html.parser')
# print(soap.prettify())

courseBar = soap.find('div',{'class':'row course-list list'})

# print(courseBar.prettify())

coursesList = courseBar.find_all('div',{'class':'course-listing-title'})

for links in coursesList:
    print(type(links.text))
    print(links.text)


