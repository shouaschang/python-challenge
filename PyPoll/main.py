# Assignment 3
# Cohort 4
# main.py document for PyPoll analysis

# Resources: election_data.csv
# Data columns: Voter ID[0], County[1], Candidate[2]

# INSTRUCTIONS
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winer of the electin based on popular vote

import os
import csv

csvpath = os.path.join(".", 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        print(row)
