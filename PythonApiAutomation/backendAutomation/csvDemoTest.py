import csv

with open('utilities/Book.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    Status = []
    for row in csvReader:
        names.append(row[0])
        Status.append(row[1])

print(names)
print(Status)
Index = names.index('Pruthvi')
loanStatus = Status[Index]
print(' loan status is '+loanStatus)

with open('utilities/Book.csv','a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Ram","rejected and denied"])