import os
import csv

# Define Variables
month_count = 0 # To keep track of month in the file
total_profit_loss = 0 # Total of all profits/losses in file
initial_profit_loss = 0 #Assign the first value in profit/loss
monthly_profit_loss_change = [] # list to add each monthly change profit/loss value
monthly_change_months = [] # list to add each month for the monthly change profit/loss value
previous_monthly_profit_loss = 0
profit_loss_change = 0
total_profit_loss_change = 0
average_profit_loss_change = 0
date = []


# Path of file to read data
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the csv file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Loop through each row 
    for row in csvreader:

        #Count the total number of months
        month_count += 1

        #Add all the rows for profit/losses
        initial_profit_loss = int(row[1])
        total_profit_loss = total_profit_loss + initial_profit_loss
        
        #Calculate the profit/loss for month to month(row to row)
        #For the first month, previous month needs to be set to initial month
        if(month_count == 1):
             previous_monthly_profit_loss = initial_profit_loss

        else:
            #Calculate the change in profit loss 
            profit_loss_change = initial_profit_loss - previous_monthly_profit_loss

            #add it to the list
            monthly_profit_loss_change.append(profit_loss_change)

            # add month to the list
            monthly_change_months.append(row[0])

            #set previous to intial
            previous_monthly_profit_loss = initial_profit_loss

            # Find the greatest increase in change
            greatest_increase = max(monthly_profit_loss_change)

            # Find the greatest decrease in change
            greatest_decrease = min(monthly_profit_loss_change)

            # Find the gratest increase month
            increase_month = monthly_change_months[monthly_profit_loss_change.index(greatest_increase)]
            # Find the greatest decrease month
            decrease_month = monthly_change_months[monthly_profit_loss_change.index(greatest_decrease)]



#Add up all the values in the list to find sum of profit/loss changes
total_profit_loss_change = sum(monthly_profit_loss_change)

#Average of Profit/Loss changes
average_profit_loss_change = total_profit_loss_change / (month_count - 1)

print("Financial Analysis")
print("---------------------------------------")       
print("Total Months : " + str(month_count))
print("Total : " + "$" + str(total_profit_loss))
print("Average Change : " + "$" + str(round(average_profit_loss_change, 2)))
print("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatest_decrease) + ")")

#Export to a text file
# Specify the file to write to
output_path = os.path.join("analysis","output_text.txt")

with open(output_path, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------------------\n")       
    textfile.write("Total Months : " + str(month_count) + "\n")
    textfile.write("Total : " + "$" + str(total_profit_loss) + "\n")
    textfile.write("Average Change : " + "$" + str(round(average_profit_loss_change, 2))+ "\n")
    textfile.write("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(greatest_increase) + ")\n")
    textfile.write("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(greatest_decrease) + ")\n")
