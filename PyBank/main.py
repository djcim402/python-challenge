import os
import csv

budget_csv = os.path.join("..","Desktop","budget_data.csv")
    
# Variables
total_months = []
net_total = []
monthly_change = []

# Read csv
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip headers
    next(csvreader, None)

    # Loop and collect data
    for row in csvreader:
        total_months.append(row[0])
        net_total.append(int(row[1]))

    # Monthly change in profit/losses
    for i in range(len(net_total)-1):

        monthly_change.append(net_total[i+1]-net_total[i])

max_increase = max(monthly_change)
max_decrease = min(monthly_change)

# Calculate min and max month to month
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1
        
 # Print statement

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")
    
# Output txt file

output_budget = os.path.join("..","Desktop","budget_data.txt")

with open(output_budget, "w") as txt_file:

    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {len(total_months)}")
    txt_file.write("\n")
    txt_file.write(f"Total: ${sum(net_total)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")
