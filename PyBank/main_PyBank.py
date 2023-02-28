import os
import csv 
import statistics

#set path for file
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, "Resources/budget_data.csv")

#define variables
total_months = 0 
months_list = []
profit_losses = []
profit_losses_change_list = []


#open and read CSV
with open(filepath) as budget_data_file:
    csv_reader = csv.reader(budget_data_file, delimiter=',')

    #read the header row 
    csv_header = next(budget_data_file)

    #read through each row of data and count total months
    for row in csv_reader:
        total_months = total_months + 1

        #create list of months column
        months_list.append(str(row[0]))

        #calculate net total amount of Profit/Losses using list 
        profit_losses.append(int(row[1]))
        net_total = sum(profit_losses)

    #calculate changes of Profit/Losses over entire period and its average
    for i in range (len(profit_losses)-1):
        profit_losses_change = (profit_losses[i+1] - profit_losses[i])
        profit_losses_change_list.append(profit_losses_change)
        mean_change = statistics.mean(profit_losses_change_list)
    
    #calculate greatest increase and decrease of changes of Profit/Losses and find the corresponding months
    greatest_increase = max(profit_losses_change_list)
    greatest_decrease = min(profit_losses_change_list)
    greatest_increase_index = profit_losses_change_list.index(greatest_increase)+1
    greatest_decrease_index = profit_losses_change_list.index(greatest_decrease)+1
    greatest_increase_month = months_list[greatest_increase_index]
    greatest_decrease_month = months_list[greatest_decrease_index]
     
#print final values
print("Financial Analysis:")
print("---------------------------")
print(f"Header: {csv_header}")
print(f"Total months: {total_months}")
print(f"Total net amount: ${net_total}")
print(f"Average change: ${mean_change}") 
print(f"Greatest increase in proftis: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest decrease in proftis: {greatest_decrease_month} (${greatest_decrease})")

#create path for output file
dirname = os.path.dirname(__file__)
output_file = os.path.join(dirname, "Analysis/budget_data.txt")

#open output file and fill it with information
with open(output_file, "w") as outfile:

    outfile.write("Financial Analysis:\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Header: {csv_header}\n")
    outfile.write(f"Total months: {total_months}\n")
    outfile.write(f"Total net amount: ${net_total}\n")
    outfile.write(f"Average change: ${mean_change}\n")
    outfile.write(f"Greatest increase in profits: {greatest_increase_month} (${greatest_increase})\n")
    outfile.write(f"Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})")


