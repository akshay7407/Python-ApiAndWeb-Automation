

listItem= [2, 0, 88, 99, "akshay"]

#for in loop
for obj in listItem:
    print(obj)

#print 1 to 10 number in loop

for num in range(1, 11):
    print(num)

# sum of First Natural numbers 1+2+3+4+5 = 15
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("*******************************")
for k in range(1, 10, 5):
    print(k)
    print("**************SKIPPING FIRST INDEX*****************")
for m in range(10):
    print(m)
