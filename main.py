#Define modules to open csv files
#convert operating system
import os
#open a csv file
import csv


#create csv file path 
budgetDataPath = os.path.join('..','PyBank','budget_data.csv')


#Open the CSV file and save into variable called csvfile
with open(budgetDataPath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #csv_row_list = list(csvreader)
    next(csvreader)
   
    profit_loss = []     
    date = []
    rev_change = []

#append lists
    for row in csvreader:
        profit_loss.append(float(row[1]))
        date.append(row[0])

    Total_months = len(date)
    Total_budget = sum(profit_loss)

#create a loop to find the differences between all rows in "Revenue list"
    for i in range(1,len(profit_loss)):
        rev_change.append(profit_loss[i] - profit_loss[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])

      

    
print("Financial Analysis")  
print("---------------------------------------")

print(f"Total Months: {Total_months}") 
print(f"Total budget: {Total_budget}")
print(f"Average change $: {avg_rev_change}")
print(f" Greatest increase in revenue: {max_rev_change_date}, $ {max_rev_change}")
print(f" Greatest decrease in revenue: {min_rev_change_date}, $ {min_rev_change}")

        






