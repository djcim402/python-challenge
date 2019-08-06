import os
import csv
from operator import itemgetter

election = os.path.join("..","Desktop","election_data.csv")

# Variables
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


with open(election) as election_data:
    csvreader = csv.reader(election_data,delimiter=",")

    # Skip headers
    next(csvreader, None)

    for row in csvreader:
        total_votes = total_votes + 1      

        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1


 # Make lists
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Find the winner
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Summary results
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#Print summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output to txt file
output_path = os.path.join("..","Desktop","election_data.txt")

# with open("election_data.txt", "w") as text_file:
with open(output_path,"w") as txt_file:

    txt_file.write(f"Election Results")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {total_votes}")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    txt_file.write("\n")
    txt_file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    txt_file.write("\n")
    txt_file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    txt_file.write("\n")
    txt_file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Winner: {key}")
    txt_file.write("\n")
    txt_file.write(f"----------------------------")


    
    