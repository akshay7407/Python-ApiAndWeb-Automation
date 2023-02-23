from utilities.configuaration import *

conn = getConnection()

cursor = conn.cursor()

cursor.execute('select * from CustomerInfo ')
#row = cursor.fetchone()
#print(row)
#print(row[3])

#to print all records

rowAll = cursor.fetchall()
print(rowAll)
sum = 0
for table in rowAll:
    print(type(table))
    courseName = table[0]
    location = table[3]
    price = table[2]
    if courseName == 'Jmeter':
     print("Price of jmeter " + str(price))
     print('location of course ' + location)
    sum = table[2] + sum
print(sum)

query ="update CustomerInfo set location = %s where CourseName = %s "
data = ("Mumbai","Appium")
cursor.execute(query,data)
conn.commit()

conn.close()