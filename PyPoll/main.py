import csv

# The use of OrderDict ensures that it will keep the order of the keys.
# Reference: https://docs.python.org/3.6/howto/sorting.html
# https://www.blog.pythonlibrary.org/2016/03/24/python-201-ordereddict/
# THANKS GOOGLE FOR EVERYTHING!!!!!
from collections import OrderedDict
from operator import itemgetter

# file path
election_path = "Resources/election_data_1.csv"
election_analysis = "Resources/election_analysis.txt"

# Trackable Variable
votes = 0
winner_votes = 0
total_candidates = 0
candidate_options = []
candidate_votes = {}

with open(election_path) as election_data:
    csvreader = csv.DictReader(election_data)

    for row in csvreader:
        votes += 1
        total_candidates = row["Candidate"]

        if row["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

# Print the answer
print()
print()
print("Election Results")
print("--------------------------")
print("Total Votes " + str(votes))
print("--------------------------")

for candidate in candidate_votes:
    print(candidate + " " + str(round(((candidate_votes[candidate] / votes) * 100))) + "%" + "(" + str(candidate_votes[candidate]) + ")")

    candidate_results = (candidate + " " + str(round(((candidate_votes[candidate] / votes) * 100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

    # Reference: https://stackoverflow.com/questions/18595686/how-does-operator-itemgetter-and-sort-work-in-python
    candidate_votes
    winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("--------------------------")
print("Winner: " + str(winner[0]))
print("--------------------------")

# Output files
with open(election_analysis, "w")as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("--------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("--------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
