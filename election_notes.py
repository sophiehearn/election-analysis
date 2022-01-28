# Deliverables for this analysis
## Total number of votes cast
## A complete list of candidates who received votes
## Total number of votes each candidate received
## Percentage of votes each candidate won
## The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#import csv module 
import csv

import os

file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
