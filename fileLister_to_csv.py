import os
import csv

dataSet =[]

fileType = "."+raw_input("what file type are you looking for? (No need to add '.')\n")
csvName = raw_input("what is the output csv file name?\n")+".csv"

for file in os.listdir("./"):
    if file.endswith(fileType):
        print(os.path.join("./", file))
        fileName = file;
        fileNameR = fileName.replace(str(fileType),"")
        dataSet.append(fileNameR)
        
with open(csvName, "wb") as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        for line in dataSet:
            writer.writerow([line])
