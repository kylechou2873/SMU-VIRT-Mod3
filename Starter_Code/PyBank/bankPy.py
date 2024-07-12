import os
import csv

#file path
pathFile = os.path.join("Resources","budget_data.csv")
#data in file
dateD = [] #raw row[0] data
proLosD = [] #raw row[1] data as int
#store previous month profit/losses
preNum = 0
netList = [] #calculated base on previous month
#store greatest increase and decrease in profit
dateInc = [] #store data from row[0]
proInc = 0 #stonre data from row[1] as int
dateDec = [] #store data from row[0]
proDec = 0 #store data from row[1] as int
#read in
with open(pathFile) as csvFile:
    readFile = csv.reader(csvFile, delimiter = ",")
    fileHead = next(readFile) #skip header row
    for row in readFile:
        dateD.append(row[0])
        proLosD.append(int(row[1]))
        absP = abs(preNum - int(row[1]))#take the absolute value btw previous month and this month
        if int(row[1]) < preNum: #if this month is a loss
            netList.append(absP * -1) #input as the negative absolute value
            if absP * -1 < proDec:
                dateDec = row[0]
                proDec = absP * -1
        elif int(row[1]) > preNum: #if this month is profitable
            netList.append(absP)
            if absP > proInc:
                dateInc = row[0]
                proInc = absP
        preNum = int(row[1]) #update this month to previous month        
    print(f"Total Months: {len(dateD)}")
    print(f"Total: ${sum(proLosD)}")
    print(f"Average Change: ${round(sum(proLosD)/len(dateD),2)}")
    print(f"Greatest Increase in Profit: {dateInc} (${proInc})")
    print(f"Greatest Decrease in Profit: {dateDec} (${proDec})")
