# Assignment 3
# Cohort 4
# main.py document for PyBank analysis

# Resources: budget_data.csv
# Data columns: Date[0] and Profit/Losses[1]

# INSTRUCTIONS
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The average of the changes in "Profit/Losses" over the entire period
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in losses (date and amount) over the entire period

# Importing packages for CSV file
import os
import csv

# Loading CSV file source
csvpath = os.path.join(".", 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # data = list(csvreader)
    # row_count = len(data) #total of 87 rows
    # print(len(data))
    # print(csvreader)
    
#   csv_header = next(csvreader)
#   print(f"CSV Header: {csv_header}")
    
#   for row in csvreader:
#       print(row)
    
    
 
 