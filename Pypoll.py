##PyPoll.py - for analyzing election result data 
import csv
import os

##Open then loop through Resources/election_results.csv
##Create path using os join to join two paths together
file_to_load = os.path.join("Resources", "election_results.csv")

#Using this with syntax avoids having to close the file at the end
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

##1. TotalVotes - int - keep a count of looped rows
##2. CandidateList - list - if cand not in list, append it
##3. VotesDict - dict - find key in votes dict (if not found, add it) and increment value (int which represents vote)
##4. PercentageDict - dict- loop through VotesDict, divide by Total, times by 100
##5. Winner - str - return cand with highest percentage

#Create path for output file and open it
file_to_write = os.path.join("Analysis","election_analysis.txt")
with open(file_to_write, "w") as outfile:
    outfile.write('hi\nhello\nhola')

