import os
import csv

file_path = os.path.join("./Resources", "budget_data.csv")

total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

csv_file = "financial_data.csv"

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)


    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        total_months += 1
        net_total += profit_loss

        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

       
        previous_profit_loss = profit_loss

average_change = sum(profit_loss_changes) / (total_months - 1)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")