#import the necessary modules
import os
import csv

#create a file path for the budget data
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#create variables to hold the data from the csv file, and variables to hold the final analyses of the data
monthly_change = []
dates = [] 
month = 0
net_total = 0
initial = 0

#open the csv file, save the header, and loop through the table
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)

    for row in csvreader:    
        #increase the count of the months for every row in the csv table
        month += 1
        #add the dates from the csv table into the dates list
        dates.append(row[0])
        
        #read the amount of money in each row, and add it all together into the net_total variable
        net_total += int(row[1])
        #the final variable will at first be the first row
        final = int(row[1])
        
        #determining the monthly financial change is as simple as subtracting the initial amount from the final amount
        #and then adding each given result into the monthly_change list
        monthly_change.append((final-initial))
        
        #reset the intial variable to the final variable (iterating it so it keeps up with the list iterating through the csv table)
        initial = final
        
        #create a for loop to go through the monthly change list, first create a count variable
        count = 0
        for i in range(len(monthly_change)):
            #for each item in the monthly change list, it is added to the count variable
            count += monthly_change[i]
        
        #the average change per month is simply dividing the totality of changes by the number of months
        #rounding to imitate dollar and cents amounts
        average_change = round((count/month), 2)
        
        #use the max and min methods to search through the monthly change lists and find the single 
        #greatest increase and decrease in the list
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
        
        #create a variable to store the date that corresponds to the greatest increase/decrease
        #each will look through the dates list and find the index of the date that matches the greatest increase/decrease
        date_increase = dates[monthly_change.index(greatest_increase)]
        date_decrease = dates[monthly_change.index(greatest_decrease)]

#print out a summary financial analysis table 
print(f"Financial Analysis")
print(f"-"*28)
print(f"Total Months: {month}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase In Profits: {date_increase} (${greatest_increase})")
print(f"Greatest Decrease In Profits: {date_decrease} (${greatest_decrease})")

#write (in an almost identical fashion to the printed out summary) the result to a text file
with open("financial_analysis.txt", "w") as text:
    text.write("Financial Analysis \n")
    text.write("-"*28)
    text.write("\n")
    text.write(f"Total Months: {month} \n")
    text.write(f"Total: ${net_total} \n")
    text.write(f"Average Change: ${average_change} \n")
    text.write(f"Greatest Increase In Profits: {date_increase} (${greatest_increase} \n")
    text.write(f"Greatest Decrease In Profits: {date_decrease} (${greatest_decrease} \n")