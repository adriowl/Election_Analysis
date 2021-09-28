##PyPoll.py - for analyzing election result data 
import csv
import os

##Open then loop through Resources/election_results.csv
##Create path using os join to join two paths together
file_to_load = os.path.join("Resources", "election_results.csv")

##1. total_votes - int - keep a count of looped rows
##2. candidate_options - list - if cand not in list, append it
##3. candidate_votes - dict - find key in votes dict (if not found, add it) and increment value (int which represents vote)
##4. PercentageDict - dict- loop through VotesDict, divide by Total, times by 100
##5. Winner - str - return cand with highest percentage
total_votes = 0
candidate_options = []
candidate_votes = {}
#Using this with syntax avoids having to close the file at the end
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        #Increment votes
        total_votes+=1
        #Add candidate to list & dict 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #Increment vote
        candidate_votes[candidate_name]+=1

print(total_votes)
print(candidate_options)
print(candidate_votes)

#who won? winner = string, winning_count = int, winning_percent = float.
winner = ""
winning_count = 0
winning_percent = 0
for cand in candidate_options:
    votes = candidate_votes[cand]
    percent = round((votes/total_votes)*100,2)
    print(f'{cand} got {percent}% of the votes, with a count of {votes}')
    if votes > winning_count:
        winner = cand
        winning_count = votes
        winning_percent = percent
print(f'----------------------------------------------------------\n'
    f'The winner is {winner} with {winning_percent}% of the votes!\n'
    f'----------------------------------------------------------\n')
#Create path for output file and open it
file_to_write = os.path.join("Analysis","election_analysis.txt")
with open(file_to_write, "w") as outfile:
    outfile.write(f'Election Results\n'
    f'--------------------------------\n'
    f'Total Votes: {total_votes}\n'
    f'--------------------------------\n')
    for cand in candidate_votes:
        candvote = candidate_votes[cand]
        candpercent = round((candvote/total_votes)*100,2)
        outfile.write(f'{cand}: {candpercent} ({candvote})\n')
    outfile.write(f'--------------------------------\n')
    outfile.write(f'Winner: {winner}\n')
    outfile.write(f'Winning Vote Count: {winning_count}\n')
    outfile.write(f'Winning Percentage: {winning_percent}\n')
    outfile.write(f'--------------------------------\n')

