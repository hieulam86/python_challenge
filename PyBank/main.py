import csv
import os

# Read data from the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

data = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        data.append((date, profit_loss))

# Calculate total number of months
def calculate_total_months(data):
    total_months = len(data)
    return total_months

# Calculate total amount of profit/loss
def calculate_total(data):
    total = sum(profit_loss for _, profit_loss in data)
    return total

# Calculate average change in profit/loss
def calculate_average_change(data):
    total_changes = 0
    for i in range(len(data) - 1):
        next_month_profit_loss = data[i + 1][1]
        current_month_profit_loss = data[i][1]
        change = next_month_profit_loss - current_month_profit_loss
        total_changes += change
    average_change = total_changes / (len(data) - 1)
    return average_change



# Calculate greatest increase in profits
def calculate_greatest_increase(data):
    max_increase = ("", 0)
    for i in range(len(data) - 1):
        next_month_profit_loss = data[i + 1][1]
        current_month_profit_loss = data[i][1]
        change = next_month_profit_loss - current_month_profit_loss
        if change > max_increase[1]:
           max_increase = (data[i + 1][0], change) 
    return max_increase

# Calculate greatest decrease in profits
def calculate_greatest_decrease(data):
    min_decrease = ("", 0)
    for i in range(len(data) - 1):
        next_month_profit_loss = data[i + 1][1]
        current_month_profit_loss = data[i][1]
        change = next_month_profit_loss - current_month_profit_loss
        if change < min_decrease[1] or min_decrease[1] == 0:
            min_decrease = (data[i + 1][0], change) 
    return min_decrease

total_months = calculate_total_months(data)
total_profit_loss = calculate_total(data)
average_change = calculate_average_change(data)
greatest_increase_date, greatest_increase_amount = calculate_greatest_increase(data)
greatest_decrease_date, greatest_decrease_amount = calculate_greatest_decrease(data)

#Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

#Path to the output text file
output_patch = os.path.join('..', 'Analysis', 'PyBank.txt')

#Write results to a text file
with open(output_patch, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")
