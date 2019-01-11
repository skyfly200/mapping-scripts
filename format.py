# -*- coding: cp1252 -*-
import csv

def writeLine(row, line_num):
    line_name = row[12]
    with open('lines/' + str(line_num) + '-' + line_name + '-' + row[3] + '.csv', 'wb') as lineFile:
        writer = csv.writer(lineFile)
        # write header line to csv
        writer.writerow(["type","latitude","longitude","altitude","accuracy","name","color",row[1],line_name,row[3]])
        # break track field into list by semi colon
        points = row[10].split(';')
        color = 'blue'
        # write a line to the file for each point
        for p in points:
            if p:
                writer.writerow(['T'] + p.split() + [line_name, color])

with open('data.csv', 'rb') as inFile:
    reader = csv.reader(inFile)
    with open('points.csv', 'wb') as pointsFile:
        fields = ["uuid","name","notes","latitude","longitude","depth","timestamp"]
        fieldIndexes = [1, 12, 13, 6, 7, 11, 16]
        writerP = csv.writer(pointsFile)
        writerP.writerow(fields) # write header
        lines = 0
        for row in reader:
            if row[2] == 'line': # for lines call write line function to make a new line file
                writeLine(row, lines)
                lines += 1
            elif row[-1] != "KEY": # for a point write to points file
                point = []
                for n in fieldIndexes:
                    point.append(row[n])
                writerP.writerow(point)
