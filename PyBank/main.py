import csv

# file path
budget_path = "Resources/budget_data_1.csv"
budget_output = "Resources/budget_analysis.txt"

# Trackable Variable
total_months = 0
total_revenue = 0
revenue_change = 0
previous_revenue = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000000000000000000]

revenue_changes = []

# Read csv Files
# The reason why I choose DictReader instead of Reader is because under DictReader, it reads file as a string type.
# Reference: https://stackoverflow.com/questions/13541567/python-csv-reader-vs-csv-dictreader-differences
with open(budget_path) as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Loop through all the rows of data
    for row in csvreader:

        # Calculation of the totals
        total_months += 1
        total_revenue += int(row["Revenue"])

        revenue_change = int(row["Revenue"]) - previous_revenue

        # Reset previous_revenue
        previous_revenue = int(row["Revenue"])

        # The greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        # Add it to the revenue_change
        revenue_changes.append(int(row["Revenue"]))
    # Revenue Average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)

    # Print the answer
    print()
    print()
    print("Financial Analysis")
    print("----------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
    print("Greatest Increase in Revenue: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease in Revenue: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

# Output Files
with open("budget_output", "w") as txt_file:
    txt_file.write("\n")
    txt_file.write("Financial Analysis")
    txt_file.write("----------------------")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes), 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
