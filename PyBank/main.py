#Importiing relevant packages
import os
import csv

#Establishing path to the data
csvpath = os.path.join(".","Resources","budget_data.csv")

#number of months tracker
n = 0

#cumulative profit/loss tracker
total = 0

#The difference between the profit/loss from one row and another
change = 0

#cumulative changes in profit/loss tracker
change_total = 0

#Greastest increase in profits
greatest_increase = 0

#Greatest decrease in profits
greatest_decrease = 0

#Greastest increase date in profits
greatest_increase_date = 0

#Greatest decrease date in profits
greatest_decrease_date = 0

#Opening CSV file to read data
with open(csvpath, encoding  = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Skips CSV headers
    header = next(csvreader)

    #Looping row by row in the sheet
    for row in csvreader:
        n += 1
        total += int(row[1])

        #The first row does not have a change; thus must be skipped
        if n != 1:
            change = int(row[1]) - previous_row
            change_total += change
        
        #Checking the greatest increase/decrease
        if change > int(greatest_increase):
            greatest_increase_date = row[0]
            greatest_increase = change

        elif change < int(greatest_decrease):
            greatest_decrease_date = row[0]
            greatest_decrease = change
        
        #Establish "previous" row for next row calculations
        previous_row = int(row[1])
    
    #Calculating desired metrics
    average = round(change_total/(n-1),2)
    change = int(row[1]) - previous_row
    change_total += change

#Printing and Creating textfile
text = open("financial_analysis.txt", "w")
text.write("Financial Analysis\n")
text.write("----------------------------\n")
text.write(f"Total Months: {n}\n")
text.write(f"Total ${total}\n")
text.write(f"Average Change: ${average}\n")
text.write(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n")
text.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}\n")
text.close()

