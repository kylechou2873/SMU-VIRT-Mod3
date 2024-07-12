import os
import csv

#file path
pathFile = os.path.join("Resources","election_data.csv")
#store data from csv
idB = []
votDic ={
    "name" : ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"],
    "vote" : [0,0,0]
}
#read in
with open(pathFile) as csvFile:
    readFile = csv.reader(csvFile, delimiter = ",")
    fileHead = next(readFile)#skip header
    for row in readFile:
        idB.append(row[0])
        if row[2] == "Charles Casper Stockham":
            votDic["vote"][0] +=1
        elif row[2] == "Diana DeGette":
            votDic["vote"][1] +=1
        elif row[2] == "Raymon Anthony Doane":
            votDic["vote"][2] +=1


#getting data from dic for print
ccsVote = votDic["vote"][0]
ddgVote = votDic["vote"][1]
radVote = votDic["vote"][2]
winC = max(votDic["vote"])
winIndex = votDic["vote"].index(winC)
winner = votDic["name"][winIndex]

#print to terminal
print(f"Election Results")
print()
print("----------------------------------------")
print()
print(f"Total Votes: {len(idB)}")
print()
print("----------------------------------------")
print()
print(f"Charles Casper Stockham: {round(ccsVote/len(idB)*100,3)}% ({ccsVote})")
print(f"Diana DeGette: {round(ddgVote/len(idB)*100,3)}% ({ddgVote})")
print(f"Raymon Anthony Doane: {round(radVote/len(idB)*100,3)}% ({radVote})")
print()
print("----------------------------------------")
print()
print(f"Winner: {winner}")
print()
print("----------------------------------------")
