import os
import csv
from operator import itemgetter

election = os.path.join("..","Desktop","election_data.csv")


votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


with open(election) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

# Output to txt file
output_path = os.path.join("..","Desktop","election_data.txt")

# with open("election_data.txt", "w") as text_file:

    # Initialize csv.writer
file = open("testfile.txt","w") 
 
file.write("Election Results\n") 
file.write("----------------------------\n") 
file.write("Total Votes: " + str(votes) + "\n")
file.write("----------------------------\n") 
 
file.close() 

    # # Write the first row (column headers)
    # csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # # Write the second row
    # csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

