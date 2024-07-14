import os
import csv

# Get current work directory
cwd = os.getcwd()

budget_csv = os.path.join(cwd, 'Resources', 'budget_data.csv')

# Lists to store data
budget_date = []
#profit_losses = []
monthly_delta = []

# Intialize variables
rec_count = 0
total_profit_losses_amt = 0
prev_profit_losses_amt = 0
cur_profit_losses_amt = 0
monthly_delta_amt = 0
avg_profit_losses_amt = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read header
    csv_header = next(csvreader)
    
    
    # Store csv file columns into 2 lists
    for row in csvreader:
        
        rec_count += 1
        
        budget_date.append(row[0])
        #profit_losses.append(float(row[1]))
        
        cur_profit_losses_amt = float(row[1])
        
        # On first record set previous profit/losses to current profit/losses amount
        if (rec_count == 1):
            prev_profit_losses_amt = float(cur_profit_losses_amt)
            
            
        # Calculate average change in profits/losses
        total_profit_losses_amt += cur_profit_losses_amt
        
        monthly_delta_amt = cur_profit_losses_amt - prev_profit_losses_amt
        
        # Stored monthly delta amount in list
        monthly_delta.append(monthly_delta_amt)
        
        prev_profit_losses_amt = cur_profit_losses_amt
    
    total_deltas = sum(monthly_delta)
    avg_profit_losses_amt = round(total_deltas / (rec_count - 1), 2)
    
    # Return min/max profit losses delta
    max_delta = max(monthly_delta)
    min_delta = min(monthly_delta)
    
    # Search lists monthly_delta and budget_date to find record with
    # greatest profit increase/decrease 
    max_month_index = monthly_delta.index(max_delta)
    min_month_index = monthly_delta.index(min_delta)
    
    # Return budget date of greatest increae/decrease
    greatest_incr_mon = budget_date[max_month_index]
    greatest_decr_mon = budget_date[min_month_index]

# Save analysis results to variable
report = f"""
Financial Analysis:
---------------------------
Total Months: {rec_count}
Total: {'${:,.2f}'.format(total_profit_losses_amt)}
Average Change: {'${:,.2f}'.format(avg_profit_losses_amt)}
Greatest Increase in Profits: {greatest_incr_mon} ({'${:,.2f}'.format(max_delta)})
Greatest Decrease in Profits: {greatest_decr_mon} ({'${:,.2f}'.format(min_delta)})
"""
# Display analysis report to terminal
print(report)

# Save analysis report to text file
analysis_file = os.path.join(cwd, "analysis", "budget_data_analysis.txt")
with open(analysis_file, "w") as outfile:
    outfile.write(report)
