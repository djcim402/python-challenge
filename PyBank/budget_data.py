import os
import csv

budget_csv = os.path.join("..","Desktop","budget_data.csv")
    
# Variables
total_months = 0
net_total = 0
previous = 0
change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
changes = []

# Read csv
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip headers
    next(csvreader, None)

    # Loop and collect data
    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        change = int(row[1]) - previous
        previous = int(row[1])

        if (change > greatest_increase[1]):
            greatest_increase[1] = change
            greatest_decrease[0] = row[0]
        
        changes.append(int(row[1]))
    avg = sum(changes) / len(changes)

    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(net_total))
    print("Average Change: " + "$" + str(round(sum(changes) / len(changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
    
# Output txt file
