import json

courses = '{"name": "Akshay Gaikwad","languages": [ "Java", "Python", "javascript"]}'

#Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
#get me the first language taught by trainer
# list_language = dict_courses['languages']
# print(type(list_language))
# print(list_language[0])
print(dict_courses['languages'][0])

#****** Parse content present in Json file
with open('D:\PythonTutorial\PythonApiAutomation\course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][2])


for course in data['courses']:
        #print(course)
        if course['title'] == "Selenium Python":
            print(course['price'])
            assert course['price'] == 50











