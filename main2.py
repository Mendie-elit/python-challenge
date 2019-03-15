#Define modules to open csv files
#convert operating system
import os
#open a csv file
import csv

import subprocess

#create csv file path 
budgetDataPath = os.path.join('..','PyPoll','election_data.csv')

#Open the CSV file and save into variable called csvfile
with open(budgetDataPath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #csv_row_list = list(csvreader)
    next(csvreader)
#Create open lists to  populate later with values
    Votes = []
    Candidates = []
    Unique_Candidates_list = []
    Candidate_Vote_Count = []
    Candidate_Percent_Votes = []
    
# Populate Vote and Candidate lists
    for row in csvreader:
        Votes.append((float(row[0])))
        Candidates.append(row[2])
# Find total number of votes from counting the objects in the list
    Total_votes = len(Votes)
# Find the unique Candidate names from list of Candidates
    for candidate_name in Candidates:
        if candidate_name not in Unique_Candidates_list:
            Unique_Candidates_list.append(candidate_name)
        else:
            continue
#Find vote count for each candidates
    for name in Unique_Candidates_list:
#if each_candidate in Candidates:
        count = Candidates.count(name)
        Candidate_Vote_Count.append(count)
# calculate % of votes
        Percent_of_votes = round((count/Total_votes*100), 4)
        Candidate_Percent_Votes.append(Percent_of_votes)

#Find the index of the winner so can return name from Unique Candidate List then use value to index from list
        winner_position = Candidate_Percent_Votes.index(max(Candidate_Percent_Votes))           

 
print("Election Results") 
print("------------------------")
print(f"Total votes: {Total_votes}")
print("------------------------")
for i in range(4):
    print(f"{Unique_Candidates_list[i]}: {Candidate_Percent_Votes[i]}% ({Candidate_Vote_Count[i]})")
print("------------------------")
print(f'Winner: {Unique_Candidates_list[winner_position]}')
print("------------------------")

#Export to text file
with open("Election_OutPut.text", "w+") as f:
    subprocess.check_call(["python", "main2.py"], stdout=f)            


