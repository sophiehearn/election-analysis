# Election Analysis 

This code determines the winner of a local election by analyzing a CSV file, containing the votes, tallying the votes of each candidate, and comparing vote totals to determine a winner. 
This Election Audit was conducted in three counties in Colorado (Jefferson, Denver, and Arapahoe), and also analyzes the voter turnout within the three counties.

## Summary Results

- Total votes: 399,711

#### Candidate Outcomes
- Candidates: Diana DeGette, Charles Casper Stockham, Raymon Anthony Doane. 
- Winner: Diana DeGette (73.8%, 272,892 votes)
- Runner-Up: Charles Casper Stockham (23%, 85,213 votes)
- Other Candidate: Raymon Anthony Doane (3.1%, 11,606 votes)

#### County Turnout 
- Denver: 82.8%, 306,055 votes 
- Jefferson: 10.5%, 38,855 votes
- Arapahoe: 6.7%, 24,801 votes

## Audit Methodology
In order to conduct this audit, we initially needed to import the os and csv modules in python to read data from a csv and write data to a text file. 
```
import csv
import os
```
After initializing variables, lists, and dictionaries for both candidates and counties, we opened the file and used a for loop to loop through every row in the data. 
The first function tallied the total votes `total_votes = total_votes + 1`, then we pulled the names of the candidate from each row, and used an if statement to add it to our list of candidate names if it wasn't already listed. Finally, we added a tally to that candidates vote total in the dictionary. 
```
        # Get the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```
This process was repeated with the counties to determine the vote totals within each county.

To determine which candidate was the winner and which county had the largest turnout, we looped through the dictionary to retrieve the vote totals for each county / candidate and then compared those to our "largest county" or "winning candidate" variables. Using an if statement, we determined whether the current value was larger than the largest previous value. If so, the current value is now set as the "winning" or "largest" variable, and the subsequent data is changed as well. 
For the counties, this looked like:
```
        if cvotes > largest_turnout_count: 
            largest_turnout_count = cvotes
            largest_turnout_county = county_name
            largest_turnout_percentage = cvote_percentage
```

All of this data was then written into an opened text file using f strings. 
Here is an example of the code used to write into the text file.
```
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

    txt_file.write(election_results)
```

The resulting text file gave the following output:  
![Election_Results](https://raw.githubusercontent.com/sophiehearn/election-analysis/main/Resources/Election%20Results.png)

This gives us the final summary or candidate votes as well as county vote turnout.

## Replicating the Methodology for Future Use
The structure of this code could be used to udit future elections with a few minor adjustments. It can function to tally votes for candidates, counties, or other information. The code would need to be modified to adjust to the correct row of data (candidate, county, etc) that is being tallied. 
e.g. in this code on line 47: 
```
# Get the candidate name from each row.
candidate_name = row[2]
```
The user would need to confirm which row the candidate information is in based on the data. 

For ease of reading, the variable names should be changed to reflect what is being tallied. 
e.g. in this code we are tracking candidates but these variables and list/dict names (among others) should be edited if one were tallying something else: 
```
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```

And of course, the f-string outputs to print and record the information should be edited to correctly reflect the content of the data. 
e.g. this code tracks the largest turnout per county: 
```
    largest_turnout_county_summary = (
        f"-------------------------\n"
        f"Largest Turnout County: {largest_turnout_county}\n"
        f"Largest Turnout Vote Count: {largest_turnout_count:,}\n"
        f"Largest Turnout Percentage of Total Votes: {largest_turnout_percentage:.1f}%\n"
        f"-------------------------\n"
        f"\nCandidate Votes:\n")
```
This output should be edited to reflect the specificities of the relevant data. 

Ultimately this code can be useful, with some small modifications, to tally numbers of almost any variable in a CSV file. 
